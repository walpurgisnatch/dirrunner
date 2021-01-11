# dirrunner
Simple tool for path traversal attacks

## Basic Usage
```
python3 dirrunner.py -u https://example/com/someurl
```

## Depth
You can set the amount of subdirectories to dig in with the `-d` flag. 
Default = 12.
```
python3 dirrunner.py -u https://example/com/someurl -d 8
```

## File
To specify file to try to access, use `-f` flag. 
Default - "/etc/passwd"
```
python3 dirrunner.py -u https://example/com/someurl -f /var/www/html/index.html
```
