
# I have a picture file called 'Pabba' in this directory, for reference
# Pictures are read and written in binary mode
# hence, use 'rb' for reading and 'wb' for writing
with open('Pabba.jpg', 'rb') as ri:
    with open('Pabba_Copy.jpg', 'wb') as wi:
        for line in ri:
            wi.write(line)

# To have more control, we can specify the size of chunks
with open('nmc logo.jpg', 'rb') as ri:
    with open('nmc logo_Copy.jpg', 'wb') as wi:
        size_of_chunk = 4096
        ri_chunk = ri.read(size_of_chunk)
        while len(ri_chunk) > 0:
            wi.write(ri_chunk)
            ri_chunk = ri.read(size_of_chunk)