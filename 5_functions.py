def show_hello():
    print(f"Hello!")

def say_hello(name):  # parameter
    print(f"Hello {name}")

def say_hello(name2):  # parameter
    print(f"Hello2 {name2}")

def say_hello2(name="world"):  # default parameter
    print(f"Hello {name}")

show_hello()
say_hello("pradeep")
say_hello2()
say_hello2("janu")
