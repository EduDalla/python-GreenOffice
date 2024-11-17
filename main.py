from service.serviceUser import forca_opcao, senha_len, email_regex, email_existe, \
    cadastrar_arcondicionado, deletar_arcondicionado, login_usuario, logging, cadastro_usuario, \
    select_arcondicionados_by_id, verifica_numero, select_arcondicionado, insert_mensagem

exec(open('./service/serviceUser.py').read())
print(' ' * 12, 'GreenOffice')
print('CONFORTO SAUDÁVEL, ENERGIA SUSTENTÁVEL\n')
escolha_incio = forca_opcao("Digite 1 para se cadastrar ou 2 para fazer login: ", ['1', '2'])
dados_usuario = 0
while escolha_incio != '3':
    while escolha_incio == '1':
        print("Faça seu cadastro!")
        nome = input("Diga seu nome: ")
        email = email_regex("Diga seu email: ")
        senha = senha_len("Digite sua senha: ")
        cadastro_usuario(nome, email, senha)

        logging.info(f"Usuário {nome} cadastrado com sucesso.")
        invalido = 0

        print('Você completou seu cadastro!')
        escolha_incio = '2'
        break

    while escolha_incio == '2':
        print("Faça seu login")
        try:
            email = input("Diga seu email: ")
            if not email_existe(email):
                raise ValueError("Email não encontrado.")
        except ValueError as ve:
            logging.warning(f"Tentativa de login com email inválido!")
            email = input("Email inválido! Digite novamente: ")
            email_existe(email)

        senha = input("Digite sua senha: ")
        dados_usuario = login_usuario(email, senha)
        print(dados_usuario)
        if not dados_usuario:
            logging.warning(f"Tentativa de login falhou para o email: {email}")
            escolha_incio = forca_opcao(
                "Credenciais inválidas!\nDigite 1 para se cadastrar ou 2 para fazer login novamente: ",
                ['1', '2'])
        else:
            logging.info(f"Usuário logado com sucesso: {email}")
            escolha_incio = '3'

escolha_site = forca_opcao("Home[Digite 1], Ar condicionado[Digite 2], Contato[Digite 3] - ", ['1', '2', '3'])

while True:
    if escolha_site == '1':
        print("-" * 67)
        print(' ' * 33, 'Home')
        print("-" * 67)

        print('A GreenOffice, é uma plataforma inteligente desenvolvida para reduzir o consumo de energia elétrica\n'
              'em ambientes corporativos, promovendo eficiência, sustentabilidade e saúde. Utilizando\n'
              'sensores IoT e uma interface web intuitiva e gamificada,\n'
              'o sistema monitora e controla automaticamente o ar-condicionado com base na presença de pessoas e\n'
              'condições ambientais. O objetivo é otimizar o uso dos recursos energéticos, tendo como foco a\n'
              'saúde dos colaboradores, reduzindo custos e o desperdício de energia, especialmente em horários de \n'
              'menor atividade.\n')

        print("-" * 67)
        print(' ' * 30, 'Quem somos')
        print("-" * 67)

        print("Somos um grupo de 3 estudantes da FIAP cursando Engenharia de Software no nosso primeiro ano.\n"
              "O grupo é composto por:\n"
              "Eduardo Dallabella Lima, focado em back-end;\n"
              "Helôisa Real, focada em Iot e cálculo;\n"
              "e Pedro Gustavo Schmitz, focado em front-end.\n")

        escolha_site = forca_opcao("Home[Digite 1], Ar condicionado[Digite 2], Contato[Digite 3] - ", ['1', '2', '3'])

    elif escolha_site == '2':
        print("-" * 67)
        print(' ' * 30, 'Arcondicionados', ' ' * 30)
        print("-" * 67)
        escolha_ar = forca_opcao("Cadastro[Digite 1], Verificar ar condicionados[Digite 2], Deletar ar condicionado["
                                 "Digite 3], Sair[Digite 4] - ", ['1', '2', '3', '4'])
        while escolha_ar != '4':
            if escolha_ar == '1':
                try:
                    cadastrar_arcondicionado(dados_usuario[0][0])
                    print("Ar condicionado cadastrado com sucesso!")
                except Exception as e:
                    print(f"Erro: {e}")
                escolha_ar = forca_opcao("Cadastro[Digite 1], Verificar ar condicionados[Digite 2], Deletar ar "
                                         "condicionados[Digite 3], Sair[Digite 4] - ", ['1', '2', '3', '4'])

            elif escolha_ar == '2':
                try:
                    arcondicionados = select_arcondicionados_by_id(dados_usuario[0][0])
                    if not arcondicionados:
                        print("Você não possui ar condicionados")
                        break
                    for arcondicionado in arcondicionados:
                        print(f'''Ar condicionado número - {arcondicionado[0]}
                                Nome - {arcondicionado[2]}
                                Horas de consumo - {round(arcondicionado[4])} horas
                                Consumo de energia - {round(arcondicionado[5], 2)}kWh
                                Saúde do ambiente - {round(arcondicionado[6], 1)}%''')

                    escolha_ar = forca_opcao(
                        "Cadastro[Digite 1], Verificar ar condicionados[Digite 2], Deletar ar condicionados["
                        "Digite 3], Sair[Digite 4] - ", ['1', '2', '3', '4'])
                except Exception as e:
                    print(f"Erro: {e}")

            elif escolha_ar == '3':
                arcondicionados = select_arcondicionados_by_id(dados_usuario[0][0])
                if arcondicionados:
                    for arcondicionado in arcondicionados:
                        print(f'''Ar condicionado número - {arcondicionado[0]}
                                Nome - {arcondicionado[2]}
                                Horas de consumo - {round(arcondicionado[4])} horas
                                Consumo de energia - {round(arcondicionado[5], 2)}kWh
                                Saúde do ambiente - {round(arcondicionado[6], 1)}%''')
                    escolha_del = forca_opcao("Deseja deletar algum ar condicionado? (sim/nao) ", ['sim', 'nao'])
                    while escolha_del == 'sim':
                        num_id = input("Digite o id do ar condicionado: ")
                        id_ar = verifica_numero(num_id)
                        print('okhaa')
                        air_exists = select_arcondicionado(id_ar)

                        while not air_exists:
                            num_id = input("Digite um id válido: ")
                            id_ar = verifica_numero(num_id)
                            air_exists = select_arcondicionado(id_ar)
                        deletar_arcondicionado(id_ar)

                        escolha_ar = forca_opcao(
                            "Cadastro[Digite 1], Verificar ar condicionados[Digite 2], Deletar ar condicionados["
                            "Digite 3] Sair[Digite 4] - ", ['1', '2', '3', '4'])
                        escolha_del = 'nao'
                else:
                    print("Você não possui nenhum ar condicionado cadastrado!")
                    escolha_ar = forca_opcao(
                        "Cadastro[Digite 1], Verificar ar condicionados[Digite 2], Deletar ar condicionados["
                        "Digite 3] Sair[Digite 4] - ", ['1', '2', '3', '4'])

        escolha_site = forca_opcao("Home[Digite 1], Ar condicionado[Digite 2], Contato[Digite 3] - ",
                                   ['1', '2', '3'])

    elif escolha_site == '3':
        print("-" * 67)
        print(' ' * 30, 'Contato', ' ' * 30)
        print("-" * 67)
        print(' ' * 19, 'Email - greenoffice@gmail.com', ' ' * 30)
        print(' ' * 20, 'Número - (99) 99999 - 9999', ' ' * 30)
        escolha_contato = forca_opcao("Deseja em entrar em contato conosco? (sim/nao) ",
                                   ['sim', 'nao'])
        mensagem = input("Digite sua mensagem: ")
        try:
            insert_mensagem(dados_usuario[0][0], mensagem)
            print("Mensagem enviada com sucesso! Entraremos em contato em breve!")
        except Exception as e:
            print("Algo deu errado ao enviar a mensagem! Tente mais tarde.")

        escolha_site = forca_opcao("Home[Digite 1], Ar condicionado[Digite 2], Contato[Digite 3] - ", ['1', '2', '3'])

