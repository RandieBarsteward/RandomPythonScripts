from collections import Counter


lst = ['fee', 'fie', 'fee', 'fum']
cl = Counter(lst)
print(cl)
print("No. of foes:", cl['foe'])

c12 = Counter(squirls=42, rabbits=395, moles=12)
print("Pests:",sum(c12.values()))
print(c12.most_common())