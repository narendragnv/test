def get_number():
    return 1
    return 2
    return 3

def get_number_g1():
    yield 1
    yield 2
    yield 3

def get_number_g2():
    for i in range(1, 4):
        yield i

print("function")
print(get_number())
print(get_number())
print(get_number())
print(get_number())

print("\n\nGenerator")
g = get_number_g1()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # EXCEPTION: StopIteration

print("\n\nGenerator2")
g = get_number_g2()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # EXCEPTION: StopIteration

for i in get_number_g2():
    print(i)
