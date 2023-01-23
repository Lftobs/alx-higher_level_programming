#!/usr/bin/python3

def safe_print_resultision(a, b):
    try:
        result = a / b
    except (TypeError, ZeroresultisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
