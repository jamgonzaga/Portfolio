# 🌳 Projeto: Análise de Arborização Urbana (NYC Street Trees)

> Parte dos meus [**Estudos de SQL**](../). Foco em **Funções de Agregação** e **Comparação Histórica** entre diferentes censos (1995, 2005 e 2015).

---

## 🛠️ Setup e Competências
* **Dataset:** `bigquery-public-data.new_york_trees`
* **Técnicas SQL:** `AVG()` para cálculos estatísticos e `UNION ALL` para unificar resultados de tabelas distintas.
* **Desafio Técnico:** Lidar com nomes de colunas diferentes entre tabelas (ex: `diameter` em 1995 vs `tree_dbh` em 2015).

---

## 🚀 Consultas Práticas

### 1. Cálculo de Diâmetro Médio (2005)
* **Pergunta:** Qual o diâmetro médio (em polegadas) das árvores de NYC em 2005?
```sql
SELECT 
    AVG(tree_dbh) AS media_2005
FROM 
    `bigquery-public-data.new_york_trees.tree_census_2005`;
```
2. Comparativo Histórico (1995 vs 2015)
Pergunta: O diâmetro médio das árvores aumentou ao longo de 20 anos?

```sql
SELECT 
    '1995' AS ano, 
    AVG(diameter) AS diametro_medio
FROM 
    `bigquery-public-data.new_york_trees.tree_census_1995`

UNION ALL

SELECT 
    '2015' AS ano, 
    AVG(tree_dbh) AS diametro_medio
FROM 
    `bigquery-public-data.new_york_trees.tree_census_2015`;
```
