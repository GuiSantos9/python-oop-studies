#Propriedades de Classe
#São as variáveis que pertencem as classes. Eles armazenam dados para cada objeto criado a partir da classe 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessaa1 = Pessoa("Guilherme", 20)

print(pessaa1.nome, pessaa1.idade)

#Acessando propriedades
#Você pode acessar as propriedades de um obejeto usando a notação ponto(.)
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Mercedes", 2003)

print(carro1.modelo, carro1.ano)

#Modificando propriedades
#Você pode modificar o valor das propriedades do objeto
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessaa1 = Pessoa("Guilherme", 20)

print(pessaa1.idade)

pessaa1.idade = 26
print(pessaa1.idade)

#Deletando propriedades
#Você pode deletar as propriedades de um objeto usando a palavra chave 'del'

# del pessoa1.idade

#Propriedades da Classe vs Propriedades do Objeto 
#As propriedades definidas dentro da função __init__() pertencem a cada objeto(propriedades de instância)
#As propriedades definidas fora de métodos pertencem a classes (Propriedades da classe) e são compartilhadas com todos os objetos
class Person:
    especie = "Humano" #Propriedade da classe

    def __init__(self, nome):
        self.nome = nome #Propriedade do objeto

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.nome)
print(p2.nome)
print(p1.especie)
print(p2.especie)


#Modificando as propriedades da classe
#Quando modificamos as propriedades das classes, afetam todos os obejetos
class Nome:
    ultimoNome = ""

    def __init__(self, nome):
        self.nome = nome

p1 = Person("Linus")
p2 = Person("Emil")

Person.ultimoNome = "Refsnes"

print(p1.ultimoNome)
print(p2.ultimoNome)


#Adicione novas propriedades
#Você pode adicionar novas propriedades de um objeto existênte 

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)