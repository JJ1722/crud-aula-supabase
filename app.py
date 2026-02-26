import streamlit as st
from supabase import create_client, Client
import time

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]

HEADERS = {
    "apikey" : KEY,
    "Authorization" : f"Bearer {KEY}",
    "Content-Type" : "application/json"
}

supabase = Client = create_client(URL, KEY)

# Criar Registros
def add_alunos (nome, email, cidade):
    supabase.table("alunos").insert({
        "nome" : nome,
        "email" : email,
        "cidade" : cidade
    }).execute()

# Ler dados da Tabela
def get_alunos():
   resposta = supabase.table("alunos").select("*").order("nome").execute()
   return resposta.data

# Update na tabela
def update_alunos(id, nome, email, cidade):
    supabase.table("alunos").update({
        "nome": nome,
        "email": email,
        "cidade": cidade
    }).eq("id", id).execute()

# Delete
def delete_aluno(id):
    supabase.table("alunos").delete().eq("id", id).execute()

delete_aluno(12)
print(get_alunos())

# Iniciando com Streamlit
st.title("Aprendendo CRUD")

read_alunos, create_aluno = st.tabs(["Ver Alunos", "Criar Aluno"])

with read_alunos:
    alunos = get_alunos()
    if alunos:
        for x in alunos:
            st.write(f"**{x["nome"]}** -- {x["email"]} -- {x["cidade"]}")


with create_aluno:
    with st.form("nome_aluno"):
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        cidade = st.text_input("Cidade")
        if st.form_submit_button("Adicionar"):
            if nome and email:
                add_alunos(nome, email, cidade)
                st.success(f"O {nome} foi salvo com sucesso!")
                time.sleep(2)
                st.rerun()
            else:
                st.warning("Nome e email são obrigatórios")
                time.sleep(2)
                st.rerun()
