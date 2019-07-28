# list == array
# tuple
# dict

## LIST
a = ["somestring", 2, 4.0]
print(a)
b = [2.3, a]
b = [2.3, ["somestring", 2, 4.0]]  # same as above line
print(b)

print(2 in a)
print(3 not in a)
print("somestring" in a)
print("string" in a)

a = ["somestring", 2, 4.0]
print(a)
print(a[1])
a[1] = 32  # list is mutable
print(a)
print(a[1])

a.append(40)
print(a)

## TUPLE is immutable
a = ("somestring", 2.0, 564)
a = tuple(("somestring", 2.0, 564))
print(a)
print(a[0])

# a[0] = 123  # ERROR! since tuples are immutable

## DICT
# a = {"key": "value"}
a = {"a": 1, "b": 2}
print(a)
a = {1: "a", 2: "b"}
print(a)
a = {"a": [1, 2, 3], "b": ("12312", 123)}
print(a)

dict1 = {"a": 1, "b": 2}
print(dict1["b"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1 = {"a": [1, 2, 3], "b": ("12312", 123)}
print(dict1["a"][1])

dict1 = {"a": 1, "b": 2}
dict1["a"] = 100
print(dict1)
dict1 = {"a": 1, "b": 2, "a": 200}
print(dict1)
