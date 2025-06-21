
import datetime

# Variáveis globais
saldo = 0.0
limite_saque = 500.0
extrato = ""
saques_realizados = 0
LIMITE_SAQUES_DIARIOS = 3

# Funções
def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"{datetime.datetime.now()}: Depósito de R$ {valor:.2f}\n"
        print(f">>> Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(">>> Operação falhou! O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo, extrato, saques_realizados
    if saques_realizados >= LIMITE_SAQUES_DIARIOS:
        print(">>> Limite diário de saques atingido.")
    elif valor > limite_saque:
        print(f">>> Saque não permitido. Limite por saque: R$ {limite_saque:.2f}.")
    elif valor > saldo:
        print(">>> Saldo insuficiente.")
    elif valor <= 0:
        print(">>> Valor inválido.")
    else:
        saldo -= valor
        saques_realizados += 1
        extrato += f"{datetime.datetime.now()}: Saque de R$ {valor:.2f}\n"
        print(f">>> Saque de R$ {valor:.2f} realizado com sucesso!")

def exibir_extrato():
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=================================\n")

def simular_fluxo(opcao, valor=0.0):
    if opcao == "1":
        depositar(valor)
    elif opcao == "2":
        sacar(valor)
    elif opcao == "3":
        exibir_extrato()
    else:
        print(">>> Opção inválida.")
