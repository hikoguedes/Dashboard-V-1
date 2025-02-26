import os
import csv
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import io  # Para manipulação de dados em formato de bytes
import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# import plotly.express as px
# import plotly.graph_objects as go
# import plotly.io as pio
import locale
import altair as alt
import matplotlib.ticker as mticker
import pygsheets


# Configuração do layout
st.set_page_config(layout="wide")
# Lendo o arquivo XLSX

#credenciais = pygsheets.authorize(service_file="Kempisnki-chave.json") 
#ArquivoKempinskiGoogleSheets = 



# URL compartilhada do OneDrive/SharePoint
#url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA1MjkyMzMifQ.PiGt_QWGY8WlbaJsYlr439vokYU_QJLC6PrKZ6bm8vJ3INjtofuwUce6FYwicUkmX4NV1zY6IVU2y_iyHUJKBzCI5KEGsjRerLOO6-0C0IDhS3b36YPRWLqeL9JWqyfSNefMfj5m5pWZ0ZXP3tt7ARdZzeTuFiRxUWKCDDytelbLcyF2kxURBnZTdyGd8mZYITI-EcBYn8c57OH4QZIZhtJ0UZNvYSZ47Ejqndiu6XGrR-9x67PLcPKZJGiCQcwmGSvQt_6hZvP8xLAlEeS6G3M_e7a7pQ0nahX_YgCl4s0Rv7o3Wt3RlUcaJESJh45bC_OEoVb319VoFXKFP079dsnZkhKhL9cd42mlvpY2N9KMoyhDeev6I2afX4mf7r8P-N9Yd68dbYqJGtphRVkw8w.lCXl9JPJrmetVmAR8BsrlEZSHrQNPLLeCeBYpI-XaW4&ApiVersion=2.0"
url = "https://my.microsoftpersonalcontent.com/personal/9b2376debd26f163/_layouts/15/download.aspx?UniqueId=bd26f163-76de-2023-809b-750000000000&Translate=false&tempauth=v1e.eyJzaXRlaWQiOiJlNDc5ZWIzOS01NDYxLTQ0NjEtODIxMy1hMjg5NjY4YWQ2MGMiLCJhcHBfZGlzcGxheW5hbWUiOiJPREMgQ29uc3VtZXIiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3NDA1NzczMTcifQ.I4JXk2odmnYrajfe31XhbahQG1o_W-A8wVDL_y1BYpE6aksinQqRT2chhuH1SsqqXBvOe9nuFfaNjZfOesMzKbIy8xPkMK771Jl3cEt3-8Q7dt4UmBX1IOa2z6VEyPszPHz9tgkGD4spVldbrll31_OIs4v1_ubMQ1Kdg0ZNhOAIIjiHPn4V0ef_3z2JoF4pg58rK6thfkPIXjqOWH2_OuqWAU_kfLXPFhCsgnxbQkpApmHIQ8R3ygPCHcK3YbFR99yGqINcZ6KGvGcQAOGXggEewHP--TXE3-LWOcth2M7PS8BPxUcsjW98syhrZuczRy91_Q7rbqQCcse315vfM87TsrmHCbEuxuSiNn7pFEzIdu7xHhlODn3XGZMk7YkczgC7kd_tQMPmyvaInRNEfQ.aZBPjVRLEUyw_RsZ77QA9cOwU5klY-rDI4ttsZpBQNY&ApiVersion=2.0"
# Função para carregar o arquivo Excel
try:
    # Nome da aba sem espaços extras
    df = pd.read_excel(url, sheet_name="Consulta Contratos", engine="openpyxl")
    st.write("✅ Dados da Planilha:")
    st.dataframe(df)
except Exception as e:
    st.error(f"🚫 Erro ao carregar o arquivo: {e}")




#
# 🔹 CAMINHO LOCAL OU LINK



# Initialize all variables with default values
def initialize_variables():
    return {
        # Sales and Status Variables
        'total_valor_vendido_sem_cancelado': 0,
        'total_desconto_financeiro_sem_cancelado': 0,
        'valor_final': 0,
        'quant_assinado': 0,
        'quant_nao_assinado': 0,
        'df_vendas_agrupadas':0,
        
        # Purchase Latency Variables
        'media_latencia_compra': 0,
        'media_latencia_compra_arredondada': 0,
        
        # Table Type Quantities and Percentages
        'quant_a_vista': 0,
        'percent_a_vista': 0,
        'quant_curta': 0,
        'percent_curta': 0,
        'quant_longa': 0,
        'percent_longa': 0,
        'quant_longuissima': 0,
        'percent_longuissima': 0,
        
        # Monthly Analysis Variables
        'ultima_variacao': '➡️',
        'ultimo_valor': 0,
        'ultimo_ano': 'Sem Dados',
        'ultimo_mes': 'Sem Dados',
        
        # Financial Metrics
        'total_valor_vendido_filtrado': 0,
        'total_clientes_filtrado': 0,
        'ticket_medio_filtrado': 0,
        'total_follow_ups': 0,
        'total_entrada': 0,
        'percent_entrada': 0,
        
        # Unit Type Variables
        'quant_integral': 0,
        'percent_integral': 0,
        'quant_4_semanas': 0,
        'percent_4_semanas': 0,
        'quant_6_semanas': 0,
        'percent_6_semanas': 0,
        'quant_13_semanas': 0,
        'percent_13_semanas': 0,
        
        # Discount Variables
        'total_desconto_financeiro': 0,
        'percent_desconto_financeiro': 0,
        'total_desconto_viabilidade': 0,
        'percent_desconto_viabilidade': 0,
        'total_ganho_viabilidade': 0,
        'percent_ganho_viabilidade': 0,
        
        # Client Variables
        'total_clientes': 0,
        
        # Formatted Values
        'total_desconto_financeiro_formatado': "R$ 0,00",
        'total_desconto_viabilidade_formatado': "R$ 0,00",
        'total_ganho_viabilidade_formatado': "R$ 0,00"
    }

# Initialize variables at the start of your script
vars = initialize_variables()


# After your imports...

# Initialize variables
vars = initialize_variables()

# ============================


# ✅ Caminho do arquivo (CSV ou XLSX)
#caminho_arquivo = r"BASERESGATE.xlsx"  # Altere o caminho aqui

# ============================
# 🔹 EXECUÇÃO
# ============================
#df = load_data(caminho_arquivo)

# ============================
# 🔹 EXIBIR O DATAFRAME
# ============================
#if not df.empty:
 #   st.title("📊")
    # st.dataframe(df)
#else:
#    st.error("⚠️ Não foi possível carregar o DataFrame. Verifique o arquivo.")

# Botão para recarregar
if st.button("🔄 Recarregar"):
    st.experimental_rerun()


# Criando o sidebar de navegação
st.sidebar.title('Navegação')
pagina = st.sidebar.radio('Selecione a página:', [
    'HOME',
    'RANKING',
    'Origens_Estados',
    'GRÁFICOS VIABILIDADE',
    'GRÁFICOS TABELA',
    'GRÁFICOS DISTRATOS',
    'Previsão de Vendas',
    'Simulador'
])

# Criando seção de filtros no sidebar
st.sidebar.title('Filtros')

# Convertendo a coluna 'Data da Venda' para datetime
df['Data da Venda'] = pd.to_datetime(df['Data da Venda'], errors='coerce')

# Determinando o primeiro e o último dia de venda
# Definindo limite inferior para 2020
data_inicio_min = pd.to_datetime('2020-01-01').date()
# Definindo limite superior para 2027
data_fim_max = pd.to_datetime('2027-12-31').date()

# Valores padrão para o filtro (pode ser ajustado conforme necessidade)
data_inicio_padrao = pd.to_datetime('2021-01-01').date()
data_fim_padrao = pd.to_datetime('2025-12-31').date()

# Filtro de data com os novos limites
data_inicio = st.sidebar.date_input(
    'Data da Venda - Início',
    min_value=data_inicio_min,
    max_value=data_fim_max,
    value=data_inicio_padrao
)

data_fim = st.sidebar.date_input(
    'Data da Venda - Fim',
    min_value=data_inicio_min,
    max_value=data_fim_max,
    value=data_fim_padrao
)

# Filtrando o DataFrame com as datas selecionadas
df_filtrado = df[(df['Data da Venda'].dt.date >= data_inicio)
                 & (df['Data da Venda'].dt.date <= data_fim)]

# Demais filtros
gerente = st.sidebar.selectbox(
    'GERENTE', ['Todos'] + list(df['GERENTE'].unique()))
corretor1 = st.sidebar.selectbox(
    'Corretor 1', ['Todos'] + list(df['Corretor 1'].unique()))
corretor2 = st.sidebar.selectbox(
    'Corretor 2', ['Todos'] + list(df['Corretor 2'].unique()))
produto = st.sidebar.selectbox(
    'PRODUTO', ['Todos'] + list(df['PRODUTO'].unique()))
uf = st.sidebar.selectbox('UF', ['Todos'] + list(df['UF'].unique()))
origem_venda = st.sidebar.selectbox(
    'Origem da venda', ['Todos'] + list(df['Origem da venda'].unique()))
campanha = st.sidebar.selectbox(
    'Campanha', ['Todos'] + list(df['Campanha'].unique()))
status1 = st.sidebar.selectbox(
    'Status 1', ['Todos'] + list(df['Status 1'].unique()))
status2 = st.sidebar.selectbox(
    'Status 2', ['Todos'] + list(df['Status 2'].unique()))
tipo_unidade = st.sidebar.selectbox('Tipo unidade (semanas)', [
                                    'Todos'] + list(df['Tipo unidade semanas'].unique()))

# Aplicando os filtros
df_filtrado = df.copy()

# Filtro de data
mask_data = (df_filtrado['Data da Venda'].dt.date >= data_inicio) & (
    df_filtrado['Data da Venda'].dt.date <= data_fim)
df_filtrado = df_filtrado[mask_data]

if gerente != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['GERENTE'] == gerente]
if corretor1 != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Corretor 1'] == corretor1]
if corretor2 != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Corretor 2'] == corretor2]
if produto != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['PRODUTO'] == produto]
if uf != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['UF'] == uf]
if origem_venda != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Origem da venda'] == origem_venda]
if campanha != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Campanha'] == campanha]
if status1 != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Status 1'] == status1]
if status2 != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Status 2'] == status2]
if tipo_unidade != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas']
                              == tipo_unidade]


# ============================ HOME ============================
if pagina == 'HOME':
    st.title('🏠 Página Home')
    if not df_filtrado.empty:
        st.write("### Análise de Valores Vendidos")
        #st.write(df_filtrado)

        ####################################### BEGIN HOME############################################################
        ####################################################################################################
        # Calculando o total das vendas

        # Filtrar somente os valores "Assinado" na coluna "Status 1"
        df_assinado = df_filtrado[df_filtrado['Status 1'] == 'ASSINADO']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_assinado = df_assinado.shape[0]

        # Filtrando os dados para excluir as linhas com 'CANCELADO' em "Status 2"
        df_filtrado_sem_cancelado = df_filtrado[df_filtrado['Status 2'] != 'CANCELADO']

        # Calculando o total da coluna "Valor vendido" sem os "CANCELADO"
        total_valor_vendido_sem_cancelado = df_filtrado_sem_cancelado['Valor vendido'].sum(
        )

#___________________________________________________________________________________



        # Converter a coluna "Desconto Financeiro" para numérico, substituindo erros por NaN
        df_filtrado_sem_cancelado['Desconto Financeiro'] = pd.to_numeric(
            df_filtrado_sem_cancelado['Desconto Financeiro'], errors='coerce'
        )

        # Substituir NaN por 0 para evitar erro na soma
        df_filtrado_sem_cancelado['Desconto Financeiro'].fillna(0, inplace=True)

        # Agora podemos calcular a soma sem erro
        total_desconto_financeiro_sem_cancelado = df_filtrado_sem_cancelado['Desconto Financeiro'].sum()

        # Exibir o resultado no Streamlit
        #st.write(f"💰 Total de Desconto Financeiro (sem cancelados): R$ {total_desconto_financeiro_sem_cancelado:,.2f}")


#___________________________________________________________________________________

        # Calculando o valor final descontando o "Desconto Financeiro"
        valor_final = total_valor_vendido_sem_cancelado - \
            total_desconto_financeiro_sem_cancelado

        # _________________________________________________________________________________________#

        df_nao_assinado = df_filtrado[df_filtrado['Status 1']
                                      == 'NAO ASSINADO']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_nao_assinado = df_nao_assinado.shape[0]

        # _________________________________________________________________________________________#

        # Filtrar os valores válidos de "Latencia de compra" (remover valores nulos ou inválidos)
        latencia_compra = df_filtrado['Latencia de compra'].dropna()

        # Calcular a média e arredondar
        media_latencia_compra = latencia_compra.mean()

        media_latencia_compra_arredondada = round(
            np.nan_to_num(media_latencia_compra, nan=0))

        # Criar o histograma
        fig, ax = plt.subplots(figsize=(6, 4))  # Tamanho do gráfico ajustado
        plt.hist(latencia_compra, bins=30, color='blue', edgecolor='black')
        plt.title('Distribuição da Latencia de compra')
        plt.xlabel('Latencia de compra (dias)')
        plt.ylabel('Frequência')
        plt.grid(True)

        # Salvar o gráfico em uma imagem
        buf = io.BytesIO()  # Agora 'io' está importado
        fig.savefig(buf, format="png")
        buf.seek(0)

        # _________________________________________________________________________________________#

        df_a_vista = df_filtrado[df_filtrado['Tabela'] == 'A vista']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_a_vista = df_a_vista.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_a_vista = round((quant_a_vista / total_registros) * 100)
        percent_a_vista = round(
            (quant_a_vista / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        df_curta = df_filtrado[df_filtrado['Tabela'] == 'Curta']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_curta = df_curta.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_curta = round((quant_curta / total_registros) * 100)
        percent_curta = round((quant_curta / total_registros)
                              * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        df_longa = df_filtrado[df_filtrado['Tabela'] == 'Longa']
        df_longa = df_filtrado[df_filtrado['Tabela'] == 'Longa']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_longa = df_longa.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_longa = round((quant_longa / total_registros) * 100)
        percent_longa = round((quant_longa / total_registros)
                              * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        df_longuissima = df_filtrado[df_filtrado['Tabela'] == 'Longuissima']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        df_longuissima = df_filtrado[df_filtrado['Tabela'] == 'Longuissima']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_longuissima = df_longuissima.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_longuissima = round((quant_longuissima / total_registros) * 100)
        percent_longuissima = round(
            (quant_longuissima / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        df_filtrado['Data da Venda'] = pd.to_datetime(
            df_filtrado['Data da Venda'])

        # 1️⃣ Criar colunas para Ano e Mês
        df_filtrado['Ano'] = df_filtrado['Data da Venda'].dt.year
        df_filtrado['Mês'] = df_filtrado['Data da Venda'].dt.month

        # 2️⃣ Agrupar por Ano e Mês para calcular o total de vendas
        total_por_mes = df_filtrado.groupby(
            ['Ano', 'Mês'])['Valor vendido'].sum().reset_index()

        # 3️⃣ Ordenar os dados por Ano e Mês
        total_por_mes = total_por_mes.sort_values(
            ['Ano', 'Mês']).reset_index(drop=True)

        # 4️⃣ Calcular a variação percentual mês a mês
        total_por_mes['Variação (%)'] = total_por_mes['Valor vendido'].pct_change(
        ) * 100  # Em percentual

        # Adicionar coluna de setas com códigos HTML para cor
        def definir_seta_colorida(variacao):
            if pd.isna(variacao):
                return '<span style="color:gray; font-size:25px;">➡️</span>'  # Estabilidade inicial
            elif variacao > 0:
                return '<span style="color:green; font-size:25px;">⬆️</span>'  # Crescimento
            elif variacao < 0:
                return '<span style="color:red; font-size:25px;">⬇️</span>'    # Queda
            else:
                return '<span style="color:gray; font-size:25px;">➡️</span>'  # Estabilidade

        total_por_mes['Seta'] = total_por_mes['Variação (%)'].apply(
            definir_seta_colorida)

        # 6️⃣ Converter o número do mês para nome
        total_por_mes['Mês Nome'] = total_por_mes['Mês'].apply(
            lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))

        # 7️⃣ Valores para o Cartão
        valor_final = df_filtrado['Valor vendido'].sum()  # VGV Bruto
        quant_assinado = df_filtrado.shape[0]  # Total de assinados

        # Últimos dados para o cartão
        if not total_por_mes.empty:
            ultima_variacao = total_por_mes.iloc[-1]['Seta']
            ultimo_valor = total_por_mes.iloc[-1]['Valor vendido']
            ultimo_ano = total_por_mes.iloc[-1]['Ano']
            ultimo_mes = total_por_mes.iloc[-1]['Mês Nome']
        else:
            # Valores padrão em caso de DataFrame vazio
            ultima_variacao = '➡️'
            ultimo_valor = 0
            ultimo_ano = 'Sem Dados'
            ultimo_mes = 'Sem Dados'

            # ____
            # _____________________________________________________________________________________#

            # Converter colunas para numérico e tratar valores ausentes no DataFrame filtrado
        df_filtrado['Valor vendido'] = pd.to_numeric(
            df_filtrado['Valor vendido'], errors='coerce')
        df_filtrado['# Clientes'] = pd.to_numeric(
            df_filtrado['# Clientes'], errors='coerce')

        # Calcular o Ticket Médio usando o DataFrame filtrado
        total_valor_vendido_filtrado = df_filtrado['Valor vendido'].sum()
        total_clientes_filtrado = df_filtrado['# Clientes'].sum()

        # Evitar divisão por zero
        if total_clientes_filtrado != 0:
            ticket_medio_filtrado = total_valor_vendido_filtrado / total_clientes_filtrado
        else:
            ticket_medio_filtrado = 0

            # _____________________________________________________________________________________#

            # Converter a coluna 'N de FU' para numérico no DataFrame filtrado
        df_filtrado['N de FU'] = pd.to_numeric(
            df_filtrado['N de FU'], errors='coerce')

        # Calcular o total de Follow-ups (ignorando valores nulos)
        total_follow_ups = df_filtrado['N de FU'].sum()

        # Remover casas decimais usando int()
        total_follow_ups = int(total_follow_ups)

        # _____________________________________________________________________________________#

        # _____________________________________________________________________________________#

        # Converter a coluna 'N de FU' para numérico no DataFrame filtrado
        df_filtrado['% De Entrada'] = pd.to_numeric(
            df_filtrado['% De Entrada'], errors='coerce')

        # Calcular o total de Follow-ups (ignorando valores nulos)
        total_entrada = df_filtrado['% De Entrada'].sum()

        # Remover casas decimais usando int()
        total_entrada = int(total_entrada)

        percent_entrada = round((total_entrada / total_valor_vendido_sem_cancelado)
                                * 100) if total_valor_vendido_sem_cancelado != 0 else 0

        # _____________________________________________________________________________________#
        # _________________________________________________________________________________________#

        df_integral = df_filtrado[df_filtrado['Tipo unidade semanas'] == 'Integral']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_integral = df_integral.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_a_vista = round((quant_a_vista / total_registros) * 100)
        percent_integral = round(
            (quant_integral / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        # Normalizando os dados para garantir que o filtro funcione
        df_filtrado['Tipo unidade semanas'] = df_filtrado['Tipo unidade semanas'].astype(
            str).str.strip()

        # Agora filtra
        df_4_semanas = df_filtrado[df_filtrado['Tipo unidade semanas'] == '4']
        quant_4_semanas = df_4_semanas.shape[0]
        total_registros = df_filtrado.shape[0]
        percent_4_semanas = round(
            (quant_4_semanas / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        # _________________________________________________________________________________________#

        # Normalizando os dados para garantir que o filtro funcione
        df_filtrado['Tipo unidade semanas'] = df_filtrado['Tipo unidade semanas'].astype(
            str).str.strip()

        # Agora filtra
        df_6_semanas = df_filtrado[df_filtrado['Tipo unidade semanas'] == '6']
        quant_6_semanas = df_6_semanas.shape[0]
        total_registros = df_filtrado.shape[0]
        percent_6_semanas = round(
            (quant_6_semanas / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#

        # _________________________________________________________________________________________#

        # Normalizando os dados para garantir que o filtro funcione
        df_filtrado['Tipo unidade semanas'] = df_filtrado['Tipo unidade semanas'].astype(
            str).str.strip()

        # Agora filtra
        df_13_semanas = df_filtrado[df_filtrado['Tipo unidade semanas'] == '13']
        quant_13_semanas = df_13_semanas.shape[0]
        total_registros = df_filtrado.shape[0]
        percent_13_semanas = round(
            (quant_13_semanas / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#
        # _____________________________________________________________________________________#

        # Converter a coluna 'Desconto Financeiro' para numérico no DataFrame filtrado
        df_filtrado['Desconto Financeiro'] = pd.to_numeric(
            df_filtrado['Desconto Financeiro'], errors='coerce')

        # Calcular o total de Desconto Financeiro (ignorando valores nulos)
        total_desconto_financeiro = df_filtrado['Desconto Financeiro'].sum()

        # Calcular o percentual sobre o total vendido (em %)
        percent_desconto_financeiro = round(
            (total_desconto_financeiro / total_valor_vendido_sem_cancelado) * 100) if total_valor_vendido_sem_cancelado != 0 else 0

        # Formatar o valor em reais (usando substituição para vírgula e ponto)
        total_desconto_financeiro_formatado = "R$ {:,.2f}".format(
            total_desconto_financeiro).replace(",", "X").replace(".", ",").replace("X", ".")

        # _____________________________________________________________________________________#
        # ______#_____________________________________________________________________________________#

        # Converter a coluna 'Desconto Financeiro' para numérico no DataFrame filtrado
        df_filtrado['Desconto Real Viabilidade'] = pd.to_numeric(
            df_filtrado['Desconto Real Viabilidade'], errors='coerce')

        # Calcular o total de Desconto Financeiro (ignorando valores nulos)
        total_desconto_viabilidade = df_filtrado['Desconto Real Viabilidade'].sum(
        )

        # Calcular o percentual sobre o total vendido (em %)
        percent_desconto_viabilidade = round(
            (total_desconto_viabilidade / total_valor_vendido_sem_cancelado) * 100) if total_valor_vendido_sem_cancelado != 0 else 0

        # Formatar o valor em reais (usando substituição para vírgula e ponto)
        total_desconto_viabilidade_formatado = "R$ {:,.2f}".format(
            total_desconto_viabilidade).replace(",", "X").replace(".", ",").replace("X", ".")

        # _____________________________________________________________________________________#
        # Converter a coluna 'Desconto Financeiro' para numérico no DataFrame filtrado
        df_filtrado['Ganho Viabilidade R$ '] = pd.to_numeric(
            df_filtrado['Ganho Viabilidade R$ '], errors='coerce')

        # Calcular o total de Desconto Financeiro (ignorando valores nulos)
        total_ganho_viabilidade = df_filtrado['Ganho Viabilidade R$ '].sum()

        # Calcular o percentual sobre o total vendido (em %)
        percent_ganho_viabilidade = round(
            (total_ganho_viabilidade / total_valor_vendido_sem_cancelado) * 100) if total_valor_vendido_sem_cancelado != 0 else 0

        # Formatar o valor em reais (usando substituição para vírgula e ponto)
        total_ganho_viabilidade_formatado = "R$ {:,.2f}".format(
            total_ganho_viabilidade).replace(",", "X").replace(".", ",").replace("X", ".")

        # _____________________________________________________________________________________#

        # _____________________________________________________________________________________#

        # _____________________________________________________________________________________#

        # Agrupando por 'CLIENTES' e contando a quantidade de registros para cada cliente
        # clientes_agrupados = df.groupby('CLIENTE').size().reset_index(name='Total')
        # Agrupando por 'CLIENTES' e contando a quantidade de registros para cada cliente
        # Contando o número de clientes distintos
        # Agora o total_clientes irá variar com os filtros aplicados
        # Contando os clientes únicos no df_filtrado
        total_clientes = df_filtrado['CLIENTE'].nunique()

        ###################################################################################################
        ####################################################################################################

        # CSS para padronizar o tamanho dos cartões
        st.markdown(
            """
                <style>
                .card {
                    background-color: #00FFFF;
                    padding: 30px;
                    width: 90%;
                    height: 200px; /* Altura fixa para todos os cartões */
                    margin-right: 15px;
                    text-align: center;
                    border-radius: 10px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center; /* Centraliza verticalmente */
                }

                .card span {
                    margin: 5px 0; /* Espaçamento entre os textos */
                }

                </style>
                """,
            unsafe_allow_html=True
        )

        # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#BDBDBD;">
                    <span style="color: black; font-size: 15px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Primeira linha de cartões
            st.write("")  # Linha em branco cria espaço
            # Criando as colunas para os cartões
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.markdown(
                    f"""
                        <div class="card">
                            <span style="color: black; font-size: 13px; font-weight: bold;">💰 VGV Bruto</span>
                            <span style="color: black; font-size: 13px;">R$ {total_valor_vendido_sem_cancelado:,.2f}</span>
                            <span style="color: black; font-size: 13px;">Total Assinados: {quant_assinado}</span>
                            <span style="color: black; font-size: 13px;">R$ {ultimo_valor:,.2f}</span>
                            <span style="color: black; font-size: 13px;">Mês: {ultimo_mes} - Ano: {ultimo_ano}</span>
                            <span style="color: black; font-size: 13px;">{ultima_variacao}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#FFDDC1;">
                            <span style="color: black; font-size: 13px; font-weight: bold;">Total Bruto</span>
                            <span style="color: black; font-size: 13px;">R$ {valor_final:,.2f}</span>
                            <span style="color: black; font-size: 13px;">Total Não Assinados: {quant_nao_assinado}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col3:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#FFDDC1;">
                            <span style="color: black; font-size: 13px; font-weight: bold;"> 👥Quantidade Clientes</span>
                            <span style="color: black; font-size: 13px;">{total_clientes}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col4:
                st.markdown(
                    f"""
                        <div class="card">
                            <span style="color: black; font-size: 13px; font-weight: bold;">📉 Latencia de compra</span>
                            <span style="color: black; font-size: 13px;">{media_latencia_compra_arredondada} Dias</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col5:
                st.markdown(
                    f"""
                        <div class="card">
                            <span style="color: black; font-size: 13px; font-weight: bold;">TABELA A VISTA (4M)</span>
                            <span style="color: black; font-size: 13px;">{quant_a_vista}</span>
                            <span style="color: black; font-size: 13px;">{percent_a_vista}%</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )
            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço
            # Segunda linha de cartões
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#2196F3;">
                            <span style="color: white; font-size: 13px; font-weight: bold;">VGV TOTAL LÍQUIDO</span>
                            <span style="color: white; font-size: 13px;">R$ {valor_final:,.2f}</span>
                            <span style="color: white; font-size: 13px;">Total Assinados: {quant_assinado}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                        <div class="card">
                            <span style="color: black; font-size: 13px; font-weight: bold;">VGV Bruto</span>
                            <span style="color: black; font-size: 13px;">R$ {valor_final:,.2f}</span>
                            <span style="color: black; font-size: 13px;">Total Assinados: {quant_assinado}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col3:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#FFDDC1;">
                            <span style="color: black; font-size: 13px; font-weight: bold;">Ticket Médio</span>
                            <span style="color: black; font-size: 13px;">R$ {ticket_medio_filtrado:,.2f}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col4:
                st.markdown(
                    f"""
                        <div class="card" style="background-color:#FFDDC1;">
                            <span style="color: black; font-size: 13px; font-weight: bold;">Follow-ups</span>
                            <span style="color: black; font-size: 13px;">{total_follow_ups}</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            with col5:
                st.markdown(
                    f"""
                        <div class="card">
                            <span style="color: black; font-size: 13px; font-weight: bold;">TABELA CURTA (35M)</span>
                            <span style="color: black; font-size: 13px;">{quant_curta}</span>
                            <span style="color: black; font-size: 13px;">{percent_curta}%</span>
                        </div>
                        """,
                    unsafe_allow_html=True
                )

            # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#BDBDBD;">
                    <span style="color: black; font-size: 13px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:

            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço

            # Definindo as colunas com larguras específicas
            # O primeiro cartão ocupa o espaço de 2 cartões
            col26, col27, col28, col29 = st.columns([2, 1, 1, 1])

            with col26:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#4CAF50;">
                        <span style="color: white; font-size: 13px; font-weight: bold;">📊 DESCONTOS FINANCEIROS</span><br>
                        <span style="color: white; font-size: 13px;">R$ {total_desconto_financeiro}</span><br>
                        <span style="color: white; font-size: 13px;">{percent_desconto_financeiro}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col27:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#FF9800;">
                            <span style="color: black; font-size: 13px; font-weight: bold;">📆INTEGRAL</span>
                            <span style="color: black; font-size: 13px;">{quant_integral}</span>
                            <span style="color: black; font-size: 13px;">{percent_integral}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col28:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#FFDDC1;">
                            <span style="color: black; font-size: 20px; font-weight: bold;">4 SEMANAS</span>
                        <span style="color: black; font-size: 13px;">{quant_4_semanas}</span>
                        <span style="color: black; font-size: 13px;">{percent_4_semanas}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                with col29:
                    st.markdown(
                        f"""
                    <div class="card" style="background-color:#03A9F4;">
            <span style="color: white; font-size: 15px; font-weight: bold;">TABELA LONGA (60M)</span>
                            <span style="color: white; font-size: 13px;">{quant_longa}</span>
                            <span style="color: white; font-size: 13px;">{percent_longa}%</span>
                    </div>
                    """,
                        unsafe_allow_html=True
                    )
            # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#BDBDBD;">
                    <span style="color: black; font-size: 13px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:

            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço

            # Definindo as colunas com larguras específicas
            # O primeiro cartão ocupa o espaço de 2 cartões
            col26, col27, col28, col29 = st.columns([2, 1, 1, 1])

            with col26:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#4CAF50;">
                        <span style="color: white; font-size: 13px; font-weight: bold;">📊 DESCONTO REAL VIABILIDADE</span>
                        <span style="color: white; font-size: 13px;">R$ {total_desconto_viabilidade}</span>
                        <span style="color: white; font-size: 13px;">{percent_desconto_viabilidade}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col27:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#FF9800;">
                        <span style="color: black; font-size: 13px; font-weight: bold;">📆 4 SEMANAS</span>
                        <span style="color: black; font-size: 13px;">{quant_4_semanas}</span>
                        <span style="color: black; font-size: 13px;">{percent_4_semanas}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col28:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#FFDDC1;">
                        <span style="color: black; font-size: 13px; font-weight: bold;">📆 4 SEMANAS</span>
                        <span style="color: black; font-size: 13px;">{quant_4_semanas}</span>
                        <span style="color: black; font-size: 13px;">{percent_4_semanas}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                with col29:
                    st.markdown(
                        f"""
                    <div class="card" style="background-color:#03A9F4;">
                            <span style="color: white; font-size: 13px; font-weight: bold;">TABELA LONG+ (>60M)</span>
                            <span style="color: white; font-size: 13px;">{quant_longuissima}</span>
                            <span style="color: white; font-size: 13px;">{percent_longuissima}%</span>
                    </div>
                    """,
                        unsafe_allow_html=True
                    )

            # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#BDBDBD;">
                    <span style="color: black; font-size: 13px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:

            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço

            # Definindo as colunas com larguras específicas
            # O primeiro cartão ocupa o espaço de 2 cartões
            col26, col27, col28, col29 = st.columns([2, 1, 1, 1])

            with col26:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#4CAF50;">
                        <span style="color: white; font-size: 13px; font-weight: bold;">📊 GANHO VIABILIDADE</span>
                        <span style="color: white; font-size: 13px;">R$ {total_ganho_viabilidade}</span>
                        <span style="color: white; font-size: 13px;">{percent_ganho_viabilidade}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col27:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#FF9800;">
                        <span style="color: black; font-size: 13px; font-weight: bold;">📆 6 SEMANAS</span>
                        <span style="color: black; font-size: 13px;">{quant_6_semanas}</span>
                        <span style="color: black; font-size: 13px;">{percent_6_semanas}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col28:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#FFDDC1;">
                        <span style="color: black; font-size: 13px; font-weight: bold;">📆 % MÉDIO DE ENTRADA</span>
                        <span style="color: black; font-size: 13px;">{percent_entrada}%</span>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # Verificando se o df_filtrado está vazio após os filtros
        if df_filtrado.empty:
            st.markdown(f"""
                <div class="card" style="background-color:#BDBDBD;">
                    <span style="color: black; font-size: 13px; font-weight: bold;">Sem Dados para Amostra</span>
                </div>
                """, unsafe_allow_html=True)
        else:

            # 👉 Espaço entre as linhas
            st.write("")  # Linha em branco cria espaço

            # Definindo as colunas com larguras específicas
            # O primeiro cartão ocupa o espaço de 2 cartões
            col26, col27, col28, col29 = st.columns([2, 1, 1, 1])

            with col26:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#4CAF50;">
                        <span style="color: white; font-size: 13px; font-weight: bold;">📊 RELATÓRIO COMPLETO</span>
                        <span style="color: white; font-size: 13px;">R$ {valor_final:,.2f}</span>
                        <span style="color: white; font-size: 13px;">Total Assinados: {quant_assinado}</span>
                        <span style="color: white; font-size: 13px;">Descontos Aplicados: R$ {total_desconto_financeiro:,.2f}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col27:
                st.markdown(
                    f"""
                    <div class="card" style="background-color:#FF9800;">
                        <span style="color: black; font-size: 13px; font-weight: bold;">📆 13 SEMANAS</span>
                        <span style="color: black; font-size: 13px;">{quant_13_semanas}</span>
                        <span style="color: black; font-size: 13px;">{percent_13_semanas}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            ####################################################### END HOME #######################################################

            # else:
                # st.write("Nenhum dado encontrado para os filtros selecionados.")


# PÁGINA RANKING
if pagina == 'RANKING':
    st.title('📈 RANKING')
    if not df_filtrado.empty:

        # ============================
        # 🔹 LAYOUT: 2 COLUNAS E 2 LINHAS
        # ============================

        # Criar colunas para os gráficos
        col1, col2 = st.columns(2)

        # ============================
        # 📊 1️⃣ GERENTE: Latência + Produtos
        # ============================
        with col1:
            st.subheader("Ranking de Vendas por GERENTE")
            ranking_gerente = df_filtrado.groupby('GERENTE').agg({
                'Valor vendido': 'sum',
                'PRODUTO': 'count',
                'Latencia de compra': 'mean'
            }).reset_index()

            ranking_gerente.rename(columns={
                'PRODUTO': 'Quantidade de Produtos Vendidos',
                'Latencia de compra': 'Média de Latência (Dias)'
            }, inplace=True)

            ranking_gerente = ranking_gerente.sort_values(
                'Valor vendido', ascending=False)
            st.dataframe(ranking_gerente)

            # Gráfico para GERENTE
            chart = alt.Chart(ranking_gerente).mark_bar().encode(
                x=alt.X('GERENTE:N', title='Gerente'),
                y=alt.Y('Valor vendido:Q', title='Valor Vendido (R$)'),
                color=alt.Color('GERENTE:N', title='Gerente'),
                tooltip=[
                    alt.Tooltip('GERENTE:N', title='Gerente'),
                    alt.Tooltip('Valor vendido:Q',
                                title='Valor Vendido', format=',.2f'),
                    alt.Tooltip('Média de Latência (Dias):Q',
                                title='Latência Média', format=',.2f')
                ]
            ).properties(
                width=400,
                height=400,
                title='Vendas por GERENTE'
            )
            st.altair_chart(chart, use_container_width=True)

        # ============================
        # 📊 2️⃣ CORRETOR 1: Latência + Produtos
        # ============================
        with col2:
            st.subheader("Ranking de Vendas por CORRETOR 1")
            ranking_corretor = df_filtrado.groupby('Corretor 1').agg({
                'Valor vendido': 'sum',
                'PRODUTO': 'count',
                'Latencia de compra': 'mean'
            }).reset_index()

            ranking_corretor.rename(columns={
                'PRODUTO': 'Quantidade de Produtos Vendidos',
                'Latencia de compra': 'Média de Latência (Dias)'
            }, inplace=True)

            ranking_corretor = ranking_corretor.sort_values(
                'Valor vendido', ascending=False)
            st.dataframe(ranking_corretor)

            # Gráfico para CORRETOR 1
            chart = alt.Chart(ranking_corretor).mark_bar().encode(
                x=alt.X('Corretor 1:N', title='Corretor 1'),
                y=alt.Y('Valor vendido:Q', title='Valor Vendido (R$)'),
                color=alt.Color('Corretor 1:N', title='Corretor 1'),
                tooltip=[
                    alt.Tooltip('Corretor 1:N', title='Corretor 1'),
                    alt.Tooltip('Valor vendido:Q',
                                title='Valor Vendido', format=',.2f'),
                    alt.Tooltip('Média de Latência (Dias):Q',
                                title='Latência Média', format=',.2f')
                ]
            ).properties(
                width=400,
                height=400,
                title='Vendas por CORRETOR 1'
            )
            st.altair_chart(chart, use_container_width=True)

        # ============================
        # 🔹 Criar nova linha para os próximos gráficos
        # ============================
        col3, col4 = st.columns(2)

        # ============================
        # 📊 3️⃣ GERENTE com Desconto Financeiro
        # ============================
        with col3:
            st.subheader("GERENTES com Desconto Financeiro")
           # Garantir que as colunas 'Valor vendido' e 'Desconto Financeiro' são numéricas
            df_filtrado['Valor vendido'] = pd.to_numeric(df_filtrado['Valor vendido'], errors='coerce')
            df_filtrado['Desconto Financeiro'] = pd.to_numeric(df_filtrado['Desconto Financeiro'], errors='coerce')

            #Remover valores NaN (caso tenham sido convertidos)
            df_filtrado.fillna(0, inplace=True)

            # Realizar o agrupamento após a conversão correta dos dados
            ranking_gerente_desc = df_filtrado.groupby('GERENTE').agg({
                'Valor vendido': 'sum',
                'Desconto Financeiro': 'sum'
            }).reset_index()

            ranking_melted = ranking_gerente_desc.melt(id_vars='GERENTE',
                                                       value_vars=[
                                                           'Valor vendido', 'Desconto Financeiro'],
                                                       var_name='Tipo',
                                                       value_name='Valor')

            color_scale = alt.Scale(domain=['Valor vendido', 'Desconto Financeiro'],
                                    range=['skyblue', 'red'])

            chart = alt.Chart(ranking_melted).mark_bar().encode(
                x=alt.X('GERENTE:N', title='Gerente', sort='-y'),
                y=alt.Y('Valor:Q', title='Valor Total (R$)'),
                color=alt.Color('Tipo:N', scale=color_scale,
                                title='Tipo de Valor'),
                tooltip=[
                    alt.Tooltip('GERENTE:N', title='Gerente'),
                    alt.Tooltip('Tipo:N', title='Tipo'),
                    alt.Tooltip('Valor:Q', title='Valor (R$)', format=',.2f')
                ]
            ).properties(
                width=400,
                height=400,
                title='Desconto Financeiro por GERENTE'
            )
            st.altair_chart(chart, use_container_width=True)

        # ============================
        # 📊 4️⃣ CORRETOR 1 com Desconto Financeiro
        # ============================
        with col4:
            st.subheader("CORRETORES com Desconto Financeiro")
            ranking_corretor_desc = df_filtrado.groupby('Corretor 1').agg({
                'Valor vendido': 'sum',
                'Desconto Financeiro': 'sum'
            }).reset_index()

            ranking_melted = ranking_corretor_desc.melt(id_vars='Corretor 1',
                                                        value_vars=[
                                                            'Valor vendido', 'Desconto Financeiro'],
                                                        var_name='Tipo',
                                                        value_name='Valor')

            chart = alt.Chart(ranking_melted).mark_bar().encode(
                x=alt.X('Corretor 1:N', title='Corretor 1', sort='-y'),
                y=alt.Y('Valor:Q', title='Valor Total (R$)'),
                color=alt.Color('Tipo:N', scale=color_scale,
                                title='Tipo de Valor'),
                tooltip=[
                    alt.Tooltip('Corretor 1:N', title='Corretor 1'),
                    alt.Tooltip('Tipo:N', title='Tipo'),
                    alt.Tooltip('Valor:Q', title='Valor (R$)', format=',.2f')
                ]
            ).properties(
                width=400,
                height=400,
                title='Desconto Financeiro por CORRETOR 1'
            )
            st.altair_chart(chart, use_container_width=True)

        # ============================
        # 🔹 PREPARAÇÃO DOS DADOS
        # ============================

        # Remover espaços extras nos nomes das colunas
        df_filtrado.columns = df_filtrado.columns.str.strip()

        # Converter 'Data da Venda' para datetime e extrair o ano
        df_filtrado['Data da Venda'] = pd.to_datetime(
            df_filtrado['Data da Venda'])
        df_filtrado['Ano'] = df_filtrado['Data da Venda'].dt.year

        # Verificar se 'Ano' existe e criar se necessário
        if 'Ano' not in df_filtrado.columns:
            df_filtrado['Ano'] = pd.to_datetime(
                df_filtrado['Data da Venda']).dt.year

        # ============================
        # 🔹 INTERFACE DO STREAMLIT
        # ============================

        # Título do app
        st.title("📊 Ranking de Vendas por Gerente por Ano (2022 - 2025)")

        # Filtro de anos disponíveis
        anos_disponiveis = sorted(df_filtrado['Ano'].unique().tolist())
        anos_selecionados = st.multiselect(
            '🔎 Selecione os Anos:', anos_disponiveis, default=anos_disponiveis)

        # Filtrar o DataFrame pelos anos selecionados
        df_filtrado_anos = df_filtrado[df_filtrado['Ano'].isin(
            anos_selecionados)]

        # ============================
        # 🔹 AGRUPAMENTO DE DADOS
        # ============================

        # Agrupar por 'GERENTE' e 'Ano' para somar os valores vendidos
        ranking_gerente_ano = df_filtrado_anos.groupby(
            ['GERENTE', 'Ano'])['Valor vendido'].sum().reset_index()

        # Ordenar por Ano e pelo maior valor vendido
        ranking_gerente_ano = ranking_gerente_ano.sort_values(
            ['Ano', 'Valor vendido'], ascending=[True, False])

        # ============================
        # 🔹 GRÁFICO ALTAIR (Com Layering Correto)
        # ============================

        # Criar gráfico de barras
        bars = alt.Chart(ranking_gerente_ano).mark_bar().encode(
            x=alt.X('GERENTE:N', title='Gerente'),
            y=alt.Y('Valor vendido:Q', title='Valor Vendido (R$)'),
            color=alt.Color('GERENTE:N', title='Gerente'),
            tooltip=[
                alt.Tooltip('GERENTE:N', title='Gerente'),
                alt.Tooltip('Ano:N', title='Ano'),
                alt.Tooltip('Valor vendido:Q',
                            title='Valor Vendido', format=',.2f')
            ]
        )

        # Adicionar rótulos de valores nas barras
        text = bars.mark_text(
            align='center',
            baseline='bottom',
            dy=-5,  # Ajuste vertical do texto
            fontSize=10
        ).encode(
            text=alt.Text('Valor vendido:Q', format=',.2f')
        )

        # Layer dos gráficos (barras + rótulos)
        layered_chart = alt.layer(bars, text)

        # Facetear o gráfico por Ano após o layering
        final_chart = layered_chart.facet(
            column=alt.Column('Ano:N', title='Ano')
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_title(
            fontSize=16
        )

        # ============================
        # 🔹 EXIBIÇÃO NO STREAMLIT
        # ============================
        st.altair_chart(final_chart, use_container_width=True)

        # ============================
        # 🔹 TABELA DE DADOS (Opcional)
        # ============================
        st.subheader("📋 Dados de Vendas por Ano e Gerente")
        st.dataframe(ranking_gerente_ano)

    else:
        st.write("Nenhum dado encontrado para o ranking.")

# PÁGINA ORIGENS E ESTADOS
elif pagina == 'Origens_Estados':
    st.title('🌍 Origens e Estados')
    if not df_filtrado.empty:

        # ============================
        # 🔹 Agrupamento com '# Clientes'
        # ============================
        # Agrupar por 'Origem da venda' e 'UF', somar o valor vendido e contar clientes únicos
        origens_estados = df_filtrado.groupby(['Origem da venda', 'UF']).agg({
            'Valor vendido': 'sum',
            'CLIENTE': 'nunique'  # Contar clientes únicos
        }).reset_index()

        # Renomear a coluna para '# Clientes'
        origens_estados.rename(columns={'CLIENTE': '# Clientes'}, inplace=True)

        # ============================
        # 🔹 LAYOUT: 2 COLUNAS E 2 LINHAS
        # ============================

        # Criar as colunas para os gráficos e tabelas
        col1, col2 = st.columns(2)

        # ============================
        # 📊 1️⃣ TABELA: Origens e Estados
        # ============================
        with col1:
            st.subheader("📋 Origens por Estado com # Clientes")
            st.dataframe(origens_estados)

        # ============================
        # 📊 2️⃣ GRÁFICO: Valor Vendido por Origem
        # ============================
        with col2:
            st.subheader("📊 Valor Vendido por Origem da Venda")
            chart = pd.pivot_table(df_filtrado, index='Origem da venda',
                                   values='Valor vendido', aggfunc='sum').reset_index()
            st.bar_chart(chart, x='Origem da venda', y='Valor vendido')

        # ============================
        # 🔹 NOVA LINHA PARA MAIS GRÁFICOS
        # ============================
        col3, col4 = st.columns(2)

        # ============================
        # 📊 3️⃣ GRÁFICO: Valor Vendido por Estado
        # ============================
        with col3:
            st.subheader("📊 Valor Vendido por UF")
            chart_uf = pd.pivot_table(
                df_filtrado, index='UF', values='Valor vendido', aggfunc='sum').reset_index()
            st.bar_chart(chart_uf, x='UF', y='Valor vendido')

        # ============================
        # 📊 4️⃣ TABELA: Clientes por Origem
        # ============================
        with col4:
            st.subheader("📋 Número de Clientes por Origem")
            clientes_por_origem = df_filtrado.groupby(
                'Origem da venda')['CLIENTE'].nunique().reset_index()
            clientes_por_origem.rename(
                columns={'CLIENTE': '# Clientes'}, inplace=True)
            st.dataframe(clientes_por_origem)

        # Agrupar por 'Origem da venda' e 'UF', somar o valor vendido e contar o número de clientes
        origens_estados = df_filtrado.groupby(['Origem da venda', 'UF']).agg({
            'Valor vendido': 'sum',
            'CLIENTE': 'nunique'  # Conta o número de clientes únicos
        }).reset_index()

        # Renomear a coluna para '# Clientes'
        origens_estados.rename(columns={'CLIENTE': '# Clientes'}, inplace=True)

        # Exibir a tabela atualizada no Streamlit
        st.write(origens_estados)

        # ============================
        # 🔹 Agrupamento com '# Clientes'
        # ============================
        # Agrupar por 'Campanha' e 'UF', somar o valor vendido e contar clientes únicos
        campanha_estados = df_filtrado.groupby(['Campanha', 'UF']).agg({
            'Valor vendido': 'sum',
            'CLIENTE': 'nunique'  # Contar clientes únicos
        }).reset_index()

        # Renomear a coluna para '# Clientes'
        campanha_estados.rename(
            columns={'CLIENTE': '# Clientes'}, inplace=True)

        # ============================
        # 🔹 LAYOUT: 2 COLUNAS E 2 LINHAS
        # ============================

        # Criar as colunas para os gráficos e tabelas
        col1, col2 = st.columns(2)

        # ============================
        # 📊 1️⃣ TABELA: Campanha e Estados
        # ============================
        with col1:
            st.subheader("📋 Campanhas por Estado com # Clientes")

            # Exemplo de agrupamento por campanha e estado
            campanha_estados = df.groupby(['Campanha', 'UF'])[
                'Valor vendido'].sum().reset_index()

        # Exibe o DataFrame na tela
            st.dataframe(campanha_estados)

            # ============================
            # 📊 2️⃣ GRÁFICO: Valor Vendido por Campanha
            # ============================
        with col2:
            st.subheader("📊 Valor Vendido por Campanha")
            chart_campanha = pd.pivot_table(
                df_filtrado, index='Campanha', values='Valor vendido', aggfunc='sum').reset_index()
            st.bar_chart(chart_campanha, x='Campanha', y='Valor vendido')

            # ============================
            # 🔹 NOVA LINHA PARA MAIS GRÁFICOS
            # ============================
        col3, col4 = st.columns(2)

        # ============================
        # 📊 3️⃣ GRÁFICO: Valor Vendido por Estado
        # ============================
        with col3:
            st.subheader("📊 Valor Vendido por UF")
            chart_uf = pd.pivot_table(
                df_filtrado, index='UF', values='Valor vendido', aggfunc='sum').reset_index()
            st.bar_chart(chart_uf, x='UF', y='Valor vendido')

            # ============================
            # 📊 4️⃣ TABELA: Clientes por Campanha
            # ============================
        with col4:
            st.subheader("📋 Número de Clientes por Campanha")
            clientes_por_campanha = df_filtrado.groupby(
                'Campanha')['CLIENTE'].nunique().reset_index()
            clientes_por_campanha.rename(
                columns={'CLIENTE': '# Clientes'}, inplace=True)
            st.dataframe(clientes_por_campanha)

            # Remover espaços extras nos nomes das colunas
            df_filtrado.columns = df_filtrado.columns.str.strip()

            # Converter 'Data da Venda' para datetime e extrair o ano
            df_filtrado['Data da Venda'] = pd.to_datetime(
                df_filtrado['Data da Venda'])
            df_filtrado['Ano'] = df_filtrado['Data da Venda'].dt.year

            # Verificar se 'Ano' existe e criar se necessário
        if 'Ano' not in df_filtrado.columns:
            df_filtrado['Ano'] = pd.to_datetime(
                df_filtrado['Data da Venda']).dt.year

            # ============================
            # 🔹 INTERFACE DO STREAMLIT
            # ============================

            # Título do app
            st.title("📊 Ranking de Vendas por Campanha por Ano (2022 - 2025)")

            # Filtro de anos disponíveis
            anos_disponiveis = sorted(df_filtrado['Ano'].unique().tolist())
            anos_selecionados = st.multiselect(
                '🔎 Selecione os Anos:', anos_disponiveis, default=anos_disponiveis)

            # Filtrar o DataFrame pelos anos selecionados
            df_filtrado_anos = df_filtrado[df_filtrado['Ano'].isin(
                anos_selecionados)]

            # ============================
            # 🔹 AGRUPAMENTO DE DADOS
            # ============================

            # Agrupar por 'Campanha' e 'Ano' para somar os valores vendidos
            ranking_campanha_ano = df_filtrado_anos.groupby(
                ['Campanha', 'Ano'])['Valor vendido'].sum().reset_index()

            # Ordenar por Ano e pelo maior valor vendido
            ranking_campanha_ano = ranking_campanha_ano.sort_values(
                ['Ano', 'Valor vendido'], ascending=[True, False])

            # ============================
            # 🔹 GRÁFICO ALTAIR (Com Layering Correto)
            # ============================

            # Criar gráfico de barras
            bars = alt.Chart(ranking_campanha_ano).mark_bar().encode(
                x=alt.X('Campanha:N', title='Campanha'),
                y=alt.Y('Valor vendido:Q', title='Valor Vendido (R$)'),
                color=alt.Color('Campanha:N', title='Campanha'),
                tooltip=[
                    alt.Tooltip('Campanha:N', title='Campanha'),
                    alt.Tooltip('Ano:N', title='Ano'),
                    alt.Tooltip('Valor vendido:Q',
                                title='Valor Vendido', format=',.2f')
                ]
            )

            # Adicionar rótulos de valores nas barras
            text = bars.mark_text(
                align='center',
                baseline='bottom',
                dy=-5,  # Ajuste vertical do texto
                fontSize=10
            ).encode(
                text=alt.Text('Valor vendido:Q', format=',.2f')
            )

            # Layer dos gráficos (barras + rótulos)
            layered_chart = alt.layer(bars, text)

            # Facetear o gráfico por Ano após o layering
            final_chart = layered_chart.facet(
                column=alt.Column('Ano:N', title='Ano')
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=14
            ).configure_title(
                fontSize=16
            )

            # ============================
            # 🔹 EXIBIÇÃO NO STREAMLIT
            # ============================
            st.altair_chart(final_chart, use_container_width=True)

            # ============================
            # 🔹 TABELA DE DADOS (Opcional)
            # ============================
            st.subheader("📋 Dados de Vendas por Ano e Campanha")
            st.dataframe(ranking_campanha_ano)

        else:
            st.write("Nenhum dado encontrado.")


# PÁGINA GRÁFICOS TABELA
if pagina == 'GRÁFICOS TABELA':
    st.title('📊 Gráficos Tabela')
    if not df_filtrado.empty:

        # ============================
        # 🔹 Simulação de Dados (substitua pelo seu df_filtrado)
        # ============================

        # Converter 'Data da Venda' para datetime e extrair o ano
        df_filtrado['Data da Venda'] = pd.to_datetime(
            df_filtrado['Data da Venda'])
        df_filtrado['Ano'] = df_filtrado['Data da Venda'].dt.year

        # ============================
        # 🔹 LAYOUT: 2 COLUNAS, 4 LINHAS (1/4 PROPORÇÃO)
        # ============================

        # Título do app
       # Título personalizado com HTML/CSS
        st.markdown(
             """
                <h1 style='font-size: 20px; text-align: center;'>
                  📊 Análise de Vendas por Campanha com Layout Personalizado
                </h1>
                 """,
                 unsafe_allow_html=True
                    )

       
#############################Inicio Grafico ######################################



 # ============================
        # 📊 1️⃣ LINHA 1: TABELA E GRÁFICO PRINCIPAL
        # _________________________________________________________________________________________#

        df_a_vista = df_filtrado[df_filtrado['Tabela']
                                 == 'A vista']
        # Contando a quantidade de "ASSINADO" na coluna 'Status 1'
        quant_a_vista2 = df_a_vista.shape[0]

        # Calculando o total de registros no DataFrame original
        total_registros = df_filtrado.shape[0]

        # Calculando o percentual de registros "A vista" em relação ao total
        # percent_a_vista = round((quant_a_vista / total_registros) * 100)
        percent_a_vista2 = round(
            (quant_a_vista2 / total_registros) * 100) if total_registros != 0 else 0

        # _________________________________________________________________________________________#
        # ============================
 # ✅ Agrupar por Ano e Mês e somar os valores

 #########################################################################################

    # ============================
    # 🔹 FILTRAR DADOS "À VISTA"
    # ============================

    # ✅ Filtrar apenas vendas "À vista"
        df_a_vista = df[df['Tabela'].str.strip().str.lower() == 'a vista']

    # ✅ Garantir que 'Data da Venda' está em formato datetime
        df_a_vista['Data da Venda'] = pd.to_datetime(
            df_a_vista['Data da Venda'], errors='coerce')
        df_a_vista = df_a_vista.dropna(subset=['Data da Venda'])

    # ✅ Criar colunas para Ano e Mês
        df_a_vista['Ano'] = df_a_vista['Data da Venda'].dt.year
        df_a_vista['Mês'] = df_a_vista['Data da Venda'].dt.month

    # ============================
    # 🔹 FILTRO DE ANO COM `key`
    # ============================

    # ✅ Lista de anos disponíveis
        anos_disponiveis = sorted(df_a_vista['Ano'].unique())
        default_anos = anos_disponiveis if anos_disponiveis else []

    # ✅ Filtro de anos (com `key` para evitar duplicação)
        anos_selecionados = st.multiselect(
            '📅 **Selecione os anos para visualizar:**',
            anos_disponiveis,
            default=default_anos,
            key='filtro_anos_a_vista'  # ✅ Chave única
        )

    # ============================
    # 🔹 FILTRO DE "Tipo unidade semanas" COM `key`
    # ============================

    # Obter os tipos de unidade disponíveis
        tipos_unidade = df_a_vista['Tipo unidade semanas'].dropna(
        ).unique().tolist()
        tipos_unidade.insert(0, 'Todos')  # Adiciona a opção "Todos"

    # ✅ Filtro de Tipo Unidade Semanas (com `key`)
        tipo_unidade_selecionado = st.selectbox(
            '🏡 **Selecione o Tipo de Unidade (semanas):**',
            tipos_unidade,
            key='filtro_tipo_unidade_a_vista'  # ✅ Chave única
        )

    # ============================
    # 🔹 APLICAR FILTROS
    # ============================

    # ✅ Filtrar por ano
        df_filtrado = df_a_vista[df_a_vista['Ano'].isin(anos_selecionados)]

    # ✅ Filtrar por Tipo Unidade Semanas (se não for "Todos")
    if tipo_unidade_selecionado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['Tipo unidade semanas']
                                  == tipo_unidade_selecionado]

    # ============================
    # 🔹 AGRUPAR DADOS
    # ============================

    # ✅ Agrupar por Ano e Mês e somar os valores vendidos e contar clientes
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            '# Clientes': 'sum'  # ✅ Soma a quantidade de clientes
        }).reset_index()

    # ============================
    # 🔹 GRÁFICO DE LINHAS
    # ============================

        st.title("📈 Vendas Mês a Mês - À Vista (Filtrável por Ano e Tipo de Unidade)")
        # ✅ Verificar as colunas antes de prosseguir
           #st.write("Colunas disponíveis:", df.columns.tolist())

    # ✅ Extraindo o mês da coluna de data
    df['Mês'] = df['Data da Venda'].dt.month

    # Simulando filtro aplicado
    #df_filtrado = df.copy()

    # ✅ Verificar se 'Mês' foi criado corretamente
    st.write("Amostra dos dados após extração do Mês:")

    # Anos selecionados para o gráfico
    anos_selecionados = [2022, 2023, 2024, 2025]

    # Criar gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    # Cores e marcadores para os anos
    cores = {2022: 'blue', 2023: 'green', 2024: 'orange', 2025: 'red'}
    marcadores = {2022: 'o', 2023: 's', 2024: '^', 2025: 'D'}

    # Verifica se há dados após o filtro
    if not df_filtrado.empty:
        # ✅ Agrupamento corrigido
        df_vendas_agrupadas = df_filtrado.groupby(['Ano', 'Mês']).agg({
            'Valor vendido': 'sum',
            '# Clientes': 'sum'
        }).reset_index()

        # ✅ Verificar se o agrupamento ocorreu corretamente
        st.write("Vendas agrupadas por Ano e Mês:")

        # Plotar linhas para cada ano selecionado
        for ano in anos_selecionados:
            df_ano = df_vendas_agrupadas[df_vendas_agrupadas['Ano'] == ano]

            # Verifica se há dados para o ano selecionado
            if not df_ano.empty:
                ax.plot(df_ano['Mês'], df_ano['Valor vendido'],
                        marker=marcadores.get(ano, 'o'),
                        color=cores.get(ano, 'black'),
                        label=str(ano))

                # Adicionar rótulos com quantidade de clientes e valor vendido
                for i, row in df_ano.iterrows():
                    ax.text(row['Mês'], row['Valor vendido'],
                            f"R$ {row['Valor vendido']:,.0f}\n{int(row['# Clientes'])} clientes",
                            ha='center', va='bottom', fontsize=8)

        # Configurações do gráfico
        ax.set_xlabel('Mês')
        ax.set_ylabel('Valor Vendido (R$)')
        ax.set_title('Evolução das Vendas À Vista por Ano e Tipo de Unidade')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul',
                            'Ago', 'Set', 'Out', 'Nov', 'Dez'])
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R$ {x:,.0f}'))
        ax.legend(title='Ano')

        # Exibir o gráfico
        st.pyplot(fig)

        # Exibir a tabela de dados
        st.subheader("📋 Vendas Mensais - À Vista")
        #st.dataframe(df_vendas_agrupadas)

    else:
        st.warning("⚠️ Nenhum dado disponível após o filtro aplicado.")




#############################Fim Grafico##########################################