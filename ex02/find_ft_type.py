#!/usr/bin/env python3.10

def all_thing_is_obj(object: any) -> int:
    if object is not None:
        if type(object) is list:
            print("List :", type(object))
        elif type(object) is set:
            print("Set :", type(object))
        elif type(object) is dict:
            print("Dict :", type(object))
        elif type(object) is str:
            print("Brian is in the kitchen :", type(object))
        elif type(object) is tuple:
            print("Tuple :", type(object))
        else:
            print("Type not found")
    return 42
