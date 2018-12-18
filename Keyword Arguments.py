import sys

def myfunc(**UserArgs):
    args = {'country' : 'England', 'town' : 'London', 'currency': 'Pound', 'Language':'English'}
    diff = set(UserArgs.keys()) - set(args.keys())
    if diff:
        print("Invalid args:", tuple(diff), file=sys.stderr)
        return
    args.update(UserArgs)
    print(args)

mydict = dict(town = 'Glasgow', country = 'Scotland')
myfunc(**mydict)
myfunc(twn = 'Glasgow', country = 'Scotland')