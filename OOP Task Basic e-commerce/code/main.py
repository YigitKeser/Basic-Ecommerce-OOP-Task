#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:58:01 2020

@author: yigitkeser
"""
import Company
import Product
import Customer

class main():
    
    
    def __init__(self,name):
        self.name = Company.Company(name, "", "", "")
        
    def __str__(self):
        return self.name.company_name
        
    def welcome(self):
        print("Welcome to {}\n".format(self.name))
    
    def is_str(check_input):
        if check_input.isalpha():
            return True
        print("Please enter alphabetical character")
        return False
            
    def is_digit(check_input):
        if check_input.isdigit():
            return True
        if check_input != 'q':
            print("Please enter digit")
        return False
        
    def user_login(self):
        login = 0
        while login == 0:
            username = str(input("Please login with name : "))
            if main.is_str(username):
                for i,customer in enumerate(self.customers):
                    if customer.customer_name == username:
                        print("Welcome {}".format(self.customers[i].customer_name))
                        login+=1
                        return self.customers[i]
                        break
                else:
                    print("Username not found , please try again")

     
    def menu(self):
        user = main.user_login(self)
        while True:
            print("""\nWhat would you like to do ?\n
1. Show My Information
2. Add Credit
3. Buy Product
4. Show {} Products
q. Quit""".format(self.company_name))
            choice = input()
            if main.is_digit(choice):
                
                if choice == '1':
                    print(user)
                    
                if choice == '2':
                    subchoice2 = input("Please enter amount : ")
                    if main.is_digit(subchoice2):
                        user.add_credit(subchoice2)
                
                if choice == '3':
                    print("Available products :")
                    for i,product in enumerate(self.products):
                        print("{} , Qty : {}".format(self.products[i],self.quantities[i]))
                    print("Which product do you want ? ")
                    subchoice3 = input()
                    if main.is_str(subchoice3):
                        defined_product = 0
                        for i,product in enumerate(self.products):
                            if str(subchoice3) == str(product.name):
                                p = product
                                defined_product+=1
                                break
                        else:
                            print("Product not found")

                        if defined_product>0:
                            subchoice4 = input("How many : ")
                            if main.is_digit(subchoice4):
                                if int(subchoice4) > int(self.quantities[i]):
                                    print("Theres not enough product in {}".format(self.company_name))
                                if int(subchoice4)*int(p.price) > int(user.credit):
                                    print("Theres not enough credit for this transaction")
                                else:
                                    user.buy_product(p,subchoice4)
                                    self.quantities[i]-=int(subchoice4)
                                    print("{} (qty:{}) sold to {}".format(p.name,subchoice4,user.customer_name))
                        
                if choice == '4':
                    print(self.print_products())
                
            
            else:
                if main.is_str(choice) and choice == 'q':
                    print("Goodbye")
                    break

amazon = main('Amazon').name
amazon.load_database()
main.menu(amazon)






