from locadora import *


# Primeiro exemplo:
print('\n-------------------------------------------------\nPrimeiro Exemplo:')

# Lendo todos as coleções do banco de dados
lerLocadores()
lerClientes()
lerCarros()

#################################################################################

# Segundo exemplo:
print('\n-------------------------------------------------\nSegundo Exemplo:')

# Adicionando locadores e um carro para cada
locadorWilliam = Locador()
locadorWilliam.criar('Willian Telles', '11122233344')
locadorWilliam.atualizarNome('William Teles')
carroW = Carro()
carroW.criar('Sandeiro', '2018', '90,00', 'PFT5248', locadorWilliam)
carroW2 = Carro()
carroW2.criar('Argo', '2021', '135,00', 'KLY8365', locadorWilliam)
locadorWilliam.ler()

locadorDiego = Locador()
locadorDiego.criar('Diego Sylva', '22211133344')
locadorDiego.atualizarNome('Diego Silva')
carroD = Carro()
carroD.criar('Onix', '2020', '120,00', 'KLE8796', locadorDiego)
locadorDiego.ler()

#################################################################################

# Terceiro exemplo
print('\n-------------------------------------------------\nTerceiro Exemplo:')

# Criando um cliente
clienteGabriel = Cliente()
clienteGabriel.criar('Gabriel Lyma', '44433322211')
clienteGabriel.atualizarNome('Gabriel Lima')
clienteGabriel.ler()

# Locando um carro para o cliente
carroW.locarCarro(clienteGabriel)
carroW.ler()

#################################################################################

# Quarto exemplo
print('\n-------------------------------------------------\nQuarto Exemplo:')

# Atualizar o valor de um carro
carroD.ler()
carroD.atualizarValor('115,00')
carroD.ler()

#################################################################################

# Quinto exemplo
print('\n-------------------------------------------------\nQuinto Exemplo:')

# Ler todos as coleções do banco de dados
lerLocadores()
lerClientes()
lerCarros()
lerCarrosDisponiveis()
lerCarrosLocados()

#################################################################################

# Sexto exemplo
print('\n-------------------------------------------------\nSexto Exemplo:')

# Remover locadores do banco de dados
locadorWilliam.deletar()
carroW.ler()
locadorDiego.deletar()
carroW.ler()

# Remover clientes do banco de dados
clienteGabriel.deletar()
