#sorting by list subkeys

import operator

cats = [['frank',14,56.5], ['Ron',8,70], ['Jess',7,0], ['Phil',3,150]]

itemsorter = operator.itemgetter(1)
cats.sort(key=itemsorter)

print(cats)