from Models import *

vendedor = Vendedor()
# vendedor.criar('jacquan', '12034568791') 
# vendedor.atualizarNome('erick jaquin', '12034568791')
vendedor.ler('12034568791')
# vendedor.deletar('12034568791')

comprador = Comprador()
# comprador.criar('william', '12034568790') 
# comprador.atualizarNome('willis', '12034568790')
comprador.ler('12034568790')
# comprador.deletar('12034568790')

carro = Carro()
# carro.criar('BMW', '5000,00', 'ABC1234', comprador = comprador, vendedor = vendedor)
# carro.atualizarModelo('AUDI', 'ABC1234')
# carro.atualizarModelo('7000,00', 'ABC1234')
carro.ler('ABC1234')
# carro.deletar('ABC1234')