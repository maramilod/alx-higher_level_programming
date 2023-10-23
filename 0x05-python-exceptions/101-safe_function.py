#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        rus = fct(*args)
        return rus
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
