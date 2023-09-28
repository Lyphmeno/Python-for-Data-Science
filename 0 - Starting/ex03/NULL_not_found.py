#!/usr/bin/env python3.10


def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing :", object, type(object))
    elif object is False:
        print("Fake :", object, type(object))
    elif object == "":
        print("Empty :", object, type(object))
    elif object == 0:
        print("Zero :", object, type(object))
    elif isinstance(object, float):
        print("Cheese :", object, type(object))
    else:
        print("Type not Found")
        return 1
    return 0
