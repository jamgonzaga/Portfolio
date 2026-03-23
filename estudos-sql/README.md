# 📊 Estudos de SQL: Google Data Analytics

> **Status:** Em andamento 🚀  
> **Objetivo:** Documentar o aprendizado prático em extração e análise de dados usando a infraestrutura do Google Cloud.

---

## 🛠️ Tecnologias e Ferramentas

* **Plataforma:** [Google Cloud Platform (GCP)](https://cloud.google.com/)
* **Ferramenta de Dados:** BigQuery Studio (Ambiente Sandbox)
* **Linguagem:** SQL (Standard SQL)

---

## 💡 Conceitos Fundamentais Aprendidos

Para interagir com grandes volumes de dados (Big Data), utilizei a estrutura básica de consultas:

1. **SELECT**: Define as colunas ou que desejo visualizar.
2. **FROM**: Indica a origem dos dados (nome da tabela).
3. **WHERE**: Aplica filtros lógicos para extrair apenas informações relevantes.

---

## 📝 Desafios Práticos Resolvidos

Todos os exercícios abaixo foram realizados utilizando o conjunto de dados público de bicicletas de Londres:  
`bigquery-public-data.london_bicycles.cycle_hire`

### 🚲 1. Identificação de Estação por ID
* **Pergunta:** Qual é o nome da estação cujo start_station_id é  **111**?
* **Query SQL:**

```sql
SELECT
    start_station_name
FROM
    `bigquery-public-data.london_bicycles.cycle_hire`
WHERE
    start_station_id = 111;
```

### 🚲 2. Rastreamento de Histórico de Bicicleta
* **Pergunta:** Retorne todos os rental_ids, IDS de estações e nomes de estações de onde bike_id 1710 partiu.
* **Query SQL:**

```sql
SELECT
    rental_id,
    start_station_id,
    start_station_name
FROM
    `bigquery-public-data.london_bicycles.cycle_hire`
WHERE
    bike_id = 1710;
```
### 🚲 3. Identificação de Modelo de Equipamento
* **Pergunta:** Qual é o bike_model de bike_id 58782 ?
* **Query SQL:**

```sql
SELECT
    bike_model
FROM
    `bigquery-public-data.london_bicycles.cycle_hire`
WHERE
    bike_id = 58782;
```
### 🚲 4. Filtro de Longa Duração
* **Pergunta:** Quantas  viagens de bicicleta duraram 20 minutos ou mais ( mais de 1200 segundos)? 
* **Query SQL:**

```sql
SELECT
    duration,
    start_station_name
FROM
    `bigquery-public-data.london_bicycles.cycle_hire`
WHERE
    duration >= 1200;
```
### 👩‍🎓 Sobre Mim
Estudante em transição de carreira para Dados & Business Intelligence. Atualmente atuando como Tutora de Farmácia e Mediadora Pedagógica, aplicando lógica estruturada na organização de processos educacionais.
