📊 Estudos de SQL: Google Data Analytics

Status: Em andamento 🚀

Objetivo: Documentar o aprendizado prático em extração e análise de dados usando a infraestrutura do Google Cloud.

🛠️ Tecnologias e Ferramentas

Plataforma: Google Cloud Platform (GCP)

Ferramenta de Dados: BigQuery Studio (Ambiente Sandbox)

Linguagem: SQL (Standard SQL)

💡 Conceitos Fundamentais Aprendidos

Para interagir com grandes volumes de dados (Big Data), utilizei a estrutura básica de consultas:

SELECT: Define as colunas que desejo visualizar.

FROM: Indica a origem dos dados (tabelas e conjuntos de dados).

WHERE: Aplica filtros lógicos para extrair apenas informações relevantes.

📝 Desafios Práticos Resolvidos

Todos os exercícios abaixo foram realizados utilizando o conjunto de dados público de bicicletas de Londres:
bigquery-public-data.london_bicycles.cycle_hire

🚲 1. Identificação de Estação por ID

Pergunta: Qual o nome da estação cujo ID de início é 111?

Query SQL:

SELECT
    start_station_name
FROM
    `bigquery-public-data.london_bicycles.cycle_hire`
WHERE
    start_station_id = 111;


🚲 2. Rastreamento de Histórico de Bicicleta

Pergunta: Quais os IDs de aluguel, IDs de estação e nomes de estação que a bike_id 1710 utilizou?

Query SQL:

SELECT
    rental_id,
    start_station_id,
    start_station_name
FROM
    `bigquery-public-data.london_bicycles.cycle_hire`
WHERE
    bike_id = 1710;


🚲 3. Identificação de Modelo de Equipamento

Pergunta: Qual o modelo da bicicleta com ID 58782?

Query SQL:

SELECT
    bike_model
FROM
    `bigquery-public-data.london_bicycles.cycle_hire`
WHERE
    bike_id = 58782;


🚲 4. Filtro de Longa Duração

Pergunta: Quais as viagens que duraram mais de 20 minutos (1200 segundos)?

Query SQL:

SELECT
    duration,
    start_station_name
FROM
    `bigquery-public-data.london_bicycles.cycle_hire`
WHERE
    duration >= 1200;


👩‍🎓 Sobre Mim

Estudante em transição de carreira para Dados & Business Intelligence. Atualmente atuando como Tutora de Farmácia e Mediadora Pedagógica, aplicando lógica estruturada na organização de processos educacionais.
