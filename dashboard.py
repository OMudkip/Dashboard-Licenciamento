import streamlit as st
import pandas as pd
import io
import requests
import os
import plotly.graph_objects as go
import plotly.express as px
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
from github import Github
import git


local = os.getcwd()

def updatefile():
    user_credentials = UserCredential(os.environ.get('LOGIN'),os.environ.get('SENHA'))
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

    try:
        repo = git.Repo('https://github.com/OMudkip/Dashboard-Licenciamento.git')
        # Resto do seu código
    except git.exc.InvalidGitRepositoryError as e:
        print(f"Erro ao inicializar o repositório Git: {e}")
        print("Verifique se o caminho do repositório está correto e se o repositório existe.")
    except PermissionError as e:
        print(f"Você não tem permissão para acessar o repositório: {e}")

    # Adicionar o arquivo ao índice
    file_path = local_file.name

    # Adicionar o caminho do arquivo ao índice
    repo.index.add([file_path])


    # Commitar as mudanças
    commit_message = f"Adicionando arquivo baixado do SharePoint: {file}"
    repo.index.commit(commit_message)
    print(f"Arquivo adicionado e commitado no repositório local com mensagem: {commit_message}")

    # Autenticar com o GitHub
    g = Github(os.environ.get('GIT_KEY'))

    # Obter o repositório remoto
    remote_url = "https://github.com/OMudkip/Dashboard-Licenciamento"  # Substitua com seu URL
    origin = repo.remote(name="origin")

    # Verificar se a origem (remote) já está configurada
    if origin.url != remote_url:
      # Configurar a origem (remote) do repositório
      origin.set_url(remote_url)
    try:
        origin.pull()
    except:
        print('Não foi possivel dar Pull no repositório.')
    # Empurrar alterações para o GitHub
    origin.push()
    print("Alterações enviadas para o repositório remoto!")


st.set_page_config(layout='wide')
st.markdown("""<style>
    [data-testid="stDecoration"] {
		background-image: linear-gradient(90deg, rgb(0, 102, 204), rgb(102, 255, 255));
	}
    .metric-total {
        color: rgb(232, 1, 0);
    }

</style>""", unsafe_allow_html=True)

contratos_a_excluir = ['12061-63678','31369-64551','46185-57281','48082-39389','64382-87123','83945-04574','19263-91577','22852-58393','25326-33073','84654-96518','17370-45363','59844-82659','82175-06872']

df = pd.read_excel('ContratosTotais.xlsx', engine='openpyxl')
for line in df.index:
    linhacontrato = df.loc[line, 'Contrato']
    if linhacontrato in contratos_a_excluir:
        df = df.drop(index=line)

# Agrupando os dados por contrato, aplicação e status





for line in df.index:
    minhalinha = df.loc[line, 'Contrato']
    if minhalinha == '17280-90655':
        # df_nomes_contratos.replace(minhalinha,'Projeto Sergipe (EPD-SE)')
        df.loc[line, 'Contrato'] = 'Projeto Sergipe (EPD-SE)'  
    elif minhalinha == '93060-97373':
        # df_nomes_contratos.replace(minhalinha,'Projeto Acre (ATO-AC)')
        df.loc[line, 'Contrato'] = 'Acre (ATO-AC)'
    elif minhalinha == '25247-87908':
        # df_nomes_contratos.replace(minhalinha,'Projeto Minas Gerais (EPD-MG)')
        df.loc[line, 'Contrato'] = 'Minas Gerais (EPD-MG)'
    elif minhalinha == '36794-91345':
        # df_nomes_contratos.replace(minhalinha,'Projeto Paraíba (EPD-PB)')
        df.loc[line, 'Contrato'] = 'Paraíba (EPD-PB)'
    elif minhalinha == '70693-79727':
        # df_nomes_contratos.replace(minhalinha,'Cemig Triângulo (CEMIG-TRI) - SHP2KML')
        df.loc[line, 'Contrato'] = 'Cemig Triângulo (CEMIG-TRI) - SHP2KML'
    elif minhalinha == '94334-36647':
        # df_nomes_contratos.replace(minhalinha,'Projeto Minas Gerais/NF (EPD-MG/NF)')
        df.loc[line, 'Contrato'] = 'Minas Gerais/NF (EPD-MG/NF)'
    elif minhalinha == '87598-92211':
        # df_nomes_contratos.replace(minhalinha,'Projeto Rondônia - Cadastro (EPD-RO)')
        df.loc[line, 'Contrato'] = 'Rondônia - Cadastro (EPD-RO)'
    elif minhalinha == '18056-95304':
        # df_nomes_contratos.replace(minhalinha,'Projeto Mato Grosso (EPD-MT)')
        df.loc[line, 'Contrato'] = 'Mato Grosso (EPD-MT)'
    elif minhalinha == '21377-66091':
        # df_nomes_contratos.replace(minhalinha,'Projeto Minas Gerais - Divinópolis 2 (EPD-DIV-2)')
        df.loc[line, 'Contrato'] = 'Minas Gerais - Divinópolis 2 (EPD-DIV-2)'
    elif minhalinha == '33069-94214':
        # df_nomes_contratos.replace(minhalinha,'Projeto Rondônia - Projeto (EPD-RO)')
        df.loc[line, 'Contrato'] = 'Rondônia - Projeto (EPD-RO)'
    elif minhalinha == '34865-58679':
        # df_nomes_contratos.replace(minhalinha,'Projeto Mato Grosso do Sul (EPD-MS)' )
        df.loc[line, 'Contrato'] = 'Mato Grosso do Sul (EPD-MS)'  
    elif minhalinha == '59844-82659':
        # df_nomes_contratos.replace(minhalinha,'Sync EPD-SS')
        df.loc[line, 'Contrato'] = 'Sync EPD-SS'
    elif minhalinha == '74772-21252':
        # df_nomes_contratos.replace(minhalinha,'Projeto Cemig')
        df.loc[line, 'Contrato'] = 'Cemig'
    elif minhalinha == '80261-05621':
        # df_nomes_contratos.replace(minhalinha,'Projeto Sul/Sudeste (EPD-SS)')
        df.loc[line, 'Contrato'] = 'Sul/Sudeste (EPD-SS)'

df_agrupado_sem_status = df.groupby(['Contrato', 'Aplicação']).size().reset_index(name='Quantidade')
df_agrupado = df.groupby(['Contrato', 'Aplicação', 'Status']).size().reset_index(name='Quantidade')



# Cria um seletor para escolher o contrato
st.sidebar.image('logosoftwares.png')
st.sidebar.markdown(f"<h1 style='text-align: left; color: white;'>Gerenciamento de Licenças</h1>", unsafe_allow_html=True)
contrato_selecionado = st.sidebar.multiselect('Selecione um contrato', df['Contrato'].unique())


if contrato_selecionado == ['17280-90655']:
    projeto = 'Projeto Sergipe (EPD-SE)'  
elif contrato_selecionado == ['93060-97373']:
    projeto = 'Projeto Acre (ATO-AC)'
elif contrato_selecionado == ['25247-87908']:
    projeto = 'Projeto Minas Gerais (EPD-MG)'
elif contrato_selecionado == ['36794-91345']:
    projeto = 'Projeto Paraíba (EPD-PB)'
elif contrato_selecionado == ['70693-79727']:
    projeto = 'Cemig Triângulo (CEMIG-TRI) - SHP2KML'
elif contrato_selecionado == ['94334-36647']:
    projeto = 'Projeto Minas Gerais/NF (EPD-MG/NF)'
elif contrato_selecionado == ['87598-92211']:
    projeto = 'Projeto Rondônia - Cadastro (EPD-RO)'
elif contrato_selecionado == ['18056-95304']:
    projeto = 'Projeto Mato Grosso (EPD-MT)'
elif contrato_selecionado == ['21377-66091']:
    projeto = 'Projeto Minas Gerais - Divinópolis 2 (EPD-DIV-2)'
elif contrato_selecionado == ['33069-94214']:
    projeto = 'Projeto Rondônia - Projeto (EPD-RO)'
elif contrato_selecionado == ['34865-58679']:
    projeto = 'Projeto Mato Grosso do Sul (EPD-MS)'  
elif contrato_selecionado == ['59844-82659']:
    projeto = 'Sync EPD-SS'
elif contrato_selecionado == ['74772-21252']:
    projeto = 'Projeto Cemig'
elif contrato_selecionado == ['80261-05621']:
    projeto = 'Projeto Sul/Sudeste (EPD-SS)'
else:
    projeto = 'Quantitativo de Licenças'
coluna1, coluna2 = st.columns([8,1])
with coluna2:
    botao = st.button("Atualizar base")
    if botao:
        updatefile()
with coluna1:
    st.markdown(f"<h1 style='text-align: center; color: white;'>{projeto}</h1>", unsafe_allow_html=True)
    st.markdown('')
    st.markdown('')
# if botao:
#     updatefile()


df_filtrado = df_agrupado_sem_status[df_agrupado_sem_status['Contrato'].isin(contrato_selecionado)]


# Filtra os dados para o contrato selecionado


# Agrupando os dados por contrato
df_total_por_contrato = df_agrupado.groupby('Contrato')['Quantidade'].sum().reset_index()
# df_nomes_contratos = df_agrupado.groupby('Contrato')['Quantidade'].sum().reset_index()



for line in df_total_por_contrato.index:
    minhalinha = df_total_por_contrato.loc[line, 'Contrato']
    if minhalinha == '17280-90655':
        # df_nomes_contratos.replace(minhalinha,'Projeto Sergipe (EPD-SE)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Projeto Sergipe (EPD-SE)'  
    elif minhalinha == '93060-97373':
        # df_nomes_contratos.replace(minhalinha,'Projeto Acre (ATO-AC)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Acre (ATO-AC)'
    elif minhalinha == '25247-87908':
        # df_nomes_contratos.replace(minhalinha,'Projeto Minas Gerais (EPD-MG)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Minas Gerais (EPD-MG)'
    elif minhalinha == '36794-91345':
        # df_nomes_contratos.replace(minhalinha,'Projeto Paraíba (EPD-PB)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Paraíba (EPD-PB)'
    elif minhalinha == '70693-79727':
        # df_nomes_contratos.replace(minhalinha,'Cemig Triângulo (CEMIG-TRI) - SHP2KML')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Cemig Triângulo (CEMIG-TRI) - SHP2KML'
    elif minhalinha == '94334-36647':
        # df_nomes_contratos.replace(minhalinha,'Projeto Minas Gerais/NF (EPD-MG/NF)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Minas Gerais/NF (EPD-MG/NF)'
    elif minhalinha == '87598-92211':
        # df_nomes_contratos.replace(minhalinha,'Projeto Rondônia - Cadastro (EPD-RO)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Rondônia - Cadastro (EPD-RO)'
    elif minhalinha == '18056-95304':
        # df_nomes_contratos.replace(minhalinha,'Projeto Mato Grosso (EPD-MT)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Mato Grosso (EPD-MT)'
    elif minhalinha == '21377-66091':
        # df_nomes_contratos.replace(minhalinha,'Projeto Minas Gerais - Divinópolis 2 (EPD-DIV-2)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Minas Gerais - Divinópolis 2 (EPD-DIV-2)'
    elif minhalinha == '33069-94214':
        # df_nomes_contratos.replace(minhalinha,'Projeto Rondônia - Projeto (EPD-RO)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Rondônia - Projeto (EPD-RO)'
    elif minhalinha == '34865-58679':
        # df_nomes_contratos.replace(minhalinha,'Projeto Mato Grosso do Sul (EPD-MS)' )
        df_total_por_contrato.loc[line, 'Contrato'] = 'Mato Grosso do Sul (EPD-MS)'  
    elif minhalinha == '59844-82659':
        # df_nomes_contratos.replace(minhalinha,'Sync EPD-SS')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Sync EPD-SS'
    elif minhalinha == '74772-21252':
        # df_nomes_contratos.replace(minhalinha,'Projeto Cemig')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Cemig'
    elif minhalinha == '80261-05621':
        # df_nomes_contratos.replace(minhalinha,'Projeto Sul/Sudeste (EPD-SS)')
        df_total_por_contrato.loc[line, 'Contrato'] = 'Sul/Sudeste (EPD-SS)'



# Agrupando os dados por projeto e somando a quantidade de licenças
df_por_projeto = df_agrupado.groupby('Contrato')['Quantidade'].sum().reset_index()


def get_total_licenças(contrato):
    # Filtra o DataFrame para os contratos selecionados
    df_filtrado = df_total_por_contrato[df_total_por_contrato['Contrato'].isin(contrato)]
    # Soma a quantidade de licenças para todos os contratos filtrados
    return df_filtrado['Quantidade'].sum()

def get_total_licenças_por_status(contratos, status):
    df_filtrado = df_agrupado.query("Contrato in @contratos and Status == @status")
    return df_filtrado['Quantidade'].sum()

# Calculando o total de licenças ativas e inativas
total_ativas = get_total_licenças_por_status(contrato_selecionado, 'Ativo')
total_inativas = get_total_licenças_por_status(contrato_selecionado, 'Inativo')
total_licenças = get_total_licenças(contrato_selecionado)

coltotal, colativa, colinativa = st.columns([2,2,3])
with coltotal:
     st.metric(label="Total de Licenças", value=total_licenças)
with colativa:
    st.metric(label="Total de Licenças Ativas", value=total_ativas)
with colinativa:
    st.metric(label="Total de Licenças Inativas", value=total_inativas)
    

tab1, tab2 = st.tabs(["Análise por Contrato","Quantitativo Geral"])

with tab1:
    st.subheader("Detalhes das Licenças")
    col1, col2, col3 = st.columns([2,2,3])
    
    with col1:
        # Cria o gráfico de pizza
        fig1 = px.pie(df_filtrado, values='Quantidade', names='Aplicação',title=f'Distribuição de Aplicativos',color='Aplicação',color_discrete_sequence=px.colors.cmocean.curl)
        # Exibe o gráfico
        st.plotly_chart(fig1)
        


    with col3:
        
        # Cria o gráfico de barras
        fig = px.bar(df_filtrado, x='Aplicação', y='Quantidade',labels={'Aplicação': 'Aplicação', 'Quantidade': 'Quantidade de Licenças'},barmode='relative',color='Contrato',title=f'Quantidade de Licenças por Contrato',color_discrete_sequence=px.colors.carto.Blugrn_r)
        # Exibe o gráfico
        st.plotly_chart(fig)

    df_filtrado_licencas = df[df['Contrato'].isin(contrato_selecionado)]
    st.dataframe(df_filtrado_licencas)

with tab2:
    st.subheader("Detalhes das Licenças")
    tab2colum1, tab2colum2 = st.columns([1, 2])
    with tab2colum1:
        st.dataframe(df_total_por_contrato)
        output = io.BytesIO()
        # Escrever o DataFrame para o buffer
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df_total_por_contrato.to_excel(writer, index=False)

        # Voltar para o início do buffer
        output.seek(0)
        st.download_button(data=output.read(),label='Baixar Dados',file_name='Quantitativo Geral.xlsx',mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    with tab2colum2:
        fig = px.bar(df_total_por_contrato, x='Contrato', y='Quantidade',labels={'Contrato': 'Contratos', 'Quantidade': 'Quantidade de Licenças'},color='Contrato',title='Comparativo de Licenças por Projeto',color_discrete_sequence=px.colors.carto.Bluyl)
        st.plotly_chart(fig)
    
    
print(df_total_por_contrato)





