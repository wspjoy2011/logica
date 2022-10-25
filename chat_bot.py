class Person:
    def __init__(self, full_name, id_card, age):
        self.__full_name = full_name
        self.__id_card = id_card
        self.__age = age

    def get_name(self):
        return self.__full_name

    def set_name(self, name):
        self.__full_name = name


john_doe = Person('John Doe', 'id-535353', 21)
print(john_doe.get_name())
john_doe.set_name('Bob Newton')
print(john_doe.get_name())

# pamela_anderson = Person('Pamela Anderson', 'id-90123909', 27)
# print(pamela_anderson.get_name())

