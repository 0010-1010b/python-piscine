def all_thing_is_obj(object: any) -> int:
    
    ret_type = type(object)

    if ret_type == list:
        print("List :", ret_type)
    elif ret_type == tuple:
        print("Tuple :", ret_type)
    elif ret_type == set:
        print("Set :", ret_type)
    elif ret_type == dict:
        print("Dict :", ret_type)
    elif ret_type == str:
        print(f"{object} is in the kitchen :", ret_type)
    else:
        print("Type not found")

    return 42