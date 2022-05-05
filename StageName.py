# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:48:29 2020

@author: UMAIR ASLAM
"""

import random #module to select a name randomly
import string
#numberName () function takes the input for numbe of names
def numberName():
    while True:
        valor = input("How many names do you want to create: ")
        try:
            valor = int(valor)
            if valor > 0 :
                
                return valor
            else: raise (ValueError)
        except ValueError:
            print ("Please, insert a valid number. ")
#generates stage name
def generate_stage_name(name):
    n=name
    #list from which random add on name is chosen
    random_names = ["Folerpa","Lostrego","Saraiba","Axouxere","Treboada","Orballo","Bretema","Loaira","Bagoa","Luar"]
    #split the name into firstname and lastname
    n=n.split()
    #Make the first name lower case and lastname uppercase. Also, take the initial from first name and make it upper case
    first_name=n[0]
    temp_initials=list(first_name)
    initial=temp_initials[0]
    initial=initial.upper()
    first_name=first_name.lower()
    Last_name=n[1]
    Last_name=Last_name.upper()
    #return the stage name
    return (initial+'. '+random.choice(random_names)+' '+Last_name+' '+first_name+' '+random.choice(random_names))

#Begin Main Program
#Assign the number of names user is going to put to num_names    
num_names=numberName()
#Initialize name list
name=[]
#Start taking name in the form 'firstname lastname' as input from the user
s = set(string.ascii_lowercase+string.ascii_uppercase+'.'+'\''+'-'+' ')
for i in range(num_names):
    #Check is a flag to know if the name input by the user is according to the requirement
    check=0
    #take name as input
    name.append(input('Enter you name in the format(firstname lastname):'))
    
    #To check if input name satisfies all requirements
    test=[]
    test=name[i].split(' ')
    #make sure that there is firstname and lastname in the input name
    while True:
        while  len(test)!=2 or s.issuperset(name[i])==False:
            #if the input name has more than 2 names then ask for input again
            name.pop(i)
            print('Invalid input name')
            name.append((input('Enter you name in the format(firstname lastname):')))
            test.clear()
            test=name[i].split(' ')
            #Check if the name is only alphabets and only allowed other characters are -. ' and .
        break
                                                
                       
#Initialize a variable to store stage name(s)
stage_name=[]
#Send each name to generate_stage_name(), get stage name, display name followed by stage name
print()
print(f"Name\t\tStage Name")
for i in range(num_names):
    stage_name.append(generate_stage_name(name[i]))
    print(f"{name[i]}\t{stage_name[i]}")
    
