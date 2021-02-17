from mongoengine import *


connect('locadora')


def lerLocadores():
    print('\nTODOS OS LOCADORES\n******************************')
    locadores = Locador.objects()
    if len(locadores) != 0:
        for i in locadores:
            print(f'Locador de cpf: {i.cpf}\nNome: {i.nome}\n')
    else:
        print('\nNão há locadores no banco de dados.')


def lerClientes():
    print('\nTODOS OS CLIENTES\n******************************')
    clientes = Cliente.objects()
    if len(clientes) != 0:
        for i in clientes:
            print(f'Cliente de cpf: {i.cpf}\nNome: {i.nome}\n')
    else:
        print('\nNão há clientes no banco de dados.')


def lerCarros():
    print('\nTODOS OS CARROS\n******************************')
    carros = Carro.objects()
    if len(carros) != 0:
        for i in carros:
            try:
                print(f'Carro de placa: {i.placa}\nModelo: {i.modelo}\nValor: R${i.valor} por dia\n'
                      f'Cliente locado: {i.cliente.nome}.\nLocador: {i.locador.nome}\n')
            except AttributeError:
                print(f'Carro de placa: {i.placa}\nModelo: {i.modelo}\nValor: R${i.valor} por dia\n'
                      f'Locador: {i.locador.nome}\n')
    else:
        print('\nNão há carros no bando de dados.')


def lerCarrosDisponiveis():
    print('\nCARROS DISPONÍVEIS\n******************************')
    carros = Carro.objects(disponivel=True)
    if len(carros) != 0:
        for i in carros:
            print(f'Modelo: {i.modelo}\nValor: R${i.valor} por dia\nLocador: {i.locador.nome}\n')
    else:
        print('\nNão há carros disponíveis para locação.')


def lerCarrosLocados():
    print('\nCARROS NÃO DISPONÍVEIS\n******************************')
    carros = Carro.objects(disponivel=False)
    if len(carros) != 0:
        for i in carros:
            print(f'\nCarro de placa: {i.placa}\nModelo: {i.modelo}\nValor: R${i.valor} por dia\n'
                  f'Cliente locado: {i.cliente.nome}.\nLocador: {i.locador.nome}\n')
    else:
        print('\nNão há carros locados atualmente.')


class Locador(Document):
    nome = StringField(max_length=50, required=True)
    cpf = StringField(max_length=11, required=True, unique=True)

    def criar(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.save()
        print(f'\nLocador \'{self.nome}\' inserido no banco de dados.')

    def ler(self):
        try:
            locador = Locador.objects(cpf=self.cpf).get()
            print(f'\n******************************\nLocador de cpf: {self.cpf}')
            print(f'Nome: {locador.nome}')
            carros = Carro.objects(locador=locador.id)
            if len(carros) != 0:
                print('Carro(s) para locar:')
                for i in carros:
                    print(f'Modelo: {i.modelo}\nAno: {i.ano}\nPlaca: {i.placa}\nValor: R${i.valor} por dia\n')
            else:
                print(f'Não possui carros para locar.')
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nLocador não encontrado no banco de dados.')

    def atualizarNome(self, nome_editado):
        try:
            locador = Locador.objects(cpf=self.cpf).get()
            locador.update(
                nome=nome_editado
            )
            locador.reload()
            print(f'\nNome do locador \'{self.nome}\' editado para \'{nome_editado}\'.')
            self.nome = nome_editado
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nLocador não encontrado no banco de dados.')

    def deletar(self):
        try:
            locador = Locador.objects(cpf=self.cpf)
            locador.delete()
            print('\nLocador removido do banco de dados, juntamente com os carros associados.')
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nLocador não encontrado no banco de dados.')

    meta = {
        'indexes': ['cpf']
    }


class Cliente(Document):
    nome = StringField(max_length=50, required=True)
    cpf = StringField(max_length=11, required=True, unique=True)

    def criar(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.save()
        print(f'\nCliente \'{self.nome}\' inserido no banco de dados.')

    def ler(self):
        try:
            cliente = Cliente.objects(cpf=self.cpf).get()
            print(f'\n******************************\nCliente de cpf: {self.cpf}')
            print(f'Nome: {cliente.nome}')
            carros = Carro.objects(cliente=cliente.id)
            if len(carros) != 0:
                print('Carro(s) Locado(s):')
                for i in carros:
                    print(f'Modelo: {i.modelo}\nPlaca: {i.placa}')
                    print()
            else:
                print('Não possui carros locados.')
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nCliente não encontrado no banco de dados.')

    def atualizarNome(self, nome_editado):
        try:
            cliente = Cliente.objects(cpf=self.cpf).get()
            cliente.update(
                nome=nome_editado
            )
            cliente.reload()
            print(f'\nNome do cliente \'{self.nome}\' editado para \'{nome_editado}\'.')
            self.nome = nome_editado
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nCliente não encontrado no banco de dados.')

    def deletar(self):
        try:
            cliente = Cliente.objects(cpf=self.cpf)
            cliente.delete()
            print('\nCliente removido do banco de dados.')
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nCliente não encontrado no banco de dados.')

    meta = {
        'indexes': ['cpf']
    }


class Carro(DynamicDocument):
    modelo = StringField(unique=True, required=True)
    ano = StringField(required=True)
    valor = StringField(required=True)
    cliente = ReferenceField(Cliente, reverse_delete_rule=CASCADE)
    locador = ReferenceField(Locador, reverse_delete_rule=CASCADE)
    placa = StringField(max_length=7, required=True, unique=True)
    disponivel = BooleanField(required=True)

    def criar(self, modelo, ano, valor, placa, locador):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.placa = placa
        self.locador = locador
        self.disponivel = True
        self.save()

    def ler(self):
        try:
            carro = Carro.objects(placa=self.placa).get()
            print(f'\nCarro de placa: {self.placa}')
            print(f'Modelo: {carro.modelo}\nValor: R${carro.valor} por dia\nCliente locado: {carro.cliente.nome}.'
                  f'\nLocador: {carro.locador.nome}')
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nCarro não encontrado no nosso banco de dados.')
        except AttributeError:
            print(f'Modelo: {self.modelo}\nValor: R${self.valor} por dia\nLocador: {self.locador.nome}')

    def atualizarValor(self, valor_editado):
        try:
            carro = Carro.objects(placa=self.placa).get()
            self.valor = valor_editado
            carro.update(
                valor=valor_editado
            )
            carro.reload()
            print(f'\nValor de locação do carro de placa \'{self.placa}\' atualizado.')
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nCarro não encontrado no nosso banco de dados.')

    def deletar(self):
        try:
            carro = Carro.objects(placa=self.placa).get()
            carro.delete()
            print('\nCarro removido do nosso banco de dados.')
        except (DoesNotExist, UnboundLocalError) as e:
            print('\nCarro não encontrado no nosso banco de dados.')

    def locarCarro(self, cliente):
        if self.disponivel:
            try:
                carro = Carro.objects(placa=self.placa).get()
                carro.update(
                    cliente=cliente,
                    disponivel=False
                )
                carro.reload()
                print(f'\n\'{cliente.nome}\' locou o carro de placa \'{self.placa}\'.')
            except (DoesNotExist, UnboundLocalError) as e:
                print(f'\nCarro não encontrado no nosso banco de dados.')
        else:
            print('Carro não está disponível para locação')

    def deslocarCarro(self, cliente):
        if not self.disponivel:
            try:
                carro = Carro.objects(placa=self.placa).get()
                carro.update(
                    disponivel=True
                )
                carro.cliente.delete()
                carro.reload()
                print(f'\n\'{cliente.nome}\' deslocou o carro de placa \'{self.placa}\'.')
            except (DoesNotExist, UnboundLocalError) as e:
                print(f'\nCarro não encontrado no nosso banco de dados.')
        else:
            print('Carro não está locado no momento')

    meta = {
        'indexes': ['placa']
    }
