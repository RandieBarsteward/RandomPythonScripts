import glob, os, os.path

def get_dir(path):

    while True:
        pattern = os.path.join(path, '*')
        path = None
        for file in glob.iglob(pattern):
            if os.path.isdir(file):
                path = yield file
                if path: break

        if not path: break

gen = get_dir('C:\Program Files')

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(gen.send('C:\Program Files (x86)'))
print(next(gen))