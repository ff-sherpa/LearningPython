# potholes.py
# Analyze potnole data to find 10 block section with most potholes.

import csv
import operator

# create dictionary
potholes_by_block = {}

def make_block(address):
    ''' Rewrite an address to strip address in 1000s (10 blocks)'''
    parts = address.split()
    num = parts[0]  
    new = num[:-3]  # or new = parts[0][:-3]

    # for number like '5412', this makes '5XXX'
    # parts[:-3] = grab everything except the last 3 characters
    parts[0] = num[:-3] + 'XXX'
    #print parts[0]
    return ' '.join(parts)


f = open('pothole_data.csv')
for row in csv.DictReader(f):
    status = row['STATUS']
    
    if status == 'Open':
        addr = row['STREET ADDRESS']
        block = make_block(addr)
        num  = row['NUMBER OF POTHOLES FILLED ON BLOCK']

        # Tabulate
        # will build dictionary as follows:
        # 4XXX W 56th St: num_or_potholes
        if block not in potholes_by_block:
            # this is the first occurance of address
            potholes_by_block[block] = 1
        else:
            potholes_by_block[block] += 1

# find block with max potholes
xx = max(potholes_by_block.iteritems(), key=operator.itemgetter(1))[0]

# sorted
sorted_blocks = sorted(potholes_by_block.items(), key=operator.itemgetter(1))

print sorted_blocks

print xx, '=>', potholes_by_block[xx]
