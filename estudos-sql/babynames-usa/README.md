
# 👶 Projeto: Tendências de Nomes (USA Babynames)

> Parte dos meus [**Estudos de SQL**](../). Foco em **Ingestão de Dados** e consultas multi-tabelas no BigQuery.

---

## 🛠️ Setup e Competências
* **Ambiente:** Google BigQuery (GCP).
* **Ingestão:** Upload manual de `.txt` com definição de **Schema**.
* **Técnica SQL:** Uso de *Wildcards* (`*`) para análise de múltiplos anos.

---

## 📝 Desafios Práticos Resolvidos

###  1. Top 5 Nomes Masculinos (2014)
* **Pergunta:** Quais foram os 5 nomes de meninos mais populares nos Estados Unidos em 2014?
* **Query SQL:**

```sql
SELECT
    name,
    count
FROM
    `meu-primeiro-491016.babynames.names_2014`
WHERE
    gender = 'M'
ORDER BY
    count DESC
LIMIT 5;
````

### 2. Consulta Global em Múltiplas Tabelas (Análise Histórica)
* **Pergunta:** Como consultar o ranking geral considerando todos os anos carregados (ex: 2015 a 2019) de uma só vez?

* **Query SQL:**

```sql
SQL
SELECT
    name,
    count
FROM 
    `meu-primeiro-491016.babynames.names_*`
ORDER BY
    count DESC
LIMIT 10;
```
