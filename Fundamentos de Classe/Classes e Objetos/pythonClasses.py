#Classes e objetos
#Python é uma linguagem orientada a objetos, quase tudo em Python é um objeto
#Com suas propriedades e métodos

#Uma classe é como um construtor de objetos, ou um "planta" para criar objetos
class MinhaClasse:
    x = 5

#Agora nós podemos usar uma classe chamada MinhaClasse para crir objetos
p1 = MinhaClasse()
print(p1.x)

#Podemos deletar objetos usando a palavra chave 'del'

del p1

#Podemos criar multiplos objetos de uma única classe
p1 = MinhaClasse() 
p2 = MinhaClasse() 
p3 = MinhaClasse() 

print(p1.x)
print(p2.x)
print(p3.x)

#As definições de uma classe não podem ser vazias, mas se por algum motivo
#Temos uma definição de classe sem conteúdo coloque o pass para evitar gerar um erro

class Pessoa:
    pass