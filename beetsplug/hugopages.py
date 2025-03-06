import os
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
import frontmatter
import datetime


class HugoPagesPlugin(BeetsPlugin):
    def __init__(self):
        super().__init__()
    
    def commands(self):
        validate_command = Subcommand('hugo', help='Check Hugo pages config is valid')
        validate_command.func = self.validate

        full_sync_command = Subcommand('hugo-sync', help='Sync Hugo pages with beets library')
        full_sync_command.func = self.do_full_sync
        return [validate_command, full_sync_command]
    
    def validate(self, lib, opts, args):
        print('Checking the hugo pages config is valid...')
        try:
            self._check_valid()
            print("Config looks good")
        except Exception as e:
            print('Error: {}'.format(e))

    def _check_valid(self):
        """Check config, throw exceptions"""
        album_path = self.config['album_path'].get()
        if not os.path.exists(album_path):
            raise ValueError('Album path does not exist: {}'.format(album_path))
    
    def _get_album_path(self, album_id):
        return os.path.join(self.config['album_path'].get(), f"{album_id}.md")
        
    def do_full_sync(self, beets_library, opts, args):
        print('Syncing Hugo pages with beets library...')
        try:
            self._check_valid()
        except Exception as e:
            print('Error: {}'.format(e))
        
        albums = beets_library.albums()
        for album in albums:
            album_id = album.get('id')
            album_path = self._get_album_path(album_id)
            
            post = PostHandler(album_path)
            post.copy_key('beets_id', album, read_key='id')
            post.copy_key('title', album, read_key='album')
            post.copy_key('artist', album, read_key='albumartist')
            if post.write():
                print(f"Updated {album_path}")
            else:
                print(f"No update: {album_path}")
        print('Sync complete')

class PostHandler:
    def __init__(self, path):
        self.path = path
        self.dirty = False
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.post = frontmatter.load(f)
        else:
            self.post = frontmatter.Post("")
            self.dirty = True
    
    def copy_key(self, key_name, source, read_key=None):
        if read_key is None:
            read_key = key_name
        
        val = source.get(read_key)
        existing_val = self.post.get(key_name, None)
        if val != existing_val:
            self.post[key_name] = val
            self.dirty = True
    
    def write(self):
        if self.dirty:
            with open(self.path, 'wb') as f:
                frontmatter.dump(self.post, f)
            self.dirty = False
            return True
        return False