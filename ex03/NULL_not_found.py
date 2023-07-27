#!/usr/bin/env python3.10

def NULL_not_found(object : any) -> int:
    if object is None:
        if type(object) is list:
            print ("List :", object, type(object))
        elif type(object) is set:
            print ("Set :", object, type(object))
        elif type(object) is dict:
            print ("Dict :", object, type(object))
        elif type(object) is str:
            print ("Brian is in the kitchen :", object, type(object))
        elif type(object) is tuple:
            print ("Tuple :", object, type(object))
    return 0

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))