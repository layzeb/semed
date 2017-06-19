import time

# uso do metodo time.strftime para capturar o ano atual com 04 digitos
ano_atual = int(time.strftime("%Y"))
# inicialização do ano de admissao
adm = total =  0
nome = mat = ''


def menu():
    """Função que estabelece o menu inicial do programa."""

    print("\t\tCALCULADORA DE QUINQUENIOS - LICENCA PREMIO v2.2.1 BETA\n\n")
    print(
        "Este programa foi desenvolvido para calcular quantos quinquenios de licenca premio o servidor da SEMED/Sao "
        "Luis tem direito.\n")
    execucao()  # chamada da função execucao()
    relatorio()


def execucao():
    """Função que solicita admissao do servidor e retorna a quantidade de quinquenios disponiveis para análise."""

    # chamada das variaveis globais de ano_atual e adm para serem usadas dentro da definição da função
    global ano_atual, adm, nome, mat

    nome = input("Nome do servidor: ")
    mat = input("Matricula: ")

    # solicita ano de admissao e armazena na variavel adm
    adm = int(input("\nDigite o ano de admissao com 04 digitos e aperte ENTER [ex: 1988]: \n"))

    # checa se o ano de admissao é válido
    if adm > ano_atual:
        print("ERRO! Admissao posterior ao ano atual. Tente novamente.\n")
        adm = int(input("Digite o ano de admissao com 04 digitos e aperte ENTER [ex: 1988]: \n"))

    # iteração sobre as hipoteses de análise
    while True:

        # solicita se o servidor possui algum impedimento e armazena na variavel faltas_lic
        faltas_lic = input(
            "O servidor possui faltas injustificadas, licencas para tratar de interesse particular ou acompanhar "
            "familiares? Digite 's' para 'SIM' ou 'n' para 'NAO' e aperte ENTER: \n")
        faltas_lic = faltas_lic.lower()
        # checa se o usuario optou por 'sim', executa a função com_imped e interrompe o laço
        if faltas_lic == "s":
            com_imped()
            break

        # checa se o usuario optou por 'nao', executa a função sem_imped e interrompe o laço
        elif faltas_lic == "n":
            sem_imped()
            break

        # reinicia o loop, caso a opção escolhida seja diferente das acima
        else:
            print("Opcao invalida. Digite 's' para 'SIM' ou 'n' para 'NAO':\n")
            continue


def sem_imped():
    """Função que calcula os quinquenios disponiveis para licenca de um servidor sem impedimentos (faltas 
    injustificadas, licencas paratratar de interesse particular ou acompanhar familiares). """

    global ano_atual, adm, total

    # calcula a quantidade de quinquenios disponiveis
    quinq = (ano_atual - adm) // 5

    # recebe a quantidade de quinquenios tirados pelo servidor
    lic_tirada = int(input(
        "Digite quantos quinquenios o servidor ja tirou. Se o servidor nunca usufruiu de Licenca Premio, digite 0: "
        "\n"))

    # checa se a quantidade de licencas tiradas é maior do que as disponiveis
    if lic_tirada <= quinq:
        # calcula o total disponivel e mostra ao usuario
        total = quinq - lic_tirada
        print("O servidor tem direito a", total, "quinquenio(s) = ", total * 3, "meses.")
    else:
        print("ERRO! O servidor ainda não completou", lic_tirada, "quinquenios, tente novamente.")


def com_imped():
    global ano_atual, adm, total

    # cria uma lista que irá armazenar todos os anos analisados
    anos = []

    # itera desde o ano de admissao até o atual, incluindo cada ano na lista anos
    for i in range(adm, ano_atual + 1):
        anos.append(i)

    print(
        "Digite o ano em que o servidor possui falta, licenca sem vencimento ou licenca para acompanhar familiares, "
        "UM POR VEZ, e aperte ENTER.\nCaso a licenca seja maior que um ano, colocar todos os anos de afastamento, "
        "sempre UM POR VEZ e aperte ENTER.\nPara parar de adicionar anos, digite SAIR e aperte ENTER\n")

    while True:

        # solicita um ano em que há impedimento
        ano_imp = input().lower()
        # checa se o usuario digitou 'sair' e sai do loop
        if ano_imp == 'sair':
            break
        else:
            # transforma o tipo de ano_imp em int
            ano_imp = int(ano_imp)

            # checa se o usuario informou um ano válido
            if ano_imp < adm or ano_imp > ano_atual:
                print("ERRO! Insira um ano valido")
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
    qt_premio = int(input(
        "Digite quantos quinquenios o servidor ja tirou. Se o servidor nunca usufruiu de Licenca Premio, digite 0 e "
        "aperte ENTER: \n"))

    # checa se a quantidade de licencas tiradas é maior do que as disponiveis
    if qt_premio <= quinquenios:
        total = (quinquenios - qt_premio)
        print("O servidor tem direito a", total, "quinquenio(s) = ", total * 3, "meses.")
    else:
        print("ERRO! O servidor ainda não completou", qt_premio, "quinquenios, tente novamente.")


def relatorio():
    """Função que irá gerar um relatorio da consulta realizada pronto para impressão."""
    global nome, total, mat

    arq_rel = open("relatorio.txt", 'w')
    arq_rel.write("Nome do servidor: " + nome + '\n')
    arq_rel.write("Matricula: " + mat + '\n')
    arq_rel.write("Quantidade de quinquenios a serem usufruidos: " + str(total) + '\n')
    arq_rel.close()


menu()
