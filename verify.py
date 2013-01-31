from __future__ import with_statement

with open('corn.diff', 'r') as f:
    data = f.read()
    if len(data) == 116:
        print 'Success!'
    else:
        print 'Failure'
