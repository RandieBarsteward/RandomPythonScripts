import operator

cats = ['frank', 'Ron', 'Jess', 'Phil']

itemsorter = operator.itemgetter(0)
cats.sort(key=itemsorter)

print(cats)