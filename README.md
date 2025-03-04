There is a bit of magic setup required here.

Create a venv and use it:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Link this dir to where beets expects it
```
mkdir -p ~/.config
ln -s $PWD ~/.config/beets
beet config # this should show the config settings
```

Python path

Find the site-packages dir
```
cd $(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
```

Pop this dir in there
```
echo "$INSTALL_LOCATION/record-library" > lib.pth
```