# --- SISTEMA DE ANÁLISE EDUCACIONAL: PORTFÓLIO DE OPERADORES ---

print("--- Iniciando Processamento de Dados Acadêmicos ---")

# DADOS FICTÍCIOS (Simulando uma entrada de banco de dados)
nome_aluno = "Carlos Silva"
nota_prova_1 = 8.5
nota_prova_2 = 7.0
frequencia_percentual = 0.85  # 85% de presença
mensalidade_base = 1200.0
tem_desconto_pontualidade = True

# 1. OPERADORES ARITMÉTICOS (Calculando o Desempenho)
# Pergunta: Qual a média final e o valor da mensalidade com bônus?
media_final = (nota_prova_1 + nota_prova_2) / 2  # Adição e Divisão
bonus_participacao = 0.5
nota_com_bonus = media_final + bonus_participacao # Soma

desconto_valor = mensalidade_base * 0.10 # Multiplicação (10% de desconto)
valor_final_mensalidade = mensalidade_base - desconto_valor # Subtração

print(f"Aluno: {nome_aluno}")
print(f"Média Final: {media_final} | Nota com Bônus: {nota_com_bonus}")

# 2. OPERADORES DE ATRIBUIÇÃO (Atualizando Registros)
# Pergunta: Se o aluno fizer um curso extra, somamos 2 pontos na média.
nota_com_bonus += 2 
# O mesmo que: nota_com_bonus = nota_com_bonus + 2
print(f"Nota após curso extra: {nota_com_bonus}")

# 3. OPERADORES DE COMPARAÇÃO (Critérios de Aprovação)
# Pergunta: O aluno atingiu os requisitos mínimos?
media_minima = 7.0
esta_aprovado = nota_com_bonus >= media_minima # Maior ou igual
foi_nota_maxima = nota_com_bonus == 10.0      # Igualdade
precisa_de_recuperacao = nota_com_bonus < 5.0  # Menor que

print(f"Aprovado: {esta_aprovado} | Nota Máxima: {foi_nota_maxima}")

# 4. OPERADORES LÓGICOS (Regras de Negócio Complexas)
# Pergunta: Para manter a bolsa, precisa de média > 8 E frequência > 80%
manter_bolsa = nota_com_bonus > 8.0 and frequencia_percentual > 0.80
# Pergunta: O aluno ganha prêmio se tiver nota 10 OU se for o destaque do mês
ganhou_premio = foi_nota_maxima or (nota_com_bonus > 9.5)

# Pergunta: Verificar se o aluno NÃO está inadimplente
situacao_regular = not False # Inversão lógica

print(f"Manter Bolsa: {manter_bolsa}")
print(f"Ganhou Prêmio de Destaque: {ganhou_premio}")

print("--- Fim da Análise Educacional ---")