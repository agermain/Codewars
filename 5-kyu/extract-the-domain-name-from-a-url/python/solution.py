import re
def domain_name(url):
    pattern = re.compile("[https://|http://]?(www\.)?([A-Z0-9a-z\-]+)\.[A-Za-z]+")
    matches = pattern.findall(url)
    print(url)
    return matches[0][1]