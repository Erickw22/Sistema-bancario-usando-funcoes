#Criando um sistema bancario
def menu():
    menu = """\n
    *****************MENU*****************
    [d]\t Deposito
    [s]\t Sacar
    [e]\tExtrato
    [nc]\tNova conta
    [mc]\tMostrar contas
    [nu]\tNovo cliente
    [q]\tSair
    =>"""
    return input(menu)


def depositar(saldo, valor, extrato, /) :
    if valor >0:
      saldo += valor
      extrato += f"Deposito no valor de R$ {valor:.2f}\n"
      print("\n ### Deposito realizado! ###")
    else:
      print("Valor informado é invalido")

      return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n### Saldo insuficiente. ###")
        
    elif excedeu_limite:
        print("\n### Limite de valor para saque diario atingido. ###")
        
    elif excedeu_saques:
        print("\n### Limite de saques diarios atingidos. ###")
        
    elif valor > 0:
        saldo -=valor
        extrato += f"Saque no valor de R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso! ")

    else:
        print("\n### Valor informado é invalido. ###")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n----------------Extrato----------------")
    print("Não ouve nemhuma movimentação." if not extrato else extrato)
    print(f"Seu saldo é de R${saldo:.2f}")
    print("--------------------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente os números): ")
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
       print("\n ### usuario ja existente, tente com outro CPF: ###")
       return
    nome = input("Digite seu none completo: ")
    data_nascimento = input("Digite sua data de nascimento (dia-mês-ano): ")
    endereco = input ("Digite o seu endereço (CEP, cidade, bairro, estado e número da casa): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})

    print("******* Conta criada com sucesso! *******")
              
def filtrar_usuario (cpf, usuarios):
   usuarios_filtradas = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
   return usuarios_filtradas[0] if usuarios_filtradas else None

def criar_conta(agencia, numero_conta, usuarios):
   cpf = input ('Informe seu cpf para criar a conta: ')
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print("\n****** Conta criada com sucesso! ******")
      return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
   
   print("\n###### Usuário não encontrado, secção encerrada! ######")

def mostrar_contas(contas):
   for conta in contas:
       linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t {conta ["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
       print("="+100)
       print(linha)


def main():
   LIMITE_SAQUES = 3
   AGENCIA = "0001"


   saldo = 0
   limite = 500
   extrato =""
   numero_saques=0
   usuarios = []
   contas = []

   while True:
        opcao = menu()

        if opcao == "d":
             valor = float(input("Qual valor você  deseja depositar? "))

             saldo, extrato = depositar(saldo, valor, extrato)
      
        elif opcao == "s":
            valor = float(input("Qual o valor você deseja sacar? "))

            saldo, extrato= sacar(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite= limite,
                excedeu_limite =  numero_saques,
                excedeu_saques = LIMITE_SAQUES,
            )
                
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == "mc":
            mostrar_contas(contas)
        
        elif opcao == "q":
            break

        else:
            print("Opção invalida, selecione outas opção no menu.")

main()