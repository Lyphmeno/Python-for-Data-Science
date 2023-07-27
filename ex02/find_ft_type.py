#!/usr/bin/env python3.10

def all_thing_is_obj(object: any) -> int:
    if object is not None:
        if type(object) is list:
            print ("List :", type(object))
        elif type(object) is set:
            print ("Set :", type(object))
        elif type(object) is dict:
            print ("Dict :", type(object))
        elif type(object) is str:
            print ("Brian is in the kitchen :", type(object))
        elif type(object) is tuple:
            print ("Tuple :", type(object))
        else:
            print ("Type not found")
    return 42

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
print(all_thing_is_obj(10))

all_thing_is_obj(None)