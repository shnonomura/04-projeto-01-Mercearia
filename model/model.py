from ..my_bible.my_functions import objetivo, secao, descricao
import os, platform
win, other = 'cls', 'clear'
comando = lambda win, other: win if platform.system() == 'Windows' else other
os.system(comando(win, other))

class PessoaFisica:
    def __init__(self, id_pf: int, nome: str, endereco: str, idade:int, cpf: str, email:str, tel_cel:str) -> None:
        self.id_pf = id_pf
        self.nome = nome
        self.endereco = endereco
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.tel_cel = tel_cel

class Cliente(PessoaFisica):
    def __init__(self, id_pf: int, nome: str, endereco: str, idade:int, cpf: str, email:str, tel_cel:str, profissao: str, renda: float, estado_civil: str) -> None:
        PessoaFisica.__init__(self, id_pf, nome, endereco, idade, cpf, email, tel_cel)
        self.profissao = profissao
        self.renda = renda
        self.estado_civil = estado_civil

class Funcionario(PessoaFisica):
    def __init__(self, id_pf: int, nome: str, endereco: str, idade:int, cpf: str, email:str, tel_cel:str, cargo:str, salario: float) -> None:
        PessoaFisica.__init__(self, nome, endereco, idade, cpf, email, tel_cel)
        self.cargo = cargo
        self.salario = salario

class PessoaJuridica:
    def __init__(self, id_ramo: int, ramo: str) -> None:
        self.id_ramo = id_ramo
        self.ramo = ramo

class Fornecedor(PessoaJuridica):
    def __init__(self, id_ramo: int, ramo: str, id_forn: int, razao_social:str, cnpj:str, email:str, tel_cel: str ) -> None:
        PessoaJuridica.__init__( self, id_ramo, ramo)
        self.id_forn = id_forn
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.email = email
        self.tel_cel = tel_cel

class Categoria:
    def __init__(self, id_cat: int, categoria: str) -> None:
        self.id_cat = id_cat
        self.categoria = categoria

class Produto(Categoria):
    def __init__(self, id_cat: int, categoria: str, id_prd: int, produto: str, unidade:str, preco: float) -> None:
        Categoria.__init__(self,  id_cat, categoria)
        self.id_prd = id_prd
        self.produto = produto
        self.unidade = unidade
        self.preco =  preco

objetivo('MVC - model')
descricao('Criar as classes do projeto Mercearia')
secao('instanciar um objeto PessoaFisica')
pf1 = PessoaFisica(1,  'sergio', 'rua arthur bettes', 26, '132346656', 'shnonomura@gmail.com', '41992578233')
print(f'{pf1=}')
print(f'{pf1.nome=}')
print(f'{pf1.endereco=}')
print(f'{pf1.idade=}')
print(f'{pf1.cpf=}')
print(f'{pf1.email=}')
print(f'{pf1.tel_cel=}')

secao('instanciar um objeto Cliente')
cli =  Cliente( 1,  'sergio', 'rua arthur bettes', 26, '132346656', 'shnonomura@gmail.com', '41992578233', 'engenheiro', 10000, 'casado')
print(f'{cli.id_pf=}')
print(f'{cli.nome=}')
print(f'{cli.endereco=}')
print(f'{cli.idade=}')
print(f'{cli.cpf=}')
print(f'{cli.email=}')
print(f'{cli.tel_cel=}')
print(f'{cli.profissao=}')
print(f'{cli.renda=}')
print(f'{cli.estado_civil=}')


