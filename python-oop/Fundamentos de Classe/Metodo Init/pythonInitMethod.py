#Todas as classes possuem um método integrado chamado __init__(), que sempre é executada quando a 
#classe é inicializada

#O método __init__() é usado para atribuir valores às propriedades de um objeto ou para realizar 
# operações necessárias durante a criação do objeto.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Guilherme", 21)
print(p1.nome)
print(p1.idade)

#O método init pode ser confundido com um construtor, porém tecnicamente ele é um construtor
#diferença __new__ e __init__
#__new__ cria um objeto na memória e retorna a instância
#__init__ configura um objeto já criado (define atributos etc.)

#Porque usar __init__
#Sem o método __init__(), você precisaria definir as propriedades manualmente para cada objeto:
#O uso de __init__() facilita a criação de objetos com valores iniciais:

#Valores padrão em __init__()
#Você também pode definir valores padrão para parâmetros no método __init__():
class MaiorDeidade:
    def __init__(self, nome, idade = 18):
        self.nome = nome
        self.idade = idade

pessoa1 = MaiorDeidade("Guilherme")
pessoa2 = MaiorDeidade("Thiago")

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)

#O método init pode ter quantos parâmentros forem necessarios 
class Identidade:
    def __init__(self, nome, idade, cidadania, email):
        self.nome = nome
        self.idade = idade
        self.cidadania = cidadania
        self.email = email

pessoa1 = Identidade("Guilherme", 21, "brasileira", "guilherme@gmail.com")
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.cidadania)
print(pessoa1.email)