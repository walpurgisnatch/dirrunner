# dirrunner
Simple tool for path traversal attacks

## Basic Usage
```
python3 dirrunner.py -u https://example.com/someurl
```

### Depth
Amount of subdirectories to dig in can be specified with the `-d` flag. 
Default = 12.
```
python3 dirrunner.py -u https://example.com/someurl -d 8
```

### File
To specify file to try to get access, use `-f` flag. 
By default script will try to get access to list of common files.
```
python3 dirrunner.py -u https://example.com/someurl -f /var/www/html/index.html
```
