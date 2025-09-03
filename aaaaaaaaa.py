# Limpar terminal
import os
def limpar():
    os.system('cls')

 # Acumuladores Mega-Sena
acumulado_sena = 0
acumulado_quina = 0
acumulado_quadra = 0
acumulado_mega = 0 
acumulado_05 = 0 

while True:    
    print('=-=-=-=-= Menu =-=-=-=-= \n[ 1 ] Mega-Sena \n[ 2 ] Quina \n[ 3 ] Lotofácil \n[ 4 ] Estatísticas Gerais')
    escolha_menu_principal = input('Digite a opção desejada: ')
    limpar()


    if escolha_menu_principal == '1':
        limpar()

        print('=-=-=-=-= Mega-Sena =-=-=-=-= ')
        print('[ 1 ] Critérios de distribuição \n[ 2 ] Cadastrar novo sorteio \n[ 3 ] Estatísticas individuais \n[ 4 ] Voltar')
        escolha_menu_loteria = input('Digite a opção desejada: ')

        if escolha_menu_loteria == '1':
            limpar()
            print('=-=-= Mega-Sena - Critérios de Distribuição: =-=-=')
            print('Prêmio Bruto Total: 46%')
            print('↳ Sena (6 acertos): 35%')
            print('↳ Quina (5 acertos): 19%')
            print('↳ Acúmulo finais 0 ou 5: 22%') 
            print('↳ Quadra (4 acertos): 19%')
            print('↳ Mega da Virada: 5%')
            print('=-=' * 20)
            print('Seguridade Social: 17.32%')
            print('Fundo Nacional de Cultura (FNC): 3%')
            print('Comitê Olímpico e Paralímpico: 1.7%')
            print('Fundo Penitenciário Nacional (FUNPEN): 3.14%')
            print('Fundo Nacional de Segurança Pública (FNSP): 9.26%')
            print('Custos operacionais (CAIXA): 9.57%')
            print('Outros encargos e taxas legais: 10.01%')
            print('=-=' * 20)

            print('[ 1 ] Sair')
            escolha_criterios_mega = input('Digite a opção desejada: ')

        if escolha_menu_loteria == '2':
            limpar()

            valor_aposta = input('\033[1mOlá jogador(a)!\033[0m\nQual o valor da sua aposta? ')
            valor_aposta = float(valor_aposta.replace(',','.'))
            numero_sorteio = int(input('Qual o número do sorteio? '))
            apostas_realizadas = int(input('Quantas apostas foram realizadas? '))
            faixa_senaM = int(input('Quantos ganhadores houveram na Sena? '))
            faixa_quinaM = int(input('Quantos ganhadores houveram na Quina? '))
            faixa_quadraM = int(input('Quantos ganhadores houveram na Quadra? '))
            print('É Mega da Virada? \n[ 1 ] Sim \n[ 2 ] Não')
            escolha_megavirada = input('Digite a opção desejada: ')

            arrecadacao_total = valor_aposta * apostas_realizadas
            seguridade_social = arrecadacao_total * 0.1732
            fnc = arrecadacao_total * 0.03
            comite = arrecadacao_total * 0.017
            funpen = arrecadacao_total * 0.0314
            fnsp = arrecadacao_total * 0.0926
            caixa = arrecadacao_total * 0.0957
            outros_encargos = arrecadacao_total * 0.1001

            premio_bruto = arrecadacao_total * 0.46
            valor_senaM = premio_bruto * 0.35
            valor_quinaM = premio_bruto * 0.19
            valor_quadraM = premio_bruto * 0.19
            mega_virada = premio_bruto * 0.05
            acumula_05 = premio_bruto * 0.22
            
            limpar()

            print(f'=-=-=-= Distribuição Prêmio Bruto =-=-=-=')

            if numero_sorteio % 5 == 0:

                premio_bruto += acumulado_05

                acumulado_05 = 0

                print(f'Arrecadação Total: {arrecadacao_total:.2f}')
                print(f'O jogo é concurso final.\nPrêmio Bruto é de: R${acumulado_05 + premio_bruto:.2f}')
  
            else: 
                print(f'Arrecadação Total: {arrecadacao_total:.2f}')
                print(f'Prêmio Bruto é de: R${premio_bruto:.2f}')
                
            if faixa_senaM == 0:
                    acumulado_sena += valor_senaM
                    print(f'Não houve ganhador na Faixa Sena. O valor acumulado é de: R${acumulado_sena:.2f}')
            else: 
                premio_sena = (valor_senaM + acumulado_sena) / faixa_senaM
                print(f'Cada ganhador da Sena recebe: R${premio_sena:.2f}')
                acumulado_sena = 0

            if faixa_quinaM == 0:
                acumulado_quina += valor_quinaM
                print(f'Não houve ganhador na Faixa Quina. O valor acumulado é de: R${acumulado_quina:.2f}')
            else: 
                premio_quina = (valor_quinaM + acumulado_quina) / faixa_quinaM
                print(f'Cada ganhador da Quina recebe: R${premio_quina:.2f}')
                acumulado_quina = 0

            if faixa_quadraM == 0:
                acumulado_quadra += valor_quadraM
                print(f'Não houve ganhador na Faixa Quadra. O valor acumulado é de: R${acumulado_quadra:.2f}')
            else: 
                premio_quadra = (valor_quadraM + acumulado_quadra) / faixa_quadraM
                print(f'Cada ganhador da Quadra recebe: R${premio_quadra:.2f}')
                acumulado_quadra = 0

            if escolha_megavirada == '1':

                premio_bruto += acumulado_mega
                
                valor_senaM = premio_bruto * 0.35
                valor_quinaM = premio_bruto * 0.19
                valor_quadraM = premio_bruto * 0.19
                mega_virada = premio_bruto * 0.05
                acumula_05 = premio_bruto * 0.22

                print(f'Prêmio bruto Mega da virada: R${premio_bruto:.2f}')
                print(f'Sena Mega da Virada: R${valor_senaM:.2f}')
                print(f'Quina Mega da Virada: R${valor_quinaM:.2f}')
                print(f'Quadra Mega da Virada: R${valor_quadraM:.2f} ')
                print(f'Acúmulo concurso final 0 ou 5: R${acumula_05:.2f}')
                print(f'Valor acúmulo próxima Mega da Virada: R${mega_virada:.2f}')
                print(f'{acumulado_mega}')

                acumulado_mega = 0 + mega_virada

            elif escolha_megavirada == '2':
                acumulado_mega += mega_virada
                print(f'Acúmulo Mega da Virada: R${mega_virada:.2f}')
                print(f'{acumulado_mega}')


            else:
                print('Opção inváilida. Tente novamente.')
            
            print(f'Acúmulo Concursos finais 0 e 5: R${acumula_05:.2f}')

            print('=-=' * 17)

            print(f'=-=-= Distribuição Fundos e Caixa  =-=-=')
            print(f'Seguridade Social: R${seguridade_social:.2f}\nFundo Nacional de Cultura (FNC): R${fnc:.2f}')
            print(f'Comitê Olímpico e Paralímpico: R${comite:.2f}\nFundo Penitenciário Nacional (FUNPEN): R${funpen:.2f}')
            print(f'Fundo Nacional de Segurança Pública (FNSP): R${fnsp:.2f}\nCustos Operacionais: R${caixa:.2f}')
            print(f'Outros encargos e taxas legais: {outros_encargos:.2f}')

            print('[ 1 ] Sair')
            escolha_sair = input('Digite a opção desejada: ')
            limpar()


