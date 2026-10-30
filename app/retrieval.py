
def buscar_chunk(pergunta, chunks_dic):
    palavras_pergunta = pergunta.lower().split()

    melhor_chunk = None
    maior_pontuacao = 0

    for chunk in chunks_dic.values():
        texto_chunk = chunk["text"].lower()
        pontuacao = 0

        for palavra in palavras_pergunta:
            if palavra in texto_chunk:
                pontuacao += 1

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_chunk = chunk

    return melhor_chunk
