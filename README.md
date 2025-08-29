# 🏛️ Fiscal de Vitória-ES: Transparência e Controle dos Gastos Públicos!
Fiscal de Vitória-ES: Aplicativo Streamlit para análise e visualização interativa dos gastos públicos da Prefeitura de Vitória, promovendo a transparência e o controle social.

##📝 Sobre o Projeto
O "Fiscal de Vitória-ES" é um projeto de código aberto e sem fins lucrativos dedicado a promover a transparência e o controle social dos gastos públicos da Prefeitura de Vitória, Espírito Santo. Desenvolvido com Streamlit, este aplicativo interativo permite que qualquer cidadão visualize, analise e explore as despesas pagas pelo município de forma intuitiva e acessível.

Acreditamos que a informação clara e de fácil acesso é fundamental para o exercício da cidadania e para fortalecer a fiscalização popular sobre o uso dos recursos públicos.

##✨ Funcionalidades
O aplicativo oferece as seguintes análises e visualizações:

Resumo das Liquidações: Métricas principais como:

Despesa Total: O valor total gasto pelo município.

Número de Registros: Quantidade de despesas detalhadas.

Despesa Média: O valor médio por liquidação.

Maior Despesa: A liquidação de maior valor registrada.

Top Fornecedores: 

Gráfico de barras dos Top 10 Fornecedores que mais receberam pagamentos.
Gráfico de pizza mostrando a Participação Percentual dos Top 5 Fornecedores no total de despesas.

Gastos por Mês: Um gráfico de linha que ilustra a tendência dos gastos mensais, permitindo identificar padrões ou anomalias ao longo do ano.

Dataset Limpo Completo: Visualização da tabela de dados brutos das despesas após o tratamento e limpeza.

##📊 Fonte de Dados
Os dados utilizados neste projeto são públicos e foram obtidos da Prefeitura Municipal de Vitória - ES, especificamente do arquivo DespesasPagas-2025.csv (referente ao ano de 2025).

##🚀 Tecnologias Utilizadas
Python: Linguagem de programação principal.

Streamlit: Framework para criação de aplicativos web interativos e dashboards.

Pandas: Biblioteca para manipulação e análise de dados.

Plotly Express: Biblioteca para criação de gráficos interativos e visualizações de dados.

##🛠️ Como Rodar o Projeto Localmente
Para executar este projeto em sua máquina, siga os passos abaixo:

Clone o Repositório:
"""
git clone <URL_DO_SEU_REPOSITORIO>
cd fiscal-vitoria-es
"""
(Substitua <URL_DO_SEU_REPOSITORIO> pela URL real do seu repositório GitHub.)

Crie e Ative um Ambiente Virtual (Recomendado):
"""
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
"""
Instale as Dependências:
"""
pip install pandas streamlit plotly-express
"""
Obtenha os Dados:
Certifique-se de ter o arquivo DespesasPagas-2025.csv na mesma pasta do script principal (app.py ou o nome do seu arquivo .py). Você pode baixar os dados diretamente do portal de transparência da Prefeitura de Vitória ou usar um arquivo que você já tenha.

Execute o Aplicativo Streamlit:

streamlit run seu_script.py

(Substitua seu_script.py pelo nome do arquivo Python que contém o código do seu aplicativo Streamlit.)

Após a execução, o Streamlit abrirá o aplicativo automaticamente no seu navegador padrão.

##🤝 Contribuições
Contribuições são bem-vindas! Se você tiver sugestões, encontrar bugs ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

##👨‍💻 Desenvolvedor
Este projeto foi desenvolvido por Lucas Vescovi.
