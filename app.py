import streamlit as st
from docx import Document # Importa a biblioteca para .docx
import io # Para ler o arquivo em memória

st.title("Upload e Leitura de Arquivos .docx")

uploaded_file = st.file_uploader("Escolha um arquivo .docx", type="docx")

if uploaded_file is not None:
    st.success("Arquivo enviado com sucesso!")

    # Lê o conteúdo do arquivo em memória
    bytes_data = uploaded_file.read()
    
    # Cria um objeto Documento do python-docx
    # Usamos io.BytesIO para tratar os bytes lidos como um arquivo
    document = Document(io.BytesIO(bytes_data)) 

    texto_extraido = ""
    # Itera sobre os parágrafos do documento
    for para in document.paragraphs:
        texto_extraido += para.text + "\n"
    
    st.subheader("Texto Extraído:")
    st.text_area("Conteúdo do .docx:", texto_extraido, height=300)

else:
    st.info("Por favor, faça o upload de um arquivo .docx.")