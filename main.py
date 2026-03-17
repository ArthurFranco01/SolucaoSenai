from processamento import CalcularMédia
ListaAluno = []
nome = ""
numeracao = 0
while True:
    nome = str(input("Informe o nome do aluno: "))
    if nome == "0":
        break
    if nome == "": 
        print("Escreva o nome de algum aluno!!!")
    else:
        notas = []
        while True:
            nota = float(input("Informe as notas do aluno(digite (11) para finalizar): "))
            if nota == 11:
                break
            elif  nota > 10:
                print("Nota de 0 a 10.")
            else:
                notas.append(nota)
        if not notas:
            print("Deve inserir pelo menos uma nota para o aluno.")
            continue
        ListaAluno.append((nome, notas))  
        numeracao += 1
        print(f"aluno {numeracao} {ListaAluno[-1]}")
        print("digite 0 para encerrar o sistema e gerar relatório de sistema")
        print("Próximo Aluno....")
print("Sistema encerrado! Gerando relatório...")
relatorio = CalcularMédia(ListaAluno)

with open("resultado.txt", "w", encoding="utf-8") as arquivo:
    for linha in relatorio:
        arquivo.write(linha + "\n")


