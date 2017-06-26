from time import strftime

#uso do método time.strftime para capturar o ano atual com 04 dígitos
ano_atual = int(strftime("%Y"))
adm = total = 0
nome = mat = ''


def menu():
    """Função que estabelece o menu inicial do programa."""

    print("\t   CALCULADORA DE QUINQUÊNIOS - LICENÇA PRÊMIO v3.1 BETA\n\n")
    print("Calcule quantos quinquênios de licenca prêmio o servidor da SEMED tem direito.\n")
    execucao()
    encerramento()
    relatorio()


def execucao():
    """Função que solicita admissao do servidor e retorna a quantidade de quinquenios disponiveis para análise."""

    #chamada das variáveis globais para serem usadas dentro da definição da função
    global ano_atual, adm, nome, mat

    nome = input("Nome do servidor: ")
    mat = input("Matrícula: ")

    while True:

        #bloco de tratamento de erros para evitar que o usuário digite um tipo diferente de dado para 'adm'
        try:
            adm = int(input("\nDigite o ano de admissão com 04 dígitos e aperte ENTER [ex: 1988]: \n"))

            #verifica se o tamanho do ano digitado corresponde ao solicitado
            if len(str(adm)) != 4:
                print('O ano precisa ter 04 dígitos. Exemplo: 2010 ')
                continue
            else:
                #verifica se o ano digitado é válido
                if adm > ano_atual:
                    print("Admissão posterior ao ano atual. Tente novamente.")
                    continue
                else:
                    break

        except ValueError:
            #se o usuário digitar um tipo diferente de 'int' para 'adm', surge a mensagem da exceção
            print("Você usou um valor não-numérico. Tente novamente.")

    while True:

        # solicita se o servidor possui algum impedimento e armazena na variável faltas_lic
        #usa o método .lower() pra transformar o conteúdo da variável pra minúsculo
        faltas_lic = input("O servidor possui faltas injustificadas, licenças para tratar de interesse particular ou acompanhar familiares? \
Digite 's' para 'SIM' ou 'n' para 'NÃO' e aperte ENTER: \n").lower()

        # checa se o usuário optou por 'sim', executa a função com_imped e interrompe o laço
        if faltas_lic == "s":
            com_imped()
            break
        # checa se o usuário optou por 'não', executa a função sem_imped e interrompe o laço
        elif faltas_lic == "n":
            sem_imped()
            break
        else:
            # reinicia o loop, caso a opção escolhida seja diferente das acima
            print("Opção inválida. Digite 's' para 'SIM' ou 'n' para 'NÃO':\n")
            continue


def sem_imped():
    """Função que calcula os quinquênios disponíveis para licença de um servidor sem impedimentos\
(faltas injustificadas, licenças para tratar de interesse particular ou acompanhar familiares)."""

    global ano_atual, adm, total

    while True:

        # calcula a quantidade de quinquênios disponíveis
        quinq = (ano_atual - adm) // 5

        try:

            # recebe a quantidade de quinquênios tirados pelo servidor
            lic_tirada = int(input(
                "Digite quantos quinquênios o servidor já tirou. Se o servidor nunca usufruiu de Licença Prêmio, digite 0: \n"))

            # checa se a quantidade de licenças tiradas é maior do que as disponíveis
            if lic_tirada <= quinq:
                total = quinq - lic_tirada
                print("O servidor tem direito a {} quinquenio(s) = {} meses".format(total, total * 3))
            else:
                print("O servidor ainda não completou {} quinquenios, tente novamente.".format(lic_tirada))
            break
        except ValueError:
            print("Você usou um valor não-numérico. Tente novamente.")


def com_imped():
    global ano_atual, adm, total

    # cria uma lista que irá armazenar todos os anos analisados
    anos = []
    # itera desde o ano de admissão até o atual, incluindo cada ano na lista anos
    for i in range(adm, ano_atual + 1):
        anos.append(i)

    print("Digite o ano em que o servidor possui falta, licença sem vencimento ou licença para acompanhar familiares, UM POR VEZ, e aperte ENTER.\n\
Caso a licença seja maior que um ano, colocar todos os anos de afastamento, sempre UM POR VEZ e aperte ENTER.\n\
Para parar de adicionar anos, digite SAIR e aperte ENTER\n")

    while True:

        # solicita um ano em que há impedimento
        ano_imp = input().lower()
        # checa se o usuário digitou 'sair' e sai do loop
        if ano_imp == 'sair':
            break
        else:
            # transforma o tipo de ano_imp em int
            ano_imp = int(ano_imp)
            # checa se o usuário informou um ano válido
            if ano_imp < adm or ano_imp > ano_atual:
                print("Insira um ano válido!\n")
                continue

            # checa se o ano_imp está na lista anos
            if ano_imp in anos:
                # se ano_imp estiver em anos, acha sua posição
                pos = anos.index(ano_imp)
                # remove o item da lista anos
                del anos[pos]
            else:
                # se o ano já tiver sido apagado, reinicia o loop
                continue


    # calcula a quantidade de anos presentes em anos[]
    # subtrai-se 1 pq o ano inicial não é contado
    qt_anos = len(anos) - 1
    quinquenios = qt_anos // 5

    try:
        qt_premio = int(input(
            "Digite quantos quinquênios o servidor já tirou. Se o servidor nunca usufruiu de Licença Prêmio, digite 0 e aperte ENTER: \n"))

        # checa se a quantidade de licenças tiradas é maior do que as disponíveis
        if qt_premio <= quinquenios:
            total = (quinquenios - qt_premio)
            print("O servidor tem direito a {} quinquênio(s) = {} meses.".format(total, total * 3))
        else:
            print("O servidor ainda não completou {} quinquênios, tente novamente.".format(qt_premio))
    except ValueError:
        print("Você usou um valor não-numérico. Tente novamente.\n")

def encerramento():
    fim = input('Pressione qualquer tecla para sair...')
    pass
        
        
def relatorio():
    """Função que irá gerar um relatório da consulta realizada pronto para impressão."""

    global nome, mat, total

    # cria um arquivo .txt chamado relatório, com parâmetro de escrita, no mesmo local do arquivo .py
    # escreve no arquivo e fecha
    arq_rel = open("relatorio.txt", 'w')
    arq_rel.write("Nome do servidor: {} \n\n".format(nome))
    arq_rel.write("Matrícula: {}\n\n".format(mat))
    arq_rel.write("Quantidade de quinquenios a serem usufruidos: {}\n\n".format(total))
    arq_rel.write("Quantidade de quinquênios correspondente a {} meses\n".format(total * 3))
    arq_rel.close()


menu()
