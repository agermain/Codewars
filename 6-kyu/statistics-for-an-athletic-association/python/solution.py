import re
import statistics
from time import strftime
from time import gmtime

pattern = re.compile(r'([\d]+)\|([\d]+)\|([\d]+)')
def stat(strg):
    if strg == "":
        return "" 
    matches = pattern.finditer(strg)
    l = []
    for match in matches:
        l.append(int(match.group(1)) * 3600 + int(match.group(2)) * 60 + int(match.group(3)))
    rng = max(l) - min(l)
    avg = statistics.mean(l)
    mdn = statistics.median(l)
    return 'Range: {} Average: {} Median: {}'.format(strftime("%H|%M|%S", gmtime(rng)), strftime("%H|%M|%S", gmtime(avg)), strftime("%H|%M|%S", gmtime(mdn)))