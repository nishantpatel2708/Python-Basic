class myclass():
    x = 10

obj = myclass
print(obj.x)


class second():

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def print_name(self):
        print("Your name is",self.name)

    def marks_print(self):
        print("marks is:",self.marks)

new = second("Anand", 77)
# new.print_name()
# new.marks_print()

# new = second("Nishant", 99)
# new.print_name()
# new.marks_print()


class child(second):
    pass
    # def print_name(self):
    #     print("child class function")
new = child("Nishant", 99)
new.marks_print()


class second_child(child):
    pass

new = second_child("Anand", 100)
new.marks_print()
