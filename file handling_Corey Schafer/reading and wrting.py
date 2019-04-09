
# first let's clear the file
f = open('dummy3.txt', 'r+')
f.truncate(0)

# let us read the contents of dummy.txt and copy it into dummy3.txt
with open('dummy.txt', 'r') as rf:
    with open('dummy3.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
