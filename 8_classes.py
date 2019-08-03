class Sample:
    def __init__(self):
        print(f"constructor magic method")
        self.b = 0
    def func1(self):
        print("First class function")
        a = 10  # local
        self.b = 20  # class variable
    def func2(self, name):
        print(f"hello {name}")
        # print(f"value of a {a}")  # error!!
        print(f"value of b {self.b}")

s = Sample()
# s.func1()
s.func2("pradeep")
