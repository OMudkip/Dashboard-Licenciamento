import streamlit as st
import requests
import json
import time

# def trigger_workflow():
#     # Substitua por seus valores
#     repo = "/OMudkip/Dashboard-Licenciamento"
#     workflow_id = "10358164267"
#     token = "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"

#     # Construa a URL da API
#     url = f"https://api.github.com/users/OMUDKIP/repos"

from github import Github

# Substitua por seu token de acesso pessoal
token = "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"

# Criar um objeto Github
g = Github(token)

# Obter o usuário autenticado
user = g.get_user()

# Listar todos os repositórios do usuário
for repo in user.get_repos():
    print(repo.name)

# Conteúdo do arquivo (substitua por seu conteúdo)
content = "Este é o conteúdo do meu novo arquivo"

# Crie um blob
blob = repo.create_git_blob(content, "utf-8")

# Crie um tree com o blob
tree = repo.create_git_tree([
    {"path": "novo_arquivo.txt", "mode": "100644", "type": "blob", "sha": blob.sha}
])

# Obtenha a referência master (ou outra branch)
master_ref = repo.get_branch("master")
master_sha = master_ref.commit.sha

# Crie um novo commit
parent_commits = [master_sha]
commit_message = "Adicionando novo arquivo"
commit = repo.create_git_commit(commit_message, tree, parent_commits)

# Atualize a referência master
master_ref.edit(commit.sha)