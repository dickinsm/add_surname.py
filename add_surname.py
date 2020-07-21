# Author: Makaliah Dickinson
# Date: 7/21/2020
# Description: Write a function that returns a list of first names that begin with "K" and adds "Kardashian" as the
#              surname.
def add_surname(firs_names_list):
    full_list = [name + ' Kardashian' for name in first_names_list if name[0] == 'K']

    return full_list


first_names_list = ["Kiki", "Krystal", "Pavel", "Annie", "Koala"]

print(add_surname(first_names_list))
