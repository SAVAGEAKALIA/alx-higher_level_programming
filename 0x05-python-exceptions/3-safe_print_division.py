#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # Handle division by zero
        result = None
    except (TypeError, ValueError):
        # Handle wrong type
        result = None
    finally:
        # Print the result inside the finally block
        print("Inside result: {}".format(result))
        return result
