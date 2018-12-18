
from collections import ChainMap

pc_components = {'motherboard' : 150, 'ram': 120,'cpu' : 250,'psu' : 55, 'case':70}
pc_options = {'hd' : 150, 'basic_gpu': 120, 'gamaing_gpu' : 250}
pc_accessories = {'keyboard':30, 'mouse':40, 'ram':40}

pc_pricing = ChainMap(pc_accessories, pc_options,pc_components)

print(type(pc_pricing))

print(pc_pricing['hd'])

print(pc_pricing['ram'])

pc_nice_to_have = {'vr':300}

pc_extra_pricing = ChainMap(pc_nice_to_have, pc_pricing)

print(pc_extra_pricing['basic_gpu'])
print(pc_extra_pricing['vr'])

pc_options.pop('hd', None)

print(pc_pricing['hd'])