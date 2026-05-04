#O parâmetro `self`
#O parâmetro `self` é uma referência à instância atual da classe.

#Ele é usado para acessar propriedades e métodos que pertencem à classe.
class Person:  
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

#Por que usar `self`?
#Sem `self`, o Python não saberia quais propriedades do objeto você deseja acessar.

#O parâmetro `self` não precisa se chamar "self".
#Ele não precisa se chamar "self", você pode dar o nome que quiser,
#  mas precisa ser o primeiro parâmetro de qualquer método da classe.
class Person:
    def __init__(meuobjeto, name, age):
        meuobjeto.name = name
        meuobjeto.age = age

    def greet(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

#Acessando propriedades com self
#Você pode acessar qualquer propriedade da classe usando self:
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

#Chamando métodos com self
#Você também pode chamar outros métodos dentro da classe usando self:
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()