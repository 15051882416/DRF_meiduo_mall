class Demo:

    def __init__(self):
        self.password = "12345678"
        print(id(self.password))


demo = Demo()
demo.password = "123456789"
print(id(demo.password))
# print(demo.password)
# print(demo.password1)
