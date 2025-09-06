# Limpar terminal
import os
def limpar():
    os.system('cls')

executando = True

# Acumuladores gerais
contador_jogos = 0
seguridade_social_total = 0
fnc_total = 0
comite_total = 0
funpen_total = 0
fnsp_total = 0
caixa_total = 0

# Acumuladores Mega-Sena
acumulado_sena_mega = 0
acumulado_quina_mega = 0
acumulado_quadra_mega = 0
acumulado_mega = 0 
acumulado_05_mega = 0 

# Estatísticas individuais - Mega
total_sena_mega = 0
total_quina_mega = 0
total_quadra_mega = 0
arrecadacao_total_acumulado_mega = 0
outros_encargos_total_mega = 0

# Acumuladores Quina 
acumulado_quina_quina = 0
acumulado_quadra_quina = 0
acumulado_terno_quina = 0
acumulado_5_quina = 0
acumulado_prox_concurso_quina = 0
acumulado_quina_saojoao = 0

# Estatísticas individuais - Quina
total_quina_quina = 0
total_quadra_quina = 0
total_terno_quina = 0


while executando:   
    limpar()   

    print('=-=-=-=-=-= Menu =-=-=-=-=-= \n[ 1 ] Mega-Sena \n[ 2 ] Quina \n[ 3 ] Lotofácil \n[ 4 ] Estatísticas Gerais')
    escolha_menu_principal = input('Digite a opção desejada: ')
   
    if escolha_menu_principal == '1': # ESCOLHA MEGA SENA
        limpar()

        print('=-=-=-=-=-= Mega-Sena =-=-=-=-=-= ')
        print('[ 1 ] Critérios de distribuição \n[ 2 ] Cadastrar novo sorteio \n[ 3 ] Estatísticas individuais \n[ 4 ] Voltar')
        escolha_menu_loteria = input('Digite a opção desejada: ')

        if escolha_menu_loteria == '1': # CRITÉRIOS DE DISTRIBUIÇÃO - MEGA
            limpar()
            print('=-=-=-= Mega-Sena - Critérios de distribuição =-=-=-=')
            print('Prêmio Bruto Total: 46%')
            print('↳ Sena (6 acertos): 35% do prêmio bruto')
            print('↳ Quina (5 acertos): 19% do prêmio bruto')
            print('↳ Quadra (4 acertos): 19% do prêmio bruto')
            print('↳ Acúmulo concurso finais 0 ou 5: 22% do prêmio bruto') 
            print('↳ Mega da Virada: 5% do prêmio bruto')
            print('=-' * 27)
            print('Seguridade Social: 17.32%')
            print('Fundo Nacional de Cultura (FNC): 3%')
            print('Comitê Olímpico e Paralímpico: 1.7%')
            print('Fundo Penitenciário Nacional (FUNPEN): 3.14%')
            print('Fundo Nacional de Segurança Pública (FNSP): 9.26%')
            print('Custos operacionais (CAIXA): 9.57%')
            print('Outros encargos e taxas legais: 10.01%')

            print()
            escolha_sair = input('Pressione ENTER para voltar...  ')


        elif escolha_menu_loteria == '2': # CADASTRAR NOVO SORTEIO - MEGA
            limpar()

            print('=-' * 5,'Mega-Sena - Novo sorteio','=-' * 5)
            valor_aposta = input('Digite o valor da sua aposta: ')
            valor_aposta = float(valor_aposta.replace(',','.'))

            if valor_aposta == 0: # Verificação para o valor da aposta não ser R$0.00
                print('Digite corretamente o valor da aposta.')
                print('')
                
                escolha_sair = input('Pressione ENTER para voltar...  ')
            
            else:
                numero_sorteio = int(input('Digite o número do sorteio: '))

                apostas_realizadas = int(input('Digite a quantidade de apostas realizadas: '))
                if apostas_realizadas == 0: # Não realizar o sorteio se não houver jogadores.
                    print('Não foi possível realizar o sorteio.')
                    print('')

                    escolha_sair = input('Pressione ENTER para voltar...  ')

                
                else:
                    faixa_sena_mega = int(input('Digite a quantidade de ganhadores na Sena: '))
                    faixa_quina_mega = int(input('Digite a quantidade de ganhadores na Quina: '))
                    faixa_quadra_mega = int(input('Digite a quantidade de ganhadores na Quadra: '))
                    print('É Mega da Virada? \n[ 1 ] Sim \n[ 2 ] Não')
                    escolha_megavirada = input('Digite a opção desejada: ')

                    arrecadacao_total = valor_aposta * apostas_realizadas
                    seguridade_social = arrecadacao_total * 0.1732
                    fnc = arrecadacao_total * 0.03
                    comite = arrecadacao_total * 0.017
                    funpen = arrecadacao_total * 0.0314
                    fnsp = arrecadacao_total * 0.0926
                    caixa = arrecadacao_total * 0.0957
                    outros_encargos_mega = arrecadacao_total * 0.1001

                    premio_bruto = arrecadacao_total * 0.46
                    
                    limpar()

                    print('=-' * 9,'Resultado Cadastro','=-' * 9)
                    print()
                    print(f'Arrecadação total: R${arrecadacao_total:.2f}')
                    print()

                    if escolha_megavirada == '1': # É Mega Virada
                        
                        # Se for Mega + 0 ou 5
                        if escolha_megavirada == '1' and numero_sorteio % 10 == 0 or numero_sorteio % 10 == 5:
                            premio_bruto += acumulado_05_mega
                            premio_bruto += acumulado_mega

                            print(f'\033[1;31m=-=-=-=-= Jogo concurso final e Mega da Virada =-=-=-=-\033[0m')
                            print('')
                            print('=-' * 7,'Distribuição Prêmio Bruto','=-' * 7)
                            print(f'Prêmio bruto: R${premio_bruto:.2f}')

                            valor_sena_mega = premio_bruto * 0.35
                            valor_quina_mega = premio_bruto * 0.19
                            valor_quadra_mega = premio_bruto * 0.19
                            mega_virada = premio_bruto * 0.05
                            acumula_05_mega = premio_bruto * 0.22

                            # Verificação 0 ganhadores - Faixa Sena Mega
                            if faixa_sena_mega == 0:
                                acumulado_sena_mega += valor_sena_mega
                                print(f'Não houve ganhador na Faixa Sena.\n↳ Valor acumulado é de: R${acumulado_sena_mega:.2f}')
                            else: 
                                premio_sena_mega = (valor_sena_mega + acumulado_sena_mega) / faixa_sena_mega
                                print(f'Sena (6 acertos): R${premio_sena_mega:.2f}')

                                total_sena_mega += (premio_sena_mega * faixa_sena_mega)
                                acumulado_sena_mega = 0

                            # Verificação 0 ganhadores - Faixa Quina Mega
                            if faixa_quina_mega == 0:
                                acumulado_quina_mega += valor_quina_mega
                                print(f'Não houve ganhador na Faixa Quina.\n↳ Valor acumulado é de: R${acumulado_quina_mega:.2f}')
                            else: 
                                premio_quina_mega = (valor_quina_mega + acumulado_quina_mega) / faixa_quina_mega
                                print(f'Quina (5 acertos): R${premio_quina_mega:.2f}')

                                total_quina_mega += (premio_quina_mega * faixa_quina_mega)
                                acumulado_quina_mega = 0

                            # Verificação 0 ganhadores - Faixa Quadra Mega
                            if faixa_quadra_mega == 0:
                                acumulado_quadra_mega += valor_quadra_mega
                                print(f'Não houve ganhador na Faixa Quadra.\n↳ Valor acumulado é de: R${acumulado_quadra_mega:.2f}')
                            else: 
                                premio_quadra_mega = (valor_quadra_mega + acumulado_quadra_mega) / faixa_quadra_mega
                                print(f'Quadra (4 acertos): R${premio_quadra_mega:.2f}')

                                total_quadra_mega += (premio_quadra_mega * faixa_quadra_mega)
                                acumulado_quadra_mega = 0

                            print(f'Acúmulo concurso final 0 ou 5: R${acumula_05_mega:.2f}')
                            print(f'Acúmulo Mega da Virada: R${mega_virada:.2f}')

                            acumulado_mega = 0
                            acumulado_05_mega = 0

                        # Se for Mega + comum
                        elif escolha_megavirada == '1':
                            premio_bruto += acumulado_mega
                            acumulado_05_mega += acumula_05_mega

                            print(f'\033[1;31m=-=-=-=-=-=-=-=-= Jogo Mega da Virada =-=-=-=-=-=-=-=-=-\033[0m')
                            print('')
                            print('=-' * 7,'Distribuição Prêmio Bruto','=-' * 7)
                            print(f'Prêmio bruto Mega da virada: R${premio_bruto:.2f}')

                            valor_sena_mega = premio_bruto * 0.35
                            valor_quina_mega = premio_bruto * 0.19
                            valor_quadra_mega = premio_bruto * 0.19
                            mega_virada = premio_bruto * 0.05
                            acumula_05_mega = premio_bruto * 0.22

                            # Verificação 0 ganhadores - Faixa Sena Mega
                            if faixa_sena_mega == 0:
                                acumulado_sena_mega += valor_sena_mega
                                print(f'Não houve ganhador na Faixa Sena.\n↳ Valor acumulado é de: R${acumulado_sena_mega:.2f}')
                            else: 
                                premio_sena_mega = (valor_sena_mega + acumulado_sena_mega) / faixa_sena_mega
                                print(f'Sena (6 acertos): R${premio_sena_mega:.2f}')

                                total_sena_mega += (premio_sena_mega * faixa_sena_mega)
                                acumulado_sena_mega = 0

                            # Verificação 0 ganhadores - Faixa Quina Mega
                            if faixa_quina_mega == 0:
                                acumulado_quina_mega += valor_quina_mega
                                print(f'Não houve ganhador na Faixa Quina.\n↳ Valor acumulado é de: R${acumulado_quina_mega:.2f}')
                            else: 
                                premio_quina_mega = (valor_quina_mega + acumulado_quina_mega) / faixa_quina_mega
                                print(f'Quina (5 acertos): R${premio_quina_mega:.2f}')

                                total_quina_mega += (premio_quina_mega * faixa_quina_mega)
                                acumulado_quina_mega = 0

                            # Verificação 0 ganhadores - Faixa Quadra Mega
                            if faixa_quadra_mega == 0:
                                acumulado_quadra_mega += valor_quadra_mega
                                print(f'Não houve ganhador na Faixa Quadra.\n↳ Valor acumulado é de: R${acumulado_quadra_mega:.2f}')
                            else: 
                                premio_quadra_mega = (valor_quadra_mega + acumulado_quadra_mega) / faixa_quadra_mega
                                print(f'Quadra (4 acertos): R${premio_quadra_mega:.2f}')

                                total_quadra_mega += (premio_quadra_mega * faixa_quadra_mega)
                                acumulado_quadra_mega = 0

                            print(f'Acúmulo concurso final 0 ou 5: R${acumula_05_mega:.2f}')
                            print(f'Acúmulo Mega da Virada: R${mega_virada:.2f}')

                            acumulado_mega = 0
            
                    elif escolha_megavirada == '2': # Não é Mega Virada
                        # Se for comum + 0 ou 5
                        if escolha_megavirada == '2' and numero_sorteio % 10 == 0 or numero_sorteio % 10 == 5:
                            premio_bruto += acumulado_05_mega
                            acumulado_mega += mega_virada

                            print(f'\033[1;31m=-=-=-=-=-=-=-=-=- Jogo concurso final =-=-=-=-=-=-=-=-\033[0m')
                            print('')
                            print('=-' * 7,'Distribuição Prêmio Bruto','=-' * 7)
                            print(f'Prêmio bruto: R${premio_bruto:.2f}')

                            valor_sena_mega = premio_bruto * 0.35
                            valor_quina_mega = premio_bruto * 0.19
                            valor_quadra_mega = premio_bruto * 0.19
                            mega_virada = premio_bruto * 0.05
                            acumula_05_mega = premio_bruto * 0.22

                            # Verificação 0 ganhadores - Faixa Sena Mega
                            if faixa_sena_mega == 0:
                                acumulado_sena_mega += valor_sena_mega
                                print(f'Não houve ganhador na Faixa Sena.\n↳ Valor acumulado é de: R${acumulado_sena_mega:.2f}')
                            else: 
                                premio_sena_mega = (valor_sena_mega + acumulado_sena_mega) / faixa_sena_mega
                                print(f'Sena (6 acertos): R${premio_sena_mega:.2f}')

                                total_sena_mega += (premio_sena_mega * faixa_sena_mega)
                                acumulado_sena_mega = 0

                            # Verificação 0 ganhadores - Faixa Quina Mega
                            if faixa_quina_mega == 0:
                                acumulado_quina_mega += valor_quina_mega
                                print(f'Não houve ganhador na Faixa Quina.\n↳ Valor acumulado é de: R${acumulado_quina_mega:.2f}')
                            else: 
                                premio_quina_mega = (valor_quina_mega + acumulado_quina_mega) / faixa_quina_mega
                                print(f'Quina (5 acertos): R${premio_quina_mega:.2f}')

                                total_quina_mega += (premio_quina_mega * faixa_quina_mega)
                                acumulado_quina_mega = 0

                            # Verificação 0 ganhadores - Faixa Quadra Mega
                            if faixa_quadra_mega == 0:
                                acumulado_quadra_mega += valor_quadra_mega
                                print(f'Não houve ganhador na Faixa Quadra.\n↳ Valor acumulado é de: R${acumulado_quadra_mega:.2f}')
                            else: 
                                premio_quadra_mega = (valor_quadra_mega + acumulado_quadra_mega) / faixa_quadra_mega
                                print(f'Quadra (4 acertos): R${premio_quadra_mega:.2f}')

                                total_quadra_mega += (premio_quadra_mega * faixa_quadra_mega)
                                acumulado_quadra_mega = 0

                            print(f'Acúmulo concurso final 0 ou 5: R${acumula_05_mega:.2f}')
                            print(f'Acúmulo Mega da Virada: R${mega_virada:.2f}')

                            acumulado_05_mega = 0

                        # Se for comum + comum
                        elif escolha_megavirada == '2':
                            acumulado_mega += mega_virada
                            acumulado_05_mega += acumula_05_mega

                            valor_sena_mega = premio_bruto * 0.35
                            valor_quina_mega = premio_bruto * 0.19
                            valor_quadra_mega = premio_bruto * 0.19
                            mega_virada = premio_bruto * 0.05
                            acumula_05_mega = premio_bruto * 0.22

                            print(f'\033[1;31m=-'*11,'Jogo comum','=-\033[1;31m'*11,'\033[0m')
                            print('')
                            print('=-' * 7,'Distribuição Prêmio Bruto','=-' * 7)
                            print(f'Prêmio bruto: R${premio_bruto:.2f}')

                            # Verificação 0 ganhadores - Faixa Sena Mega
                            if faixa_sena_mega == 0:
                                acumulado_sena_mega += valor_sena_mega
                                print(f'Não houve ganhador na Faixa Sena.\n↳ Valor acumulado é de: R${acumulado_sena_mega:.2f}')
                            else: 
                                premio_sena_mega = (valor_sena_mega + acumulado_sena_mega) / faixa_sena_mega
                                print(f'Sena (6 acertos): R${premio_sena_mega:.2f}')

                                total_sena_mega += (premio_sena_mega * faixa_sena_mega)
                                acumulado_sena_mega = 0
                                
                            # Verificação 0 ganhadores - Faixa Quina Mega
                            if faixa_quina_mega == 0:
                                acumulado_quina_mega += valor_quina_mega
                                print(f'Não houve ganhador na Faixa Quina\n↳ Valor acumulado é de: R${acumulado_quina_mega:.2f}')
                            else: 
                                premio_quina_mega = (valor_quina_mega + acumulado_quina_mega) / faixa_quina_mega
                                print(f'Quina (5 acertos): R${premio_quina_mega:.2f}')

                                total_quina_mega += (premio_quina_mega * faixa_quina_mega)
                                acumulado_quina_mega = 0

                            # Verificação 0 ganhadores - Faixa Quadra Mega
                            if faixa_quadra_mega == 0:
                                acumulado_quadra_mega += valor_quadra_mega
                                print(f'Não houve ganhador na Faixa Quadra.\n↳ Valor acumulado é de: R${acumulado_quadra_mega:.2f}')
                            else: 
                                premio_quadra_mega = (valor_quadra_mega + acumulado_quadra_mega) / faixa_quadra_mega
                                print(f'Quadra (4 acertos): R${premio_quadra_mega:.2f}')

                                total_quadra_mega += (premio_quadra_mega * faixa_quadra_mega)
                                acumulado_quadra_mega = 0

                            print(f'Acúmulo concurso final 0 ou 5: R${acumula_05_mega:.2f}')
                            print(f'Acúmulo Mega da Virada: R${mega_virada:.2f}')

                    else:
                        print('Opção inválida. Tente novamente.')
            
                    print('=-' * 7,'Distribuição Fundos e Caixa','=-' * 7)
                    print(f'Seguridade Social: R${seguridade_social:.2f}\nFundo Nacional de Cultura (FNC): R${fnc:.2f}')
                    print(f'Comitê Olímpico e Paralímpico: R${comite:.2f}\nFundo Penitenciário Nacional (FUNPEN): R${funpen:.2f}')
                    print(f'Fundo Nacional de Segurança Pública (FNSP): R${fnsp:.2f}\nCustos Operacionais (CAIXA): R${caixa:.2f}')
                    print(f'Outros encargos e taxas legais: R${outros_encargos_mega:.2f}')

                    contador_jogos += 1
                    arrecadacao_total_acumulado_mega += arrecadacao_total
                    seguridade_social_total += seguridade_social
                    fnc_total += fnc
                    comite_total += comite
                    funpen_total += funpen
                    fnsp_total += fnsp
                    caixa_total += caixa
                    outros_encargos_total_mega += outros_encargos_mega
                    
                    print()
                    escolha_sair = input('Pressione ENTER para voltar...  ')
 
        elif escolha_menu_loteria == '3': # ESTATÍSTICAS INDIVIDUAIS - MEGA
            limpar()   

            if contador_jogos > 0:
                media_geral_premios_mega = (total_sena_mega + total_quina_mega + total_quadra_mega) / contador_jogos
                valor_medio_sena_mega = total_sena_mega / contador_jogos
                valor_medio_quina_mega = total_quina_mega / contador_jogos
                valor_medio_quadra_mega = total_quadra_mega / contador_jogos

                print('=-' * 10,'Estatísticas Individuais','=-' * 10)
                print()
                print(f'Arrecadação total: R${arrecadacao_total_acumulado_mega:.2f}')
                print()
                print('=-' * 12,'Valor médio prêmios','=-' * 12)
                print(f'Valor médio dos prêmios: R${media_geral_premios_mega:.2f}')
                print(f'Valor médio Sena (6 acertos): R${valor_medio_sena_mega:.2f}')
                print(f'Valor médio Quina (5 acertos): R${valor_medio_quina_mega:.2f}')
                print(f'Valor médio Quadra (6 acertos): R${valor_medio_quadra_mega:.2f}')
                print()
                print('=-' * 12,'Valor total fundos e Caixa','=-' * 12)
                print(f'Seguridade Social: R${seguridade_social_total:.2f}\nFundo Nacional de Cultura (FNC): R${fnc_total:.2f}')
                print(f'Comitê Olímpico e Paralímpico: R${comite_total:.2f}\nFundo Penitenciário Nacional (FUNPEN): R${funpen_total:.2f}')
                print(f'Fundo Nacional de Segurança Pública (FNSP): R${fnsp_total:.2f}\nCustos Operacionais (CAIXA): R${caixa_total:.2f}')
                print(f'Outros encargos e taxas legais: {outros_encargos_total_mega:.2f}')

                print()
                escolha_sair = input('Pressione ENTER para voltar...  ')

            else:
                print('Não foi possível carregar as estatísticas. Não há jogos cadastrados.')

                print()
                escolha_sair = input('Pressione ENTER para voltar...  ')

        else:
            print('') # VOLTAR
    
    elif escolha_menu_principal == '2': # ESCOLHA QUINA
        limpar()

        print('=-=-=-=-=-=-= Quina =-=-=-=-=-=-=')
        print('[ 1 ] Critérios de distribuição \n[ 2 ] Cadastrar novo sorteio \n[ 3 ] Estatísticas individuais \n[ 4 ] Voltar')
        escolha_menu_loteria = input('Digite a opção desejada: ')

        if escolha_menu_loteria == '1': # CRITÉRIOS DE DISTRIBUIÇÃO - QUINA
            limpar()
            print('=-=-=-=-= Quina - Critérios de distribuição =-=-=-=-=')
            print('Prêmio Bruto Total: 50%')
            print('↳ Quina (5 acertos): 35% do prêmio bruto')
            print('↳ Quadra (4 acertos): 15% do prêmio bruto')
            print('↳ Terno (3 acertos): 10% do prêmio bruto')
            print('↳ Quina de São João: 15% do prêmio bruto')
            print('↳ Acúmulo concursos finais 5: 15% do prêmio bruto') 
            print('↳ Acúmulo para próximo concurso: 10% do prêmio bruto') 
            print('=-' * 27)
            print('Seguridade Social: 17.32%')
            print('Fundo Nacional de Cultura (FNC): 3%')
            print('Comitê Olímpico e Paralímpico: 1.7%')
            print('Fundo Penitenciário Nacional (FUNPEN): 3.14%')
            print('Fundo Nacional de Segurança Pública (FNSP): 9.26%')
            print('Custos operacionais (CAIXA): 9.57%')
            print('Outros encargos e taxas legais: 6.01%')

            print()
            escolha_sair = input('Pressione ENTER para voltar...  ')
        
        elif escolha_menu_loteria == '2': # CADASTRAR NOVO SORTEIO - QUINA
            limpar()

            print('=-' * 6,'Quina - Novo sorteio','=-' * 6)
            valor_aposta = input('Digite o valor da sua aposta: ')
            valor_aposta = float(valor_aposta.replace(',','.'))

            if valor_aposta == 0: # Verificação para o valor da aposta não ser R$0.00
                print('Digite corretamente o valor da aposta.')
                print('')
                
                escolha_sair = input('Pressione ENTER para voltar...  ')
            
            else:
                numero_sorteio = int(input('Digite o número do sorteio: '))

                apostas_realizadas = int(input('Digite a quantidade de apostas realizadas: '))
                if apostas_realizadas == 0: # Não realizar o sorteio se não houver jogadores.
                    print('Não foi possível realizar o sorteio.')
                    print('')

                    escolha_sair = input('Pressione ENTER para voltar...  ')
                
                else:
                    faixa_quina_quina = int(input('Digite a quantidade de ganhadores na Quina: '))
                    faixa_quadra_quina = int(input('Digite a quantidade de ganhadores na Quadra: '))
                    faixa_terno_quina = int(input('Digite a quantidade de ganhadores no Terno: '))
                    print('É Quina de São João? \n[ 1 ] Sim \n[ 2 ] Não')
                    escolha_quinasj = input('Digite a opção desejada: ')

                    arrecadacao_total = valor_aposta * apostas_realizadas
                    seguridade_social = arrecadacao_total * 0.1732
                    fnc = arrecadacao_total * 0.03
                    comite = arrecadacao_total * 0.017
                    funpen = arrecadacao_total * 0.0314
                    fnsp = arrecadacao_total * 0.0926
                    caixa = arrecadacao_total * 0.0957
                    outros_encargos_mega = arrecadacao_total * 0.1001

                    premio_bruto = arrecadacao_total * 0.50

                    limpar()

                    print('=-' * 9,'Resultado Cadastro','=-' * 9)
                    print()
                    print(f'Arrecadação total: R${arrecadacao_total:.2f}')
                    print()

                    if escolha_quinasj == '1': # É Quina de São João
                        
                        # Se for Quina São João + 5
                        if escolha_quinasj == '1' and numero_sorteio % 10 == 5:
                            premio_bruto += acumulado_5_quina
                            premio_bruto += acumulado_quina_saojoao
                            premio_bruto += acumulado_prox_concurso_quina

                            print(f'\033[1;31m=-=-=-= Jogo concurso final e Quina de São João =-=-=-\033[0m')
                            print('')
                            print('=-' * 7,'Distribuição Prêmio Bruto','=-' * 7)
                            print(f'Prêmio bruto: R${premio_bruto:.2f}')

                            valor_quina_quina = premio_bruto * 0.35
                            valor_quadra_quina = premio_bruto * 0.15
                            valor_terno_quina = premio_bruto * 0.10
                            quina_sao_joao = premio_bruto * 0.15
                            acumula_5_quina = premio_bruto * 0.15
                            acumulado_prox_concurso_quina = premio_bruto * 0.1

                            # Verificação 0 ganhadores - Faixa Quina Quina
                            if faixa_quina_quina == 0:
                                acumulado_quadra_quina += valor_quina_quina
                                print(f'Não houve ganhador na Faixa Quina.\n↳ Valor acumulado é de: R${acumulado_quina_quina:.2f}')
                            else: 
                                premio_quina_quina = (valor_quina_quina + acumulado_quina_quina) / faixa_quina_quina
                                print(f'Quina (5 acertos): R${premio_quina_quina:.2f}')

                                total_quina_quina += (premio_quina_quina * faixa_quina_quina)
                                acumulado_quina_quina = 0

                            # Verificação 0 ganhadores - Faixa Quadra Quina
                            if faixa_quadra_quina == 0:
                                acumulado_quadra_quina += valor_quadra_quina
                                print(f'Não houve ganhador na Faixa Quadra.\n↳ Valor acumulado é de: R${acumulado_quadra_quina:.2f}')
                            else: 
                                premio_quadra_quina = (valor_quadra_quina + acumulado_quadra_quina) / faixa_quadra_quina
                                print(f'Quadra (4 acertos): R${premio_quadra_quina:.2f}')

                                total_quadra_quina += (premio_quadra_quina * faixa_quadra_quina)
                                acumulado_quadra_quina = 0

                            # Verificação 0 ganhadores - Faixa Terno Quina
                            if faixa_terno_quina == 0:
                                acumulado_terno_quina += valor_terno_quina
                                print(f'Não houve ganhador na Faixa Terno.\n↳ Valor acumulado é de: R${acumulado_terno_quina:.2f}')
                            else: 
                                premio_terno_quina = (valor_terno_quina + acumulado_terno_quina) / faixa_terno_quina
                                print(f'Terno (3 acertos): R${premio_terno_quina:.2f}')

                                total_terno_quina += (premio_terno_quina * faixa_terno_quina)
                                acumulado_terno_quina = 0

                            print(f'Acúmulo concurso final 5: R${acumula_5_quina:.2f}')
                            print(f'Acúmulo Quina de São João: R${quina_sao_joao:.2f}')
                            print(f'Acúmulo próximo concurso: {acumulado_prox_concurso_quina}')

                            acumulado_quina_saojoao = 0
                            acumulado_5_quina = 0

                        # Se for Quina SJ + comum
                        elif escolha_quinasj == '1':
                            premio_bruto += acumulado_quina_saojoao
                            acumulado_5_quina += acumula_5_quina

                            print(f'\033[1;31m=-=-=-=-=-=-=-=- Jogo Quina de São João =-=-=-=-=-=-=-=-\033[0m')
                            print('')
                            print('=-' * 7,'Distribuição Prêmio Bruto','=-' * 7)
                            print(f'Prêmio bruto Quina de São João: R${premio_bruto:.2f}')

                            valor_quina_quina = premio_bruto * 0.35
                            valor_quadra_quina = premio_bruto * 0.15
                            valor_terno_quina = premio_bruto * 0.10
                            quina_sao_joao = premio_bruto * 0.15
                            acumula_5_quina = premio_bruto * 0.15
                            acumulado_prox_concurso_quina = premio_bruto * 0.1

                            # Verificação 0 ganhadores - Faixa Quina Quina
                            if faixa_quina_quina == 0:
                                acumulado_quina_quina += valor_quina_quina
                                print(f'Não houve ganhador na Faixa Quina.\n↳ Valor acumulado é de: R${acumulado_quina_quina:.2f}')
                            else: 
                                premio_quina_quina = (valor_quina_quina + acumulado_quina_quina) / faixa_quina_quina
                                print(f'Sena (6 acertos): R${premio_sena_mega:.2f}')

                                total_sena_mega += (premio_sena_mega * faixa_sena_mega)
                                acumulado_sena_mega = 0

                            # Verificação 0 ganhadores - Faixa Quina Mega
                            if faixa_quina_mega == 0:
                                acumulado_quina_mega += valor_quina_mega
                                print(f'Não houve ganhador na Faixa Quina.\n↳ Valor acumulado é de: R${acumulado_quina_mega:.2f}')
                            else: 
                                premio_quina_mega = (valor_quina_mega + acumulado_quina_mega) / faixa_quina_mega
                                print(f'Quina (5 acertos): R${premio_quina_mega:.2f}')

                                total_quina_mega += (premio_quina_mega * faixa_quina_mega)
                                acumulado_quina_mega = 0

                            # Verificação 0 ganhadores - Faixa Quadra Mega
                            if faixa_quadra_mega == 0:
                                acumulado_quadra_mega += valor_quadra_mega
                                print(f'Não houve ganhador na Faixa Quadra.\n↳ Valor acumulado é de: R${acumulado_quadra_mega:.2f}')
                            else: 
                                premio_quadra_mega = (valor_quadra_mega + acumulado_quadra_mega) / faixa_quadra_mega
                                print(f'Quadra (4 acertos): R${premio_quadra_mega:.2f}')

                                total_quadra_mega += (premio_quadra_mega * faixa_quadra_mega)
                                acumulado_quadra_mega = 0

                            print(f'Acúmulo concurso final 0 ou 5: R${acumula_05_mega:.2f}')
                            print(f'Acúmulo Mega da Virada: R${mega_virada:.2f}')

                            acumulado_mega = 0








