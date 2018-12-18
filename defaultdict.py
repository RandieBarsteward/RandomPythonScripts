from collections import defaultdict

def GetDefault():
    return 'no value set'

dd1 = defaultdict(GetDefault, {'key1':'val1', 'key2':'val2',})
print("Key3:", dd1['key3'], "key4:", dd1['key4'])

dd2 = defaultdict(lambda:len(dd2))
print(dd2['key1'], dd2['key2'], dd2['key3'], dd2['key4'])
