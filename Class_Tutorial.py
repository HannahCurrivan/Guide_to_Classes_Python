# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:02:46 2019

@author: hcurrivan
"""


class rocket:
    
    # name and years of launch
    types = 'space rockets'
    
    
    def _init_(self, name, year):
        self.name = name
        self.year = year 


# Instantiate the object:
rocket1 = rocket("Saturn_5", 1967)
rocket2 = rocket("Ariane_5", 1996)

#Access:
print("{} first launch was in {} and {} first launch was in {}.".format(
        rocket1.name,rocket1.year,rocket2.name,rocket2.year))

# Is it a rocket:
if rocket1.types == 'space rockets':
    print("{0} is a {1}!".format(rocket1.name,rocket1.year))
