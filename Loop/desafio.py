senha_correta=123456
iteracao=3
while iteracao>0:
    print(f"Você tem {iteracao} tentativas")
    senha=int(input("Digite sua senha: "))
    if senha!= senha_correta: 
        print("Senha incorreta")
        iteracao-=1
    else:
        print("Senha correta")
        print(f"Olá Carlos. Seja Bem vindo ao nosso banco!")
        break
    if iteracao==0:
        print("Sua senha foi bloqueada! Por favor se dirija aos nossos caixas")