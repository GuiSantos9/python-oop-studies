#A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.
#Classe pai é a classe da qual a herança é feita, também chamada de classe base.
#Classe filha é a classe que herda de outra classe, também chamada de classe derivada.

#Criando uma Classe Pai
#qualquer classe pode ser uma classe pai, então, a sintaxe é a mesma na criação de qualquer classe
class Pessoa:
    def __init__(self, pNome, uNome):
        self.pNome = pNome
        self.uNome = uNome

    def mostrarNome(self):
        print(self.pNome, self.uNome)

pessoa1 = Pessoa("Guilherme", "Augusto")
pessoa1.mostrarNome()

#Criando uma classe filha
#Para criarmos uma classe que herda as funcionalidades de outra classe, mande a classe pai como parâmetro enquanto
#cria a classe filho

#Adicionar a função __init__()
#Até agora, criamos uma classe filha que herda as propriedades e os métodos de sua classe pai.
#Queremos adicionar a função __init__() à classe filha (em vez da palavra-chave pass).
#Ao adicionar a função __init__(), a classe filha não herdará mais a função __init__() da classe pai.

#Para manter a herança da função __init__() da classe pai, adicione uma chamada à função __init__() da classe pai:
#Agora que adicionamos com sucesso a função __init__() e mantivemos a herança da classe pai, estamos prontos para
# adicionar funcionalidades à função __init__().

#def __init__(self, pNome, uNome):
#    Pessoa.__init__(self, pNome, uNome)

#Python também possui uma função super() que fará com que a classe filha herde todos os métodos e propriedades
# da classe pai:
#Ao usar a função super(), você não precisa usar o nome do elemento pai, pois ele herdará automaticamente
# os métodos e propriedades do elemento pai.

#No exemplo abaixo, o ano de 2019 deve ser uma variável e passada para a classe `Estudante`
# ao criar objetos `Estudante`. Para isso, adicione outro parâmetro na função `__init__()`:

class Estudante(Pessoa): #Cria um estudante que possui as mesmas propriedades e métodos da classe Pessoa
    def __init__(self, pNome, uNome, ano):
        super().__init__(pNome, uNome)
        self.anoDegraduacao = ano

    def __str__(self):
        return f"Bem Vindo {self.pNome} {self.uNome}! seu ano de graduação é em {self.anoDegraduacao}"

estudante1 = Estudante("Guilherme", "Augusto", 2027)
print(estudante1)
