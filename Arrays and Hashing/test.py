my_dict = {"apple": 1, "banana": 2, "cherry": 3}
reverseddict = dict(reversed(list(my_dict.items())))
removed_item = reverseddict.popitem()
print(reverseddict)
print(my_dict)  # Output: {'apple': 1, 'banana': 2}
print(removed_item) # Output: ('cherry', 3)