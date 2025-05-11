# Análise de Dados da COVID-19 em São Paulo

Este repositório documenta meu progresso na busca, limpeza e pesquisa de dados relacionados à COVID-19 no estado de São Paulo. O objetivo principal é fazer a análise completa da tabela, explorar os dados presentes, fazer correções e descartes necesários e também praticar queries sql usando `Jupyter Notebook`

## Fontes de Dados

Os dados utilizados neste projeto foram obtidos através do [COVID-19 Data Hub](https://covid19datahub.io/), uma plataforma que agrega dados de diversas fontes confiáveis sobre a pandemia global. O foco específico foi nos dados referentes ao estado de São Paulo.

## Processo de Análise

O processo de análise foi dividido nas seguintes etapas:

1.  **Busca e Carregamento dos Dados:**
    * Identificação e download dos dados relevantes para São Paulo a partir do COVID-19 Data Hub.
    * Utilização de bibliotecas Python como `pandas` para carregar os dados em um ambiente Jupyter Notebook.

2.  **Limpeza dos Dados:**
    * **Remoção de Colunas Irrelevantes:** Identificação e exclusão de colunas que não contribuem para a análise focada em São Paulo (ex: IDs, informações geográficas detalhadas não necessárias, chaves para outras bases de dados).
    * **Tratamento de Valores Ausentes (NULL/NaN):**
        * Substituição de valores ausentes em colunas numéricas (como `recovered`, `tests`, `vaccines`, e as colunas de medidas de saúde pública) por `0`.
        * Remoção de colunas com dados consistentemente ausentes (`hosp`, `icu`, `vent`).
        * Tratamento específico de valores `NULL` nas colunas de índices de resposta governamental, substituindo-os por `0` para permitir a análise.
    * **Conversão de Tipos de Dados:** Conversão de colunas numéricas (que podem ter sido carregadas como float) para o tipo inteiro (`int`) após o tratamento de valores ausentes.

3.  **Pesquisa e Análise Exploratória (SQL com Pandas):**
    * Utilização de consultas SQL (executadas via `pandas` e `sqlite3`) para explorar os dados limpos.
    * **Seleção e Filtragem:** Extração de subconjuntos de dados com base em critérios específicos (ex: dados após uma certa data, dados com um certo número de casos/mortes).
    * **Ordenação:** Organização dos dados por data para observar a progressão temporal.
    * **Agregação (COUNT, MAX, MIN, AVG):** Cálculo de estatísticas resumidas (total de casos, pico de mortes, média de testes).
    * **Agrupamento (GROUP BY):** Análise de métricas por diferentes categorias (ex: contagem de registros por nível de fechamento de escolas).
    * **Cálculo de Novas Métricas:** Criação de colunas derivadas, como a taxa de letalidade (`deaths` / `confirmed`).
    * **Subqueries:** Utilização de subconsultas para realizar análises mais complexas (ex: comparar valores com a média).

## Insights Importantes (Em Progresso)

Até o momento, a análise inicial dos dados limpos de COVID-19 em São Paulo permitiu observar:

* **Evolução Temporal:** A progressão do número de casos confirmados e mortes ao longo do tempo, identificando possíveis picos e ondas da pandemia.
* **Impacto das Medidas de Saúde Pública:** Uma análise preliminar da relação entre as medidas de saúde pública implementadas (como fechamento de escolas, locais de trabalho, restrições de eventos) e a variação nos indicadores da doença.
* **Tendências de Testagem e Vacinação:** A evolução do número de testes realizados e o progresso da campanha de vacinação (número de doses administradas, pessoas vacinadas com uma dose e totalmente vacinadas).
* **Taxa de Letalidade:** O cálculo da taxa de letalidade ao longo do tempo pode fornecer insights sobre a gravidade da doença em diferentes períodos.

**Próximos Passos:**

* Análise mais aprofundada da correlação entre as medidas de saúde pública e os indicadores epidemiológicos.
* Visualização dos dados utilizando bibliotecas como `matplotlib` e `seaborn` para identificar padrões e tendências de forma mais clara.
* Exploração de possíveis relações entre a taxa de vacinação e a redução de casos graves e óbitos.
* Análise da evolução das taxas de testagem em relação ao número de casos confirmados.

## Estrutura do Repositório

```
.
├── data/
│   ├── covid_data.csv                  # Arquivo CSV original
│   └── covid_data.db                   # Banco de dados SQLite original
├── notebooks/
│   ├── 01_gerar_db.ipynb               # Cria o banco de dados SQLite (covid_data.db) a partir do arquivo CSV.
│   ├── 02_limpeza_dados.ipynb          # Realiza a limpeza e tratamento dos dados, gerando covid_data_limpo.db e .csv.
│   └── 03_analise_exploratoria.ipynb   # Notebook para as consultas SQL e análise
├── output/
│   ├── covid_data_limpo.csv            # Arquivo CSV limpo (se você optar por salvar)
│   └── covid_data_limpo.db             # Banco de dados SQLite limpo
├── scripts/
│   └── gerar_db.py                     # Script Python para criar o banco de dados (mantido aqui)
└── README.md  
```

## Como Utilizar

1.  **Clone o repositório:** `git clone https://github.com/MateusdeNovaesSantos/analise-covid-sp.git`.
2.  **Certifique-se de ter o arquivo de dados:** O arquivo `covid_data.csv` deve estar presente na pasta `data/`.
3.  **Instale as bibliotecas necessárias:** Se você ainda não as tiver, execute: `pip install pandas sqlite3` no seu terminal.
4.  **Execute os notebooks em ordem:**
    * Abra o Jupyter Notebook e navegue até a pasta `notebooks/`.
    * Execute o notebook `01_gerar_db.ipynb` para criar o banco de dados `covid_data.db`.
    * Em seguida, execute o notebook `02_limpeza_dados.ipynb` para limpar os dados e gerar `covid_data_limpo.db` e `covid_data_limpo.csv` na pasta `output/`.
    * Finalmente, execute o notebook `03_analise_exploratoria.ipynb` para realizar as consultas SQL e explorar os insights.
5.  **Explore os resultados:** Os notebooks contêm o código, as consultas SQL e a saída dos resultados. Leia as explicações em Markdown para entender cada etapa.

## Aprendizados

Durante este projeto, eu aprendi sobre:

* Como buscar e carregar dados de fontes online.
* A importância da limpeza de dados e as técnicas para tratar valores ausentes e tipos de dados inconsistentes.
* Como utilizar SQL dentro do Jupyter Notebook com Pandas para explorar e analisar dados.
* A aplicação de comandos SQL como `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING` e subqueries em um cenário real.
* A criação de novas métricas a partir dos dados existentes.
* A organização de um projeto de análise de dados em um repositório GitHub.


Você pode seguir o processo de análise detalhado nos seguintes notebooks:
* [01_gerar_db.ipynb](notebooks/01_gerar_db.ipynb)
* [02_limpeza_dados.ipynb](notebooks/02_limpeza_dados.ipynb)
* [03_analise_exploratoria.ipynb](notebooks/03_analise_exploratoria.ipynb)

---

**Última Atualização:** 11 de Maio de 2025