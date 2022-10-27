
def mediaAluno(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
        print(f"Aluno Aprovado! Média: {media}\nNotas: {n1}, {n2}, {n3} e {n4}")
    else:
        print(f"Aluno Reprovado! Média: {media}\nNotas: {n1}, {n2}, {n3} e {n4}")

    return media 