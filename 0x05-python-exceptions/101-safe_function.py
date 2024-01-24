#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        num = fct(*args)
        return num
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
