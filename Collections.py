#Collections 
import collections 
from pprint import pprint 
from functools import reduce

#collections named tuple

Scientist = collections.namedtuple('Scientist',['name', 'field', 'born','nobel'])
scientists = (Scientist(name='Ada Lovelace',field='physics',born=1815,nobel=True))
pprint(scientists)

#Filter 
new_nobel= tuple(filter(lambda x: x.nobel is True, scientists))
pprint(new_nobel)

physics = tuple(filter(lambda x: x.field=='physics',scientists))
pprint(physics)

#reuse a filter 
def nobel_filter(x):
    return x.nobel is True 
pprint(tuple(filter(nobel_filter, scientists)))

#Use list comprehension 
pprint(tuple(x for x in scientists if x.nobel is True))

#using map
names_and_ages = tuple(map(lambda x: {'name': x.name,'age': 2023-x.born}, scientists))
pprint(names_and_ages)

#use the names_and_ages tuple and determine overall age of the group
total_age = reduce(lambda x,y:x+y['age'], names_and_ages,0)
tot_age = sum(x['age'] for x in names_and_ages)
print(tot_age)
