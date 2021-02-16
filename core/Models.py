from os import truncate, umask
from tkinter.constants import CASCADE, TRUE
from typing import cast
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
            vendedor = Vendedor.objects(cpf = cpf_busca)
            print('\tVendedor:')
            for i in vendedor:
                print(f'nome: {i.nome}\ncodigo: {i.cpf}')
        except DoesNotExist:
            print('Not Found')

        try:
            carros = Carro.objects(vendedor = cpf_busca)
            print('\tCarros:')
            for i in carros:
                print(f'modelo: {i.modelo}\nplaca: {i.placa}')
        except DoesNotExist:
            print('Não possui carros')

    def atualizarNome(self, nome_editado, cpf_busca):
        try:
            vendedor = Vendedor.objects(cpf = cpf_busca).get()
            vendedor.update(
                nome = nome_editado
            )
            vendedor.reload()
            print('Editado')
        except DoesNotExist:
            print("User not found")

    def deletar(self, cpf_busca):
        try:
            Vendedor.objects(cpf = cpf_busca).delete()
            print('deletado')
        except DoesNotExist:
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
            comprador = Comprador.objects(cpf = cpf_busca)
            print('\tComprador:')
            for i in comprador:
                print(f'nome : {i.nome}\ncpf : {i.cpf}')
        except DoesNotExist:
            print('Not found')

        try:
            carros = Carro.objects(comprador = cpf_busca)
            print('\tCarros:')
            for i in carros:
                print(f'modelo: {i.modelo}\nplaca: {i.placa}')
        except DoesNotExist:
            print('Não possui carros')

    def atualizarNome(self, nome_editado, cpf_busca):
        try:
            comprador = Comprador.objects(cpf = cpf_busca).get()
            comprador.update(
                nome = nome_editado
            )
            comprador.reload()
            print('Editado')
        except DoesNotExist:
            print("User not found")

    def deletar(self, cpf_busca):
        try:
            Comprador.objects(cpf = cpf_busca).delete()
            print('deletado')
        except DoesNotExist:
            print("User not found")

    meta = {
        'indexes' : ['cpf']
    }


class Carro(DynamicDocument):
    modelo = StringField(unique=True, required=True)
    valor = StringField(required=True)
    comprador = ListField(ReferenceField(Comprador, CASCADE=True))
    vendedor = ListField(ReferenceField(Vendedor, CASCADE=True))
    placa = StringField(max_length=7, required=True, unique=True)

    def criar(self, modelo, valor, placa, comprador, vendedor):
        self.modelo = modelo
        self.valor = valor
        self.placa = placa
        self.comprador = comprador
        self.vendedor = vendedor
        self.save()

    def ler(self, placa_busca):
        try
            carro = Carro.objects(placa = placa_busca)
            for i in carro:
                print(f'nome : {i.modelo}\nvalor : {i.valor}\ndono: {i.comprador}. \n Vendido por {i.vendedor}')
        except:
            print('Not found')

    def atualizarModelo(self, modelo_editado, placa_busca):
        try:
            carro = Carro.objects(placa = placa_busca).get()
            carro.update(
                modelo = modelo_editado
            )
            carro.reload()
            print('Editado')
        except DoesNotExist:
            print("User not found")

    def atualizarValor(self, valor_editado, placa_busca):
        try:
            carro = Carro.objects(placa = placa_busca).get()
            carro.update(
                valor = valor_editado
            )
            carro.reload()
            print('Editado')
        except DoesNotExist:
            print("User not found")

    def deletar(self, placa_busca):
        try:
            Carro.objects(placa = placa_busca).delete()
            print('deletado')
        except DoesNotExist:
            print("User not found")

    meta = {
        'indexes' : ['placa']


vendedor = Vendedor()
vendedor.criar('jacquan', '12034568791') 
# vendedor.atualizarNome('erick jaquin', '12034568791')
# vendedor.ler('12034568791')
# vendedor.deletar('12034568791')

comprador = Comprador()
comprador.criar('william', '12034568790') 
# comprador.atualizarNome('willis', '12034568790')
# comprador.ler('12034568790')
# comprador.deletar('12034568790')

carro = Carro()
carro.criar('BMW', '5000,00', 'ABC1234', comprador.cpf, vendedor.cpf)
# carro.atualizarModelo('AUDI', 'ABC1234')
# carro.atualizarModelo('7000,00', 'ABC1234')
# carro.ler('ABC1234')
# carro.deletar('ABC1234')
