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
