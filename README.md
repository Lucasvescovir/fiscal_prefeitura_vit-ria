**🏛️ Fiscal de Vitória-ES**

🔎 Visão Geral

O projeto Fiscal de Vitória-ES é uma aplicação interativa desenvolvida em Streamlit que visa promover a transparência e o controle social dos gastos públicos da Prefeitura Municipal de Vitória, Espírito Santo. Através de dados abertos de despesas pagas, a ferramenta permite visualizar estatísticas, gráficos e explorar os principais fornecedores e as tendências de gastos do município de forma clara e acessível.

Este projeto é uma iniciativa sem fins lucrativos, criado com o objetivo de facilitar o acesso da população às informações financeiras da cidade, incentivando a fiscalização e a participação cívica.

✨ Funcionalidades

Resumo das Liquidações Pagas: Visualização de métricas chave como despesa total, número de registros, despesa média e a maior despesa individual em 2025.

Análise de Fornecedores: Identificação dos Top 10 fornecedores por valor total de despesa, apresentados em gráficos de barras e pizza para fácil compreensão da participação de cada um.

Gastos Mensais: Gráfico de linha interativo mostrando a evolução dos gastos públicos ao longo dos meses de 2025.

Visualização do Dataset Limpo: Acesso direto ao DataFrame das despesas, após o processo de limpeza e tratamento dos dados.

🚀 Como Rodar o Projeto Localmente

Para configurar e rodar este projeto em sua máquina local, siga os passos abaixo:

Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.7+ é recomendada).

1. Clonar o Repositório
2. 
git clone https://github.com/seu-usuario/fiscal-vitoria.git
cd fiscal-vitoria

(Nota: Lembre-se de substituir seu-usuario/fiscal-vitoria pelo caminho real do seu repositório.)

2. Criar e Ativar um Ambiente Virtual (Recomendado)
3. 
python -m venv venv

 **No Windows**
 
.\venv\Scripts\activate

**No macOS/Linux**

source venv/bin/activate

5. Instalar as Dependências
6. 
pip install -r requirements.txt

7. Preparar os Dados
   
Baixe o arquivo de dados DespesasPagas-2025.csv (ou o nome do arquivo que você estiver usando) e coloque-o na raiz do diretório do projeto. Certifique-se de que o encoding do CSV seja compatível (o código usa latin-1).

9. Executar a Aplicação Streamlit
    
streamlit run seu_script_principal.py

(Nota: Substitua seu_script_principal.py pelo nome do arquivo Python que contém o código da sua aplicação Streamlit, por exemplo, app.py ou main.py).

Após executar o comando, uma nova aba será aberta em seu navegador com a aplicação rodando.

📊 Fonte dos Dados

Os dados utilizados neste projeto são obtidos da Prefeitura Municipal de Vitória, provenientes de fontes públicas e abertas relacionadas às despesas pagas.

🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, detetar bugs ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

👨‍💻 Autor

Lucas Vescovi
