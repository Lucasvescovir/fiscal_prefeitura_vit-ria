import pandas as pd
import streamlit as st
import plotly.express as px

df_despesas = pd.read_csv("DespesasPagas-2025.csv", encoding='latin-1')


df_despesas_limpo = df_despesas.drop(columns=['NumeroPagamento','ProcessoPagamento','Licitacao', 'NumeroEmpenho', 'DigitoPagamento','idEmpenho','NumeroEmpenho','NumeroLiquidacao','Exercicio','Descricao','UnidadeGestoraEmpenho','CodUnidadeGestoraEmpenho'])


# Despesas
df_despesas_limpo['Data'] = pd.to_datetime(df_despesas_limpo['Data'], dayfirst=True, format='mixed', errors='coerce')
df_despesas_limpo = df_despesas_limpo.drop_duplicates()


# Calcula as métricas principais (Despesas) e Transforma padrão americano para brasileiro

gasto_total = df_despesas_limpo['Valor'].sum()
g = f"{gasto_total:,.2f}"
g = g.replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")


num_registros = df_despesas_limpo.shape[0]  # Conta o número de linhas (registros)


media_gasto = df_despesas_limpo['Valor'].mean()
m = f"{media_gasto:,.2f}"
m = m.replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")

max_gasto = df_despesas_limpo['Valor'].max()
mx = f"{max_gasto:,.2f}"
mx = mx.replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")


#top 10 fornecedores por valor
fornecedores = df_despesas_limpo.groupby('NomeFornecedor')['Valor'].sum()
df_top_fornecedores = pd.DataFrame(fornecedores).sort_values(by='Valor', ascending=False)
top_10_fornecedores = df_top_fornecedores.head(10)

#gasto mensal
df_despesas_limpo_por_data = df_despesas_limpo.set_index('Data')
gastos_mensais = df_despesas_limpo_por_data.resample('M')['Valor'].sum()

#Streamlit
st.set_page_config(layout="wide")
# Título da página
st.title("🏛️ Fiscal de Vitória-ES")
#st.subheader("Bem vindos ao Fiscal de Vitória")
st.write('🔎 Transparência e controle dos gastos públicos de Vitória')
st.write('\n')
st.markdown("<h6>Visualize estatísticas, gráficos e explore os principais fornecedores e gastos do município.<br>Projeto sem fins lucrativos, feito para promover a transparência e o controle social.</h6>", unsafe_allow_html=True)
st.caption('Projeto sem fins lucrativos, feito para promover a transparência e o controle social.')



st.divider()

# Título da seção
st.header("📊 Análise de Liquidações Pagas (2025)")
st.subheader("🔎 Resumo das Liquidações")


# Exibindo as métricas principais
# Utilize a formatação f-string para deixar os números mais legíveis
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="💰 Despesa total", value=f"R$ {g}")
with col2:
    st.metric(label="📝 Registros", value=f"{num_registros:,.0f}".replace(",", "."))
with col3:
    st.metric(label="📊 Despesa Média", value=f"R$ {m}")
with col4:
    st.metric(label="🏆 Maior Despesa", value=f"R$ {mx}")

st.divider()

#Fornecedores

st.header('🏆 Fornecedores - Top 10 e Participação (%)')

# Cria duas colunas com larguras iguais
col1, col2 = st.columns(2)

# Coloca o gráfico de barras na primeira coluna
with col1:
    fig_bar = px.bar(
        top_10_fornecedores,
        x='Valor',
        y=top_10_fornecedores.index,  # O nome dos fornecedores está no índice
        orientation='h',  # Define a orientação horizontal
        color='Valor',  # Define a cor com base no valor, criando a legenda
        title='Top 10 Fornecedores'
    )
    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig_bar, use_container_width=True)

# Coloca o gráfico de pizza na segunda coluna
with col2:
    # Prepara o DataFrame para o gráfico de pizza
    df_pizza = top_10_fornecedores.head(5).reset_index()

    # Cria o gráfico de pizza com Plotly Express
    fig_pie = px.pie(
        df_pizza,
        values='Valor',
        names='NomeFornecedor',
        title="Top 5 - Participação (%)",
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

st.header("📅 Gastos por Mês")

# Converte a série de gastos mensais em um DataFrame
df_gastos_mensais = gastos_mensais.reset_index()
df_gastos_mensais.columns = ['Data', 'Total Gasto (R$)']

# Cria o gráfico de linha com Plotly Express
fig_line = px.line(
    df_gastos_mensais,
    x='Data',
    y='Total Gasto (R$)',
    title='Gastos por Mês',
    markers=True,  # Adiciona os pontos em cada mês
    template='plotly_dark' # Usa o tema escuro
)

# Atualiza o layout para que os rótulos de eixo fiquem mais claros
fig_line.update_layout(xaxis_title="Mês/Ano", yaxis_title="Total Gasto (R$)", hovermode="x unified")

# Exibe o gráfico no Streamlit
st.plotly_chart(fig_line, use_container_width=True)

st.divider()

st.header('DataSet Limpo Completo')
st.write(df_despesas_limpo)

st.divider()

st.markdown("<h6 style='text-align: center; color:gray;'>Fiscal de Vitória © 2025 — Desenvolvido por Lucas Vescovi</h6>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center; color:gray;'>Dados públicos da Prefeitura de Vitória | Projeto sem fins lucrativos</h6>", unsafe_allow_html=True)
