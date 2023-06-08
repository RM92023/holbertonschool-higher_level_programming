#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                value_1 = my_list_1[i]
                value_2 = my_list_2[i]

                if not isinstance((value_1, (int, float))
                                  or not isinstance(value_2, (int, float))):
                    raise TypeError("wrong type")

                if value_2 == 0:
                    raise ZeroDivisionError("division by 0")

                result = value_1 / value_2
            except IndexError:
                print("out of range")
                result = 0
            except TypeError:
                print("wrong type")
                result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            finally:
                result_list.append(result)

    finally:
        return result_list
