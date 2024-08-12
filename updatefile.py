import os
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File

def updatefile():
    user_credentials = UserCredential(os.getenv('LOGIN'),os.getenv('SENHA'))
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
