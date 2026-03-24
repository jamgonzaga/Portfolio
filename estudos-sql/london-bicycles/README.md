
# 🚲 Projeto: Bicicletas de Londres (Public Data)

> Este projeto faz parte dos meus [**Estudos de SQL**](../), focado em praticar consultas em conjuntos de dados públicos de larga escala.

---

## 📝 Desafios Práticos Resolvidos

Todos os exercícios abaixo foram realizados utilizando o dataset:  
`bigquery-public-data.london_bicycles.cycle_hire`

### 💡 Conceitos Aplicados
Neste conjunto de exercícios, foquei na estrutura fundamental do SQL:
* **SELECT**: Seleção de colunas específicas.
* **FROM**: Identificação da origem dos dados no GCP.
* **WHERE**: Filtros lógicos para extração de informações pontuais.

---

### 🚀 Consultas Realizadas

### 🚲1. Identificação de Estação por ID
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

