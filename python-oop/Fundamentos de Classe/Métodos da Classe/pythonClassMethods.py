#Métodos são funções que pertencem a uma classe. Eles definem o comportamento dos objetos criados a partir da classe.
class Calculdora:
    def soma(self, a, b):
        return a + b

    def multiplicacao(self, a, b):
        return a * b

calc = Calculdora()

print(calc.soma(23,43))
print(calc.multiplicacao(56,94))

#Métodos acessando propriedades
#Métodos podem acessar e modificar propriedades usando o 'self'
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pegar_informacao(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Guilherme", 21)
print(p1.pegar_informacao())

#Métodos modificando propriedades
#Métodos podem modificar as propriedades de um objeto 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def comemorar_aniversario(self):
        self.idade += 1
        print(f"Feliz Aniversário {self.nome}!, hoje você está fazendo {self.idade} anos de idade!")

pessoa1 = Pessoa("Guilherme", 20)
pessoa1.comemorar_aniversario()
pessoa1.comemorar_aniversario()
pessoa1.comemorar_aniversario()
pessoa1.comemorar_aniversario()

#O método __str__()
#O método __str__() é um método especial que controla o que é retornado quando um objeto é printado

#Sem o método __str__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1)

#Com o método __str__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)

#Uma classe pode ter vários métodos que trabalham em conjunto
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

#Você pode excluir métodos de uma classe usando a palavra-chave del
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet() # Isso irá gerar um erro