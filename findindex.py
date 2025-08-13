def find_in_list(element, lst):
    if element in lst:
        return lst.index(element)
    else:
        return -1
my_list = ['2', '55', '888', '30','45']
element_to_find = '888'
index = find_in_list(element_to_find, my_list)
if index != -1:
    print({element_to_find},"is present at index", {index})
else:
    print({element_to_find},"is not present in the list.")