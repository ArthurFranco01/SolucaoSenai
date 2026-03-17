ListaAluno = []
nome = ""
numeracao = 0
while True:
    nome = str(input("Informe o nome do aluno: "))
    if nome == "0":
        break
    if not nome: 
        print("informe o nome do aluno")
    else:
        notas = []
        while True:
            nota = float(input("Informe as notas do aluno(digite (11) para finalizar): "))
            if nota == 11:
                break
            notas.append(nota)
        ListaAluno.append((nome, notas))  
        numeracao += 1
        print(f"aluno {numeracao} {ListaAluno[-1]}")
        print("digite 0 para encerrar o sistema e gerar relatório de sistema")
        print("Próximo Aluno....")
print(ListaAluno)

