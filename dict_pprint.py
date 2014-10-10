import pprint

default = 'DEFAULT'

dog_owned_by = dict({'Sally': 'fido', 'DJ': 'spike'})

dogs = []

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dog_owned_by)

#for owner in ('Sara', 'Sally', 'Virgil', 'DJ'):
#    dogs.append(dog_owned_by.setdefault(owner, default))

#pprint(dog_owned_by)
#print "\n"
#{'DJ': 'spike', 'Sally': 'fido', 'Sara': 'DEFAULT', 'Virgil': 'DEFAULT'}

#tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', ('parrot'), ('fruit',)))))))

#stuff = ['a' * 10, tup, ['#' * 30, '&' * 30,], ['!' * 10, '?' * 10]]
#pprint.pprint(stuff)
#print "\n"
#pprint.pprint(stuff, depth=3)
#print "\n"
#pprint.pprint(stuff, width=60)

