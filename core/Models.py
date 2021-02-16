from mongoengine import *

connect('mongobd_concessionaria')


class Vendedor(Document):
    nome = StringField(max_length=50, required=True)
    cpf = StringField(max_length=11, required=True, unique=True)

    def criar(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.save()

    def ler(self, cpf_busca):
        try:
            vendedor = Vendedor.objects.get(cpf = cpf_busca)
            print('\tVendedor:')
            print(f'nome: {vendedor.nome}\ncodigo: {vendedor.cpf}')
        except (DoesNotExist, UnboundLocalError) as e:
            print('Not Found')

        try:
            carros = Carro.objects(vendedor = vendedor.id)
            print('\tCarros:')
            for i in carros:
                print(f'modelo: {i.modelo}\nplaca: {i.placa}')
        except (DoesNotExist, UnboundLocalError) as e:
            print('Não possui carros')

    def atualizarNome(self, nome_editado, cpf_busca):
        try:
            vendedor = Vendedor.objects(cpf = cpf_busca).get()
            vendedor.update(
                nome = nome_editado
            )
            vendedor.reload()
            print('Editado')
        except (DoesNotExist, UnboundLocalError) as e:
            print("User not found")

    def deletar(self, cpf_busca):
        try:
            Vendedor.objects(cpf = cpf_busca).delete()
            print('deletado')
        except (DoesNotExist, UnboundLocalError) as e:
            print("User not found")

    meta = {
        'indexes' : ['cpf']
    }


class Comprador(Document):
    nome = StringField(max_length=50, required=True)
    cpf = StringField(max_length=11, required=True, unique=True)

    def criar(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.save()

    def ler(self, cpf_busca):
        try:
            comprador = Comprador.objects.get(cpf = cpf_busca)
            print('\tComprador:')
            print(f'nome : {comprador.nome}\ncpf : {comprador.cpf}')
        except (DoesNotExist, UnboundLocalError) as e:
            print('Not found')

        try:
            carros = Carro.objects(comprador = comprador.id)
            print('\tCarros:')
            for i in carros:
                print(f'modelo: {i.modelo}\nplaca: {i.placa}')
        except (DoesNotExist, UnboundLocalError) as e:
            print('Não possui carros')

    def atualizarNome(self, nome_editado, cpf_busca):
        try:
            comprador = Comprador.objects(cpf = cpf_busca).get()
            comprador.update(
                nome = nome_editado
            )
            comprador.reload()
            print('Editado')
        except (DoesNotExist, UnboundLocalError) as e:
            print("User not found")

    def deletar(self, cpf_busca):
        try:
            Comprador.objects(cpf = cpf_busca).delete()
            print('deletado')
        except (DoesNotExist, UnboundLocalError) as e:
            print("User not found")

    meta = {
        'indexes' : ['cpf']
    }


class Carro(DynamicDocument):
    modelo = StringField(unique=True, required=True)
    valor = StringField(required=True)
    comprador = ReferenceField(Comprador, reverse_delete_rule=CASCADE)
    vendedor = ReferenceField(Vendedor, reverse_delete_rule=CASCADE)
    placa = StringField(max_length=7, required=True, unique=True)

    def criar(self, modelo, valor, placa, comprador, vendedor):
        self.modelo = modelo
        self.valor = valor
        self.placa = placa
        self.comprador = comprador
        self.vendedor = vendedor
        self.save()

    def ler(self, placa_busca):
        try:
            carro = Carro.objects(placa = placa_busca)
            for i in carro:
                print(f'nome : {i.modelo}\nvalor : {i.valor}\ndono: {i.comprador.nome}. \nVendido por {i.vendedor.nome}')
        except (DoesNotExist, UnboundLocalError) as e:
            print('Not found')

    def atualizarModelo(self, modelo_editado, placa_busca):
        try:
            carro = Carro.objects(placa = placa_busca).get()
            carro.update(
                modelo = modelo_editado
            )
            carro.reload()
            print('Editado')
        except (DoesNotExist, UnboundLocalError) as e:
            print("User not found")

    def atualizarValor(self, valor_editado, placa_busca):
        try:
            carro = Carro.objects(placa = placa_busca).get()
            carro.update(
                valor = valor_editado
            )
            carro.reload()
            print('Editado')
        except (DoesNotExist, UnboundLocalError) as e:
            print("User not found")

    def deletar(self, placa_busca):
        try:
            Carro.objects(placa = placa_busca).delete()
            print('deletado')
        except (DoesNotExist, UnboundLocalError) as e:
            print("User not found")

    meta = {
        'indexes' : ['placa']
    }


