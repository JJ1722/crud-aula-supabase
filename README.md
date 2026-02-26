# Aula CRUD Supabase

Aplicação web para aprender operações **CRUD** (Create, Read, Update, Delete) usando **Streamlit** e **Supabase**. O app gerencia um cadastro de **alunos** (nome, email, cidade) com interface em abas.

## Tecnologias

- **Python 3**
- **Streamlit** – interface web
- **Supabase** – backend (PostgreSQL) e cliente Python

## Estrutura do projeto

- `app2.py` – aplicação principal (CRUD de alunos)
- `requirements.txt` – dependências do projeto
- `.streamlit/secrets.toml` – credenciais do Supabase (não versionado)

## Pré-requisitos

1. **Python 3** instalado
2. **Conta no [Supabase](https://supabase.com)** com um projeto criado
3. No Supabase, uma tabela `alunos` com as colunas:
   - `id` (uuid, primary key, gerado automaticamente)
   - `nome` (text)
   - `email` (text)
   - `cidade` (text)

## Instalação

1. Clone o repositório e entre na pasta do projeto:

   ```bash
   cd aula-crud-supase
   ```

2. Crie um ambiente virtual (recomendado) e ative-o:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate   # Linux/macOS
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as credenciais do Supabase. Crie o arquivo `.streamlit/secrets.toml` na raiz do projeto com:

   ```toml
   SUPABASE_URL = "sua-url-do-projeto"
   SUPABASE_KEY = "sua-anon-key"
   ```

   A URL e a chave (anon/public) ficam em **Project Settings → API** no painel do Supabase. **Não commite** `secrets.toml` (ele deve estar no `.gitignore`).

## Como executar

Na raiz do projeto, com o ambiente ativado:

```bash
streamlit run app2.py
```

O app abre no navegador (geralmente em `http://localhost:8501`).

## Funcionalidades (baseado no `app2.py`)

A interface tem **quatro abas**:

| Aba | Descrição |
|-----|-----------|
| **Ver Alunos** | Lista todos os alunos (nome, email, cidade), ordenados por nome. |
| **Criar Aluno** | Formulário para cadastrar novo aluno. Nome e email são obrigatórios. |
| **Atualizar Alunos** | Seleção de um aluno e edição de nome, email e cidade. |
| **Deletar Alunos** | Seleção de um aluno e exclusão, com confirmação. |

As operações de criar, atualizar e deletar disparam uma atualização da página (`st.rerun()`) após a ação.

## Funções principais no código

- `add_alunos(nome, email, cidade)` – insere um aluno na tabela `alunos`
- `get_alunos()` – retorna todos os alunos ordenados por nome
- `update_alunos(id, nome, email, cidade)` – atualiza um aluno pelo `id`
- `delete_aluno(id)` – remove um aluno pelo `id`

A conexão com o Supabase é feita via `create_client(URL, KEY)` usando as variáveis definidas em `st.secrets`.

## Licença

Uso educacional / projeto de aula.
