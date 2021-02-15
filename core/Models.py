from os import truncate, umask
from tkinter.constants import CASCADE, TRUE
from typing import cast
from mongoengine import *

connect('mongobd_concessionaria')

class Vendedor(Document):
    nome = StringField(max_length=50,required=True)
    codigo_vendedor = StringField(max_length=10,required=True,unique=True)

    def criar(self,nome,codigo_vendedor):
        self.nome = nome
        self.codigo_vendedor = codigo_vendedor
        self.save()

    def ler(self):
        vendedor = Vendedor.objects(codigo_vendedor = '1203456879')
        for i in vendedor:
            print(f'nome : {i.nome}\ncodigo : {i.codigo_vendedor}')

    def atualizar(self,nome_editado):
        try:
            vendedor = Vendedor.objects(codigo_vendedor = '1203456879').get()
            vendedor.update(
                nome = nome_editado
            )
            vendedor.reload()
            print('Editado')
        except DoesNotExist:
            print("User not found")
        

    def deletar(self):
        try:
            Vendedor.objects(codigo_vendedor = '1203456879').delete()
            print('deletaoo')
        except DoesNotExist:
            print("User not found")

    meta = {
        'indexes' : ['codigo_vendedor']
    }

    
class Comprador(Document):
    nome = StringField(max_length=50,required=True)
    cpf = StringField(max_length=11,required=True,unique=True)

    def criar(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        self.save()

    def ler(self):
        comprador = Comprador.objects(cpf = '12034568791')
        for i in comprador:
            print(f'nome : {i.nome}\ncpf : {i.cpf}')

    def atualizar(self,nome_editado):
        try:
            comprador = Comprador.objects(cpf = '12034568791').get()
            comprador.update(
                nome = nome_editado
            )
            comprador.reload()
            print('Editado')
        except DoesNotExist:
            print("User not found")
        

    def deletar(self):
        try:
            Comprador.objects(cpf = '12034568791').delete()
            print('deletaoo')
        except DoesNotExist:
            print("User not found")

    meta = {
        'indexes' : ['cpf']
    }
    
class Carro(DynamicDocument):
    modelo = StringField(unique=True,required=True)
    valor = StringField(required=True)
    dono = ReferenceField(Comprador,CASCADE=True)
    vendedor = ReferenceField(Vendedor, CASCADE=True)

    def criar(self,modelo,valor,dono,vendedor):
        self.modelo = modelo
        self.valor = valor
        self.dono = dono
        self.vendedor = vendedor
        self.save()

    def ler(self):
        carro = Carro.objects(modelo = 'BMW')
        for i in carro:
            print(f'nome : {i.modelo}\nvalor : {i.valor}\ndono: {i.dono}. \n Vendido por {i.vendedor}')

    def atualizar(self,modelo_editado,valor_editado):
        try:
            carro = Carro.objects(modelo = 'BMW').get()
            carro.update(
                modelo = modelo_editado,
                valor = valor_editado
            )
            carro.reload()
            print('Editado')
        except DoesNotExist:
            print("User not found")
        

    def deletar(self):
        try:
            Carro.objects(modelo = 'BMW').delete()
            print('deletaoo')
        except DoesNotExist:
            print("User not found")


    meta = {
        'indexes' : ['modelo']
    }


vendedor = Vendedor()
vendedor.criar('jacquan','1203456879') 
# vendedor.atualizar('erick jaquin')
# vendedor.ler()
# vendedor.deletar()


comprador = Comprador()
comprador.criar('william','12034568791') 
# comprador.atualizar('willis')
# comprador.ler()
# comprador.deletar()

carro = Carro()
carro.criar('BMW', '5000,00',comprador = comprador, vendedor = vendedor)
# # carro.atualizar('AUDI','7000,00')
# carro.ler()
# carro.deletar()


