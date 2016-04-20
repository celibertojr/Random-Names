import xlrd
import random

aluno =[]

def xlread(arq_xls):
    """
    Gerador que le arquivo .xls
    """

    # Abre o arquivo
    xls = xlrd.open_workbook(arq_xls)
    # Pega a primeira planilha do arquivo
    plan = xls.sheets()[0]

    # Para i de zero ao numero de linhas da planilha
    for i in xrange(plan.nrows):
        # Le os valores nas linhas da planilha
        yield plan.row_values(i)

# captura as informacoes da tabela.
for linha in xlread('teste.xls'):
    aluno.append(linha)

#deleta cabecalho
aluno.pop(0)
#determina qual he o tamanho do arquivo.
tamanho = len(aluno)

#imprime a tabela atual
#for i in range(1, tamanho):print aluno[i]

#mistura a tabela 10 vezes. Precisa ?
for i in range(0, 9):
    random.shuffle(aluno)
#**************************

arq = open("alunosEscolhidos.txt", "w")


for i in range(0, tamanho):
    arq.write(str(aluno[i])+"\n")

arq.close
