from model.model import PessoaFisica, Cliente

class PessoaFisicaDal(PessoaFisica):

    @classmethod
    def cadastrar_cliente(cls, pessoa: Cliente)->None:
        with open('arquivos\clientes.txt', 'a') as arq:
            arq.write(  pessoa.__id_pf + ' ' +
                            pessoa.__nome + ' ' +
                            pessoa.__endereco + ' ' +
                            pessoa.__idade + ' ' +
                            pessoa.__cpf + ' ' +
                            pessoa.__email + ' ' +
                            pessoa.__tel_cel + ' ' +
                            pessoa.__profissao + ' ' +
                            pessoa.__renda + ' ' +
                            pessoa.__estado_civil
            )

    
    @property
    def id_pf(self)->int:
        return self.__id_pf

    @property
    def nome(self)->str:
        return self.__nome

    @property
    def endereco(self)->str:
        return self.__endereco

    @property
    def idade(self)->int:
        return self.__idade

    @property
    def cpf(self)->str:
        return self.__cpf

    @property
    def email(self)->str:
        return self.__email

    @property
    def tel_cel(self)->str:
        return self.__tel_cel

    @id_pf.setter
    def id_pf(self, id_pf: int)->None:
        self.__id_pf = id_pf

    @nome.setter
    def nome(self, nome: str)->None:
        self.__nome = nome

    @endereco.setter
    def endereco(self, endereco: str)->None:
        self.__endereco = endereco

    @idade.setter
    def idade(self, idade: int)->None:
        self.__idade = idade

    @cpf.setter
    def cpf(self, cpf: str)->None:
        self.__cpf = cpf

    @email.setter
    def email(self, email: str)->None:
        self.__email = email

    @tel_cel.setter
    def tel_cel(self, tel_cel: str)->None:
        self.__tel_cel = tel_cel



