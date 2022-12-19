#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(0, list_length):
        val = 0
        try:
            val = my_list_1[i] / my_list_2[i]
        except TypeError:
            print('Wrong Type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            result.append(val)

    return result
