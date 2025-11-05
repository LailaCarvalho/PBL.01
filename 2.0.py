import os
def limpar():
    os.system('cls')

rodando = True 

def gerar_id():
    id_base = '1000' # 1º ID

    try:
        with open('id.txt', 'r', encoding='utf-8') as id:
            id_linha = id.read()
            ultimo_id = int(id_linha) 
            atual_id = ultimo_id + 1
            atual_id_str = str(atual_id)

        with open('id.txt', 'w', encoding='utf-8') as id:
            id.write(atual_id_str)

    except FileNotFoundError:
        with open('id.txt', 'w', encoding='utf-8') as id:
            atual_id_str = id_base
            id.write(atual_id_str)
        
    return atual_id_str

def cadastrar_noticia():
    with open('noticias.txt', 'a', encoding='utf-8') as noticia:

        print(f'\033[31;1m{'=-='*4} CADASTRO {'=-='*4}\033[0m')
        titulo_materia = input('Digite o título da matéria: ')
        url = input('Digite o URL da matéria: ')
        print('O status é:\n1. Verdadeiro\n2. Falso\n3. Não checado')

        try:
            escolha_status = int(input('Digite a opção desejada: '))

            if escolha_status == 1:
                ids = gerar_id() # Chama o ID apenas quando as opções forem válidas.

                noticia.write(f'{titulo_materia} - {ids}\n')
                noticia.write(f'{url}\n')
                noticia.write('Status: Verdadeiro\n')

            elif escolha_status == 2: 
                ids = gerar_id() # Chama o ID apenas quando as opções forem válidas.

                noticia.write(f'{titulo_materia} - {ids}\n')
                noticia.write(f'{url}\n')
                noticia.write('Status: Falso\n')

            elif escolha_status == 3:
                ids = gerar_id() # Chama o ID apenas quando as opções forem válidas.

                noticia.write(f'{titulo_materia} - {ids}\n')
                noticia.write(f'{url}\n')
                noticia.write('Status: Não checado\n')

            else:
                limpar()
                print('\033[;1mOpção inválida. Aperte qualquer tecla e tente novamente.\033[0m')
                pausa = input('') # Serve como um "pause" para a leitura do print. 
            
            noticia.write('\n') # Separação visual das notícias. 

        except ValueError:
            limpar()
            print('\033[;1mOpção inválida. Aperte qualquer tecla e tente novamente.\033[0m')
            pausa = input('') # Serve como um "pause" para a leitura do print. 

def consultar_noticias(): # BUSCA NAO TA FUNCIONANDO
    try:
        with open('noticias.txt', 'r', encoding='utf-8') as noticia:
            visualizar_noticias = noticia.read()
            print(f'\033[31;1m{'=-='*3} NOTÍCIAS CADASTRADAS {'=-='*3}\033[0m')
            print(visualizar_noticias)

            escolha_filtrar = str(input('Você deseja filtrar as notícias? [S/N] ')).upper()

            if escolha_filtrar == 'S':
                # qual_filtro = int(input('Deseja filtrar por:\n1. Título\n2. Status\n3. ID\n4. Link'))
                palavra_chave = input('Insira a palavra-chave: ')
                print(visualizar_noticias.find(palavra_chave))

            elif escolha_filtrar == 'N':
                print('\033[;1mAperte qualquer tecla e volte para o menu principal.\033[0m')
            else:
                print('\033[;1mOpção inválida. Aperte qualquer tecla e tente novamente.\033[0m')
        
    except FileNotFoundError:
        print('\033[;1mNotícias não encontradas. Cadastre no mínimo uma e tente novamente.\033[0m')
        
    pausa = input('') # Serve como um "pause" para a leitura do print. 

# def atualizar_noticia():

def gerar_relatorio():
    limpar()

    total_noticias = 0.0
    total_noticias_verdadeiras = 0.0
    total_noticias_falsas = 0.0
    total_noticias_naochecadas = 0.0

    try:
        with open('noticias.txt', 'r', encoding='utf-8') as noticia:
            linhas = noticia.readlines()

            for i in range(0, len(linhas), 4): # Divide em "blocos" cada notícia. 
                if i + 2 < len(linhas):                    
                    if linhas[i+2] == 'Status: Verdadeiro\n':
                        total_noticias_verdadeiras += 1
                    elif linhas[i+2] == 'Status: Falso\n':
                        total_noticias_falsas += 1
                    elif linhas[i+2] == 'Status: Não checado\n':
                        total_noticias_naochecadas += 1
            
            total_noticias = total_noticias_verdadeiras + total_noticias_falsas + total_noticias_naochecadas
            
    except: 
        pass
    
    with open('relatorio.txt', 'w', encoding='utf-8') as relatorio:
        relatorio.write(f"{'=-='*4} RELATÓRIO {'=-='*4}\n")
        relatorio.write(f'Total de notícias cadastradas: {total_noticias:.0f}\n')

        if total_noticias > 0:
            relatorio.write(f'Total de notícias verdadeiras: {total_noticias_verdadeiras:.0f} - {(total_noticias_verdadeiras * 100) / total_noticias}%\n')
            relatorio.write(f'Total de notícias falsas: {total_noticias_falsas:.0f} - {(total_noticias_falsas * 100) / total_noticias}%\n')
            relatorio.write(f'Total de notícias não checadas: {total_noticias_naochecadas:.0f} - {(total_noticias_naochecadas * 100) / total_noticias}%\n')
        else: 
            relatorio.write(f'Total de notícias verdadeiras: 0 - 0%\n')
            relatorio.write(f'Total de notícias falsas: 0 - 0%\n')
            relatorio.write(f'Total de notícias não checadas: 0 - 0%\n')
            
    print(f'\033[;1mRelatório gerado com {total_noticias:.0f} notícia(s) cadastrada(s). Aperte qualquer tecla e volte para o menu inicial.\033[0m')
    pausa = input('') # Serve como um "pause" para a leitura do print. 

# MENU PRINCIPAL
while rodando:
    limpar()
    print(''\
    f'\033[31;1m{'=-='*4} MENU {'=-='*4}\033[0m\n'
    '1. Cadastrar uma notícia\n' \
    '2. Consultar notícias\n' \
    '3. Atualizar notícias\n' \
    '4. Gerar um relatório\n' \
    '5. Sair')
    print()

    try:
        opcao_menu = int(input('Digite a posição desejada: '))

        if opcao_menu == 1:
            limpar()
            cadastrar_noticia()
        elif opcao_menu == 2:
            limpar()
            consultar_noticias()
        elif opcao_menu == 4:
            limpar()
            gerar_relatorio()
        elif opcao_menu == 5:
            limpar()
            rodando = False
        else:
            print('\033[;1mOpção inválida. Aperte qualquer tecla e tente novamente.\033[0m')
            pausa = input('') # Serve como um "pause" para a leitura do print. 


    except ValueError:
        limpar()
        print('\033[;1mOpção inválida. Aperte qualquer tecla e tente novamente.\033[0m')
        pausa = input('') # Serve como um "pause" para a leitura do print. 



