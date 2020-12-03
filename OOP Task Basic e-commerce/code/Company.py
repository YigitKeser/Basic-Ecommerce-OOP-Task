#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:34:08 2020

@author: yigitkeser
"""

import csv
import Product
import Customer


class Company:
    
    def __init__(self, company_name, products, quantities, customers):
        self.company_name = company_name
        self.products = []
        self.quantities = []
        self.customers = []            
    
    
    def load_database(self):
        p = Product.Product
        c = Customer.Customer
        with open('products.txt', 'r') as f:
            reader = csv.reader(f, delimiter = ';')
            for row in reader:
                self.products.append(p(row[0], int(row[1])))
                self.quantities.append(int(row[2]))
        
        with open('customers.txt', 'r') as f:
            reader = csv.reader(f, delimiter = ';')
            for row in reader:
                self.customers.append(c(row[0], int(row[1]), '', ''))
        
        
    def print_products(self):
        for i,product in enumerate(self.products):
            print("{} \tPrice : {}TL, Qty : {}".format(product.name, product.price, self.quantities[i]))
            
    def print_customers(self):
        for i,customer in enumerate(self.customers):
            print(customer.customer_name)