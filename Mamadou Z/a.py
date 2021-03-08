# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:55:32 2021

@author: MaMadou
"""

# Enter the string to be reversed
StringToReverse= input("Please enter a word or phrase: ")
revStr = ""

#Reverse the string
for reverse in StringToReverse:
    revStr = reverse + revStr

#Print the reversed string
print("The reverse is: ",revStr)