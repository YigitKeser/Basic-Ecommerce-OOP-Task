#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:46:45 2020

@author: yigitkeser
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:40:29 2020

@author: yigitkeser
"""

class Customer:
    
    def __init__(self, customer_name , credit, owned_products, quantities):
        self.customer_name = customer_name
        self.credit = credit
        self.owned_products = []
        self.quantities = []
    
    def __str__(self):
        return "Name : {}\nCredit : {}\nOwned Products : {}\nQuantities : {}\n".format(self.customer_name,
                                                                                         self.credit,
                                                                                         self.owned_products,
                                                                                         self.quantities
                                                                                         )
        
    def buy_product(self,product,qty):
        self.owned_products.append(product.name)
        self.quantities.append(qty)
    
    def show_products(self):
        for i , product in enumerate(self.owned_products):
            print(product,self.quantities[i])
    
    def add_credit(self,amount):
        self.credit+= int(amount)
        print("Your credit is currently : {}TL".format(self.credit))