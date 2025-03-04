from beets.plugins import BeetsPlugin
from beets.ui import Subcommand

def hugo_pages(lib, opts, args):
    print('Hugo pages')

status_command = Subcommand('hugo', help='Generate Hugo pages from beets library')
status_command.func = hugo_pages

class HugoPagesPlugin(BeetsPlugin):
    def __init__(self):
        super().__init__()
        self.register_listener('pluginload', self.loaded)

    def loaded(self):
        self._log.info('Hugo plugin is loaded...')
        print('Hugo plugin is loaded...')
    
    def commands(self):
        return [status_command]
