a = []
"""interface  = ("Nome:","Nota1","Nota2","Nota3","Média")
print(interface)"""
for linha in range(11):
    a = a + [[0]*11]
linha = 0
while linha < 11:
    coluna = 0
    while coluna < 5:
        if coluna == 0:

            print("\n")
        a[0][0] = 'Nome: | '
        a[0][1] = 'Nota1 :'
        a[0][2] = 'Nota2 :'
        a[0][3] = 'Nota3 :'
        a[0][4] = 'Média :'
        a[1][0] = 'Júlio | '
        a[2][0] = 'Saulo | '
        a[3][0] = 'Lohan | '
        a[4][0] = 'Lucas | '
        a[5][0] = 'Pedro | '
        a[6][0] = 'Caleb | '
        a[7][0] = 'André | '
        a[8][0] = 'Jesus | '
        a[9][0] = 'David | '
        a[10][0]= 'Elias | '

        print(format(a[linha][coluna]), end = '        ')
        coluna+=1


    linha+=1
indice_linha = int(input("Digite a linha que deseja adicionar nota"))
indice_coluna = int(input("Digite a coluna que deseja adicionar nota"))
nota_adicionada = float(input("Digite a nota a ser adicionada"))
a[indice_linha][indice_coluna] = nota_adicionada
linhas_nota
a[linhas_nota][4] =
print()
linha = 0
while linha < 10:
    coluna = 0
    while coluna < 5:
        print(format(a[linha][coluna]), end = '        ')
        coluna+=1
    print()
    linha+=1
