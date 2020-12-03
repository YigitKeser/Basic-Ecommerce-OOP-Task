#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:58:12 2020

@author: yigitkeser
"""

class Product:
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return "Name : {} , Price : {}".format(self.name,self.price)