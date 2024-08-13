import os
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
from git import Repo
from github import Github


def updatefile():
    user_credentials = UserCredential("engeselt.projetos@engeselt.onmicrosoft.com","Massachusetts#PBI")
    ctx = ClientContext('https://engeselt.sharepoint.com/sites/Inovaesdeprocessos/Shared%20Documents/AUTOMAÇÃO%20DE%20PROCESSOS/Dashboard%20Licenciamento/ContratosTotais.xlsx').with_credentials(user_credentials)

    file_name = ('ContratosTotais.xlsx')
    with open(os.path.join(file_name), "wb") as local_file:
        file = (
            File.from_url('https://engeselt.sharepoint.com/sites/Inovaesdeprocessos/Shared%20Documents/AUTOMAÇÃO%20DE%20PROCESSOS/Dashboard%20Licenciamento/ContratosTotais.xlsx')
            .with_credentials(user_credentials)
            .download(local_file)
            .execute_query()
        )
    print("Arquivo baixado")

    repo = Repo("https://api.github.com/users/OMudkip/Dashboard-Licenciamento")

    # Adicionar o arquivo ao índice
    repo.index.add([local_file])

    # Commitar as mudanças
    commit_message = f"Adicionando arquivo baixado do SharePoint: {file}"
    repo.index.commit(commit_message)
    print(f"Arquivo adicionado e commitado no repositório local com mensagem: {commit_message}")

    # Autenticar com o GitHub
    g = Github("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")

    # Obter o repositório remoto
    remote_url = "git@github.com:OMudkip/Dashboard-Licenciamento.git"  # Substitua com seu URL
    origin = repo.remote(name="origin")

    # Verificar se a origem (remote) já está configurada
    if origin.url != remote_url:
      # Configurar a origem (remote) do repositório
      origin.set_url(remote_url)

    # Puxar alterações (opcional)
    origin.pull()

    # Empurrar alterações para o GitHub
    origin.push()
    print("Alterações enviadas para o repositório remoto!")

updatefile()
