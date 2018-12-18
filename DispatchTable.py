def spiral(cobj):
    print(cobj, "is a spiral galaxy")

def open_cluster(cobj):
    print(cobj, "is an open cluster")

dtab = {}
dtab['M31'] = spiral
dtab['M32'] = spiral
dtab['M41'] = open_cluster
#dtab['M42'] = glob_cluster

cobject = input("Enter a Messier number: ")
if cobject in dtab:
    dtab[cobject](cobject)
else:
    print(cobject, "is unknown")