import re

def getter(url):
    _pattern = r'(https?://|ftp://)([^/]*)'
    return re.findall(_pattern, url)[0][1]
