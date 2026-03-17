def CalcularMédia(lista_alunos):
    top_media = -1
    top_nome = ""

    for nome, notas in lista_alunos:
        if notas:
            media = sum(notas) / len(notas)
            if media > top_media:
                top_media = media
                top_nome = nome

            if media < 7:
                status = "Recuperação"
            else:
                status = "Aprovado"

            print(f"Aluno: {nome}, Média: {media:.2f}, Status: {status}")

    if status == "Recuperação":
        print("Top Student:Nenhum aluno acima da média")
    else:
        print(f"Top Student: {top_nome} com média {top_media:.2f}")
