def menu():

    usuario_dados = []

    print("---------Bem vindo-------------")

    while True:

        print("1 - Cadastrar Usuario")
        print("2 - Sair")

        try:
            opcao = int(input("Digite um dos numeros correspondente a opcao desejada: "))
        
        except ValueError:

            print("Opcao invalida")

        if(opcao == 2):

            break;

        elif(opcao == 1):

            usuario = input("Digite o nome de usuario: ")
            
            tamanho_senha = 0

            while(tamanho_senha < 6):

                senha = input("Digite a senha de usuario, ela deve conter mais de 6 caracteres: ")

                tamanho_senha = len(senha)

            usuario_dados = usuario_dados + [usuario,senha]
            
            print(usuario_dados)


    return 0x00

print(menu())
            




   
