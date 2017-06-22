from time import strftime

ano_atual = int(strftime("%Y"))
adm = total = 0
nome = mat = ''


def menu():
    """Função que estabelece o menu inicial do programa."""

    print("\t   CALCULADORA DE QUINQUÊNIOS - LICENÇA PRÊMIO v3.0 BETA\n\n")
    print("Calcule quantos quinquênios de licenca prêmio o servidor da SEMED tem direito.\n")
    execucao()
    relatorio()


def execucao():
    """Função que solicita admissao do servidor e retorna a quantidade de quinquenios disponiveis para análise."""

    global ano_atual, adm, nome, mat

    nome = input("Nome do servidor: ")
    mat = input("Matrícula: ")

    while True:
        try:
            adm = int(input("\nDigite o ano de admissão com 04 dígitos e aperte ENTER [ex: 1988]: \n"))
            if len(str(adm)) != 4:
                print('O ano precisa ter 04 dígitos. Exemplo: 2010 ')
                continue
            else:
                if adm > ano_atual:
                    print("Admissão posterior ao ano atual. Tente novamente.")
                    continue
                else:
                    break
        except ValueError:
            print("Você usou um valor não-numérico. Tente novamente.")

    while True:
        faltas_lic = input("O servidor possui faltas injustificadas, licenças para tratar de interesse particular ou acompanhar familiares? \
Digite 's' para 'SIM' ou 'n' para 'NÃO' e aperte ENTER: \n").lower()
        if faltas_lic == "s":
            com_imped()
            break
        elif faltas_lic == "n":
            sem_imped()
            break
        else:
            print("Opção inválida. Digite 's' para 'SIM' ou 'n' para 'NÃO':\n")
            continue


def sem_imped():
    """Função que calcula os quinquenios disponiveis para licenca de um servidor sem impedimentos\
(faltas injustificadas, licencas para tratar de interesse particular ou acompanhar familiares)."""

    global ano_atual, adm, total

    while True:
        quinq = (ano_atual - adm) // 5
        try:
            lic_tirada = int(input(
                "Digite quantos quinquênios o servidor já tirou. Se o servidor nunca usufruiu de Licença Prêmio, digite 0: \n"))
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

    anos = []
    for i in range(adm, ano_atual + 1):
        anos.append(i)

    print("Digite o ano em que o servidor possui falta, licença sem vencimento ou licença para acompanhar familiares, UM POR VEZ, e aperte ENTER.\n\
Caso a licença seja maior que um ano, colocar todos os anos de afastamento, sempre UM POR VEZ e aperte ENTER.\n\
Para parar de adicionar anos, digite SAIR e aperte ENTER\n")

    while True:
        ano_imp = input().lower()
        if ano_imp == 'sair':
            break
        else:
            ano_imp = int(ano_imp)
            if ano_imp < adm or ano_imp > ano_atual:
                print("Insira um ano válido!\n")
                continue

            if ano_imp in anos:
                pos = anos.index(ano_imp)
                del anos[pos]
            else:
                continue

    qt_anos = len(anos) - 1
    quinquenios = qt_anos // 5
    try:
        qt_premio = int(input(
            "Digite quantos quinquênios o servidor já tirou. Se o servidor nunca usufruiu de Licença Prêmio, digite 0 e aperte ENTER: \n"))
        if qt_premio <= quinquenios:
            total = (quinquenios - qt_premio)
            print("O servidor tem direito a {} quinquênio(s) = {} meses.".format(total, total * 3))
        else:
            print("O servidor ainda não completou {} quinquênios, tente novamente.".format(qt_premio))
    except ValueError:
        print("Você usou um valor não-numérico. Tente novamente.\n")


def relatorio():
    """Função que irá gerar um relatório da consulta realizada pronto para impressão."""

    global nome, mat, total

    arq_rel = open("relatorio.txt", 'w')
    arq_rel.write("Nome do servidor: {} \n\n".format(nome))
    arq_rel.write("Matrícula: {}\n\n".format(mat))
    arq_rel.write("Quantidade de quinquenios a serem usufruidos: {}\n\n".format(total))
    arq_rel.write("Quantidade de quinquênios correspondente a {} meses\n".format(total * 3))
    arq_rel.close()


menu()