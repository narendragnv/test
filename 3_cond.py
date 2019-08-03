a = "Pradeep works in Sony"

if "Sony" in a:
    print("Yes, he works")
else:
    print("No, he doesn't")

a = 29
if a > 30:
    print("a is > 30")
elif a > 20:
    print("a is > 20")
else:
    print("a is < 20")

if a > 20 and a < 30:
    print("a is between 20 and 30")

print("10 to 0")
a = 10
while(a >= 0):
    print(a)
    a = a - 1

print("\n\n0 to 9")
a = 0
while(a < 10):
    print(a)
    # a = a + 1
    a += 1

print("\n\n0 to 9 using for")
for a in range(0, 10):
    print(a)

print("\n\nfor in list")
a = [2, 3, 4, 5, 6]
for item in a:
    print(item)

dict1 = {"a": 1, "b": 2}
for key in dict1.keys():
    print(f"value for key {key} is {dict1[key]}")


