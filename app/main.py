from app.IA_ import gerar_resposta
from app.text_splitter import split_text
from app.document_loader import extract_text
from app.retrieval import buscar_chunk


def main():
    pdf_path = r"c:\Users\gutie\Downloads\Trabalho_Quimica_Elemento_Francio_Ilustrado.pdf"
    content = extract_text(pdf_path)

    print("pdf lido com sucesso")
    chunks = split_text(content)
    print(f'\ntotal de chunks: {len(chunks)}')

    chunks_dic = {
        i: {"id": i, "nome": pdf_path, "text": text}
        for i, text in enumerate(chunks)
    }

    pergunta = input('faça a pergunta:')
    resultado = buscar_chunk(pergunta, chunks_dic)

    if resultado is None:
        print("Nenhum chunk relevante encontrado.")
        return

    #print("Chunk encontrado:")
    #print(resultado["text"])
    resposta = gerar_resposta(pergunta, resultado["text"])
    print("\nResposta:")
    print(resposta)

if __name__ == "__main__":
    main()
