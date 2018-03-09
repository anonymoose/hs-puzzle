#
# Follow the breadcrumbs, with some bumps in the middle, until you get to the end.
#

import requests
import time
import re

# Start with the breadcrumb we get by solving the previous crumb.
BASE = 'https://challenge.hiringsolved.com/breadcrumbs'
crumb = 62605


def has_number(s):
    return any(i.isdigit() for i in s)


#
# Follow the breadcrumbs until we are told what to add.  Only add it once.
# If there's no digit, we're done.
#
keep_going = True
while keep_going:
    time.sleep(0.1)
    r = requests.get('%s/%d' % (BASE, crumb))
    print(r.text)
    if has_number(r.text):
        if r.text.startswith('Yes.'):
            matches = re.findall(r'\b\d+\b', r.text)
            add_to = int(matches[0])
            crumb = crumb + add_to
        else:
            crumb = int(r.text[-5:])
    else:
        # we didn't find a breadcrumb.  so stop after having printed out the content.
        keep_going = False
