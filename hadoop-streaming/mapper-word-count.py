#!/usr/bin/python2.6                        
# -*- coding: utf-8 -*-                     
                                            
import sys                                  
                                            
result = {}                                 
for line in sys.stdin:                      
        key, value = line.split("\t")       
        if  key not in result:              
                result[key] = 0             
        result[key] += 1                    
                                            
for key, value in result.items():           
        print("{1}\t{0}".format(key, value))
