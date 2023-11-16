from models.cliente import Cliente
from models.conta import Conta

fel: Cliente = Cliente('Thiago', 'thvcorreia@hotmail.com', '001.815.612-63', '27/05/1992')

print(fel)

conta: Conta = Conta(fel)

print(conta)
