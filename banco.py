from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('**************************************')
    print('*************** ATM ******************')
    print('********** Valentim Bank *************')
    print('**************************************')
    print('Selecione a opção desejada:\n'
          '1 - Criar conta\n'
          '2 - Efeturar saque\n'
          '3 - Efetuar deposito\n'
          '4 - Efetuar transferência\n'
          '5 - Listar contas\n'
          '6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Saindo do sistema!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente...')
    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail: ')
    cpf: str = input('CPF: ')
    data_nascimento: str = input('Data de nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso:')
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe a sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)

        else:
            print(f'Não foi possível encontrar a conta {numero}, tente novamente!')
    else:
        print('Ainda não existem contas cadastradas!')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe a sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do deposito: '))

            conta.depositar(valor)

        else:
            print(f'Não foi possível encontrar a conta {numero}, tente novamente!')
    else:
        print('Ainda não existem contas cadastradas!')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_orig: int = int(input('Informe a sua conta: '))

        conta_orig: Conta = buscar_conta_por_numero(numero_orig)

        if conta_orig:
            numero_dest: int = int(input('Informe a sua conta: '))

            conta_dest: Conta = buscar_conta_por_numero(numero_dest)

            if conta_dest:
                valor: float = float(input('Informe o valor que deseja transferir: '))
                conta_orig.transferir(valor)
                valor: float = float(input('Informe o valor do saque: '))
                conta_orig.transferir(conta_dest, valor)
            else:
                print(f'Não foi possível encontrar a conta {numero_dest}, tente novamente!')
        else:
            print(f'Não foi possível encontrar a conta {numero_orig}, tente novamente!')
    else:
        print('Ainda não existem contas cadastradas!')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Contas cadastradas')
        for conta in contas:
            print(conta)
            print('__________________')
            sleep(1)
    else:
        print('Ainda não existem contas cadastradas!')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c
    menu()


if __name__ == '__main__':
    main()
