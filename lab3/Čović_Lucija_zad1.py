# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:59:28 2020

@author: Lucija
"""

import json

#prva='{"Croatia": "Split", "USA": "New York"}'
#druga='{"UK": "London", "Germany": ["Berlin", "Burghausen"]}'

#def spoji(prva,druga):
#    prva_dict=json.loads(prva)
#    druga_dict=json.loads(druga)
#    prva_dict.update(druga_dict)
#    prva_json=json.dumps(prva_dict) #da vrati JSON file
#    return prva_json

#print(spoji(prva,druga))

with open('prva.json') as prva, open('druga.json') as druga:
    first_list = json.load(prva)
    second_list = json.load(druga)

print("Prva: ", first_list, "\nDruga: ", second_list, "\n") #uredno ih učita

def spoji(first_list, second_list):
    first_list.update(second_list)
    return first_list

print("Spojene:\n", spoji(first_list, second_list))