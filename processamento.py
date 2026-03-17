def CalcularMédia(lista_alunos):
    top_media = -1
    top_nome = ""
    relatorio = []
    for nome, notas in lista_alunos:
        if notas:
            media = sum(notas) / len(notas)
            if media < 7:
                status = "Recuperação"
            else:
                status = "Aprovado"
            if media > top_media:
                top_media = media
                top_nome = nome

            print(f"Aluno: {nome}, Média: {media:.2f}, Status: {status}")
            relatorio.append(f"Aluno: {nome}, Média: {media:.2f}, Status: {status}")

    if top_media < 7:
        print("Top Student:Nenhum aluno acima da média")
        relatorio.append("Top Student: Nenhum aluno acima da média")
    else:
        print(f"Top Student: {top_nome} com média {top_media:.2f}")
        relatorio.append(f"Top Student: {top_nome} com média {top_media:.2f}")
    return relatorio


