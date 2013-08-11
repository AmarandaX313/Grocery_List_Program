# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:37:02 2013

@author: heather
"""
import pickle
import os
import time


grocery_list = []

def create_list(grocery_list, item):
    list = { 
    'item' : item,
    }
    grocery_list.append(list)

def test(grocery_list, abcd):
    return "Command 'test' returned:\n" + \
        "abcd: " + abcd

def save_grocery_list():
    save_file = file("grocery_list.pickle", "w")
    pickle.dump(grocery_list, save_file)
    save_file.close()
    
def load_grocery_list():
    global grocery_list
    if os.access("grocery_list.pickle", os.F_OK):
        save_file = file("grocery_list.pickle")
        grocery_list = pickle.load(save_file)

def delete_list(grocery_list, which):
    if not which.isdigit():
        return ("'" + which +
            "' needs to be the number of the item!")
    which = int(which)
    if which < 1 or which > len(grocery_list):
        return ("'" + str(which) +
                "' needs to be the number of an item!")
    del grocery_list[which-1]
    return "Deleted item #" + str(which)
    
def delete_all_list(grocery_list):
    del grocery_list[:]
    save_grocery_list()
    return "Deleted the whole list"

def get_function(command_name):
    return commands[command_name][0]

def get_fields(command_name):
    return commands[command_name][1]    

def run_command(user_input, data=None):
    user_input = user_input.lower()
    if user_input not in commands:
        return user_input + "?" \
            "I don't know what that command is."
    else:
        the_func = get_function(user_input)
        
    if data is None:
        the_fields = get_fields(user_input)
        data = get_input(the_fields)
    return the_func(grocery_list, **data)

def get_input(fields):
    user_input = {}
    for field in fields:
        user_input[field] = raw_input(field + ">")
    return user_input  
    
def show_list(grocery_list):
    output = ("Index   "
                "Item  \n")
    
    for index, list in enumerate(grocery_list):
        line = str(index+1).ljust(8)
        for key, length in [('item', 24)]:
            line += str(list[key]).ljust(length)
        output += line + "\n"
    return output
    
def edit_list(grocery_list, which, item):
    if not which.isdigit():
        return ("'" + which +
            "' needs to be the number of the item!")
    which = int(which)
    if which < 1 or which > len(grocery_list):
        return ("'" + str(which) +
            "' needs to the number of the item!")
            
    list = grocery_list[which-1]
    if item != "":
        list['item'] = item
        
    return "Edited item #" + str(which)
    
    
commands = {
    '1' : [create_list, ['item']],
    '2' : [show_list, []],
    '3' : [edit_list, ['which', 'item']],
    '4' : [delete_list, ['which']],
    '5' : [delete_all_list, []],
    'test' : [test, ['abcd']],
    }
    
def program_menu():
    print "Please make a selection: "
    print "1.  New Item"
    print "2.  Show List"
    print "3.  Edit Item"
    print "4.  Delete Item"
    print "5.  Delete All List"
    print "To exit, please type \"quit\""

def main_loop():
    print "Welcome to the Grocery List Program"
    
    program_menu()
    
    user_input = ""
    load_grocery_list()
    while 1:

        user_input = raw_input(">")
        print run_command(user_input)
        if user_input.lower().startswith("quit"):
            print "Exiting......"
            break
        else: 
            time.sleep(3)
            program_menu()
    
    save_grocery_list()
     
if __name__ == '__main__':
    main_loop()