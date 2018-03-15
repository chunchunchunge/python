# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 15:15:04 2018

@author: Chun
"""


size_of_tank  = raw_input('size of tank(m3):')
percent_full  = raw_input('percent full(%):')
km_per_liter  = raw_input('km per liter(km/h):')
another_distance = float(size_of_tank)*0.01*float(percent_full)*float(km_per_liter)
print "size of tank:"+size_of_tank
print 'pecent full :'+percent_full
print 'km per liter:'+km_per_liter
print 'you can go another %d km'% another_distance
if another_distance <200:
    print 'you cannot wait for next station(200km from your station)'
else:print 'you can wait for next station'
