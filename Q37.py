# Let’s say we have a group of N friends represented by a list of dictionaries where each value is a friend name and their location on a three dimensional scale of (x,y,z). The friends want to host a party but want the friend with the optimal location (least distance to travel as a group) to host it.

# Write a function pick_host to return the friend that should host the party.

# Example:

# Input:

# friends = [
# {'name': 'Bob', location: (5,2,10)},
# {'name': 'David', location: (2,3,5)},
# {'name': 'Mary', location: (19,3,4)},
# {'name': 'Skyler', location: (3,5,1)},
# ]

# def optimal_host(friends) -> 'David'

import math

def pick_host(friends):
    mindis=math.inf
    hostperson=""

    for i in friends:
        dis=math.sqrt(i['location'][0]**2 + i['location'][1]**2 + i['location'][2]**2)
        if dis<mindis:
            mindis=dis
            hostperson=i['name']
    return hostperson

friends = [
    {'name': 'Bob', 'location': (5, 2, 10)},
    {'name': 'David', 'location': (2, 3, 5)},
    {'name': 'Mary', 'location': (19, 3, 4)},
    {'name': 'Skyler', 'location': (3, 5, 1)}
]

print(pick_host(friends)) 
