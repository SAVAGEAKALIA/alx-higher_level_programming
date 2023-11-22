#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle division by zero
            division_result = 0
            print("division by 0")
        except (TypeError, ValueError):
            # Handle wrong type
            division_result = 0
            print("wrong type")
        except IndexError:
            # Handle out of range
            division_result = 0
            print("out of range")
        finally:
            result.append(division_result)
    return result
