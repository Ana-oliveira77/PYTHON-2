# ============================================================
# EXERCÍCIO PRÁTICO - VISUALIZAÇÃO
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
import ast

%matplotlib inline


wc = pd.read_csv('wc_formatado.csv', parse_dates=['data'])


plt.style.use('ggplot')

# Seaborn
sns.set_theme(style='darkgrid')

# Plotly
pio.templates.default = "plotly_white"


# ============================================================
# 1) HISTOGRAMA DO PÚBLICO (comparecimento)

wc_publico = wc[wc['comparecimento'] > 0]

# --- Matplotlib ---
plt.figure(figsize=(10, 6))
plt.hist(wc_publico['comparecimento'], bins=30)
plt.title('Distribuição de público nos jogos (Matplotlib)')
plt.xlabel('Público presente')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# --- Seaborn ---
plt.figure(figsize=(10, 6))
sns.histplot(wc_publico['comparecimento'], bins=30, kde=False)
plt.title('Distribuição de público nos jogos (Seaborn)')
plt.xlabel('Público presente')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# --- Plotly ---
fig = px.histogram(
    wc_publico,
    x='comparecimento',
    nbins=30,
    title='Distribuição de público nos jogos (Plotly)'
)
fig.update_layout(
    xaxis_title='Público presente',
    yaxis_title='Frequência'
)
fig.show()


# ============================================================
# 2) SCATTER GOLS_1 x GOLS_2 

gols = wc[['gols_1', 'gols_2']] * np.random.random((len(wc), 2))

# --- Matplotlib ---
plt.figure(figsize=(8, 8))
plt.scatter(gols['gols_1'], gols['gols_2'], alpha=0.5)
plt.title('Relação entre gols feitos e sofridos (Matplotlib)')
plt.xlabel('Gols do time 1')
plt.ylabel('Gols do time 2')
plt.tight_layout()
plt.show()

# --- Seaborn ---
plt.figure(figsize=(8, 8))
sns.scatterplot(x='gols_1', y='gols_2', data=gols, alpha=0.5)
plt.title('Relação entre gols feitos e sofridos (Seaborn)')
plt.xlabel('Gols do time 1')
plt.ylabel('Gols do time 2')
plt.tight_layout()
plt.show()

# --- Plotly ---
fig = px.scatter(
    gols,
    x='gols_1',
    y='gols_2',
    title='Relação entre gols feitos e sofridos (Plotly)',
    labels={'gols_1': 'Gols do time 1', 'gols_2': 'Gols do time 2'}
)
fig.show()


# ============================================================
# 3) TOP 10 PAÍSES QUE MAIS PARTICIPARAM DE COPAS


part1 = wc[['time_1', 'ano', 'copa']].rename(columns={'time_1': 'país'})
part2 = wc[['time_2', 'ano', 'copa']].rename(columns={'time_2': 'país'})
participacoes = pd.concat([part1, part2], ignore_index=True).drop_duplicates()

participacao = (
    participacoes
    .groupby(['país', 'copa'])
    .size()
    .reset_index(name='num_copas')
)

participacao_pivot = (
    participacao
    .pivot(index='país', columns='copa', values='num_copas')
    .fillna(0)
)

participacao_pivot = participacao_pivot.reindex(
    columns=['Masculina', 'Feminina'],
    fill_value=0
)

participacao_pivot['total'] = participacao_pivot['Masculina'] + participacao_pivot['Feminina']
top10 = participacao_pivot.sort_values('total', ascending=False).head(10)
top10 = top10.sort_values('total', ascending=True)   # para plotar de forma mais bonita

paises = top10.index
masc = top10['Masculina']
fem = top10['Feminina']
x = np.arange(len(paises))

# --- Matplotlib  ---
plt.figure(figsize=(12, 6))
plt.bar(x, masc, label='Masculina')
plt.bar(x, fem, bottom=masc, label='Feminina')
plt.xticks(x, paises, rotation=45, ha='right')
plt.xlabel('País')
plt.ylabel('Número de copas disputadas')
plt.title('Top 10 países com mais participações em Copas (Matplotlib)')
plt.legend()
plt.tight_layout()
plt.show()

# --- Seaborn  ---
plt.figure(figsize=(12, 6))
ax = plt.gca()
ax.bar(x, masc, label='Masculina')
ax.bar(x, fem, bottom=masc, label='Feminina')
ax.set_xticks(x)
ax.set_xticklabels(paises, rotation=45, ha='right')
ax.set_xlabel('País')
ax.set_ylabel('Número de copas disputadas')
ax.set_title('Top 10 países com mais participações em Copas (Seaborn)')
ax.legend()
plt.tight_layout()
plt.show()

# --- Plotly  ---
top10_plotly = top10.reset_index(names='país')
fig = px.bar(
    top10_plotly,
    x='país',
    y=['Masculina', 'Feminina'],
    title='Top 10 países com mais participações em Copas (Plotly)',
    labels={'value': 'Número de copas disputadas', 'variable': 'Copa'}
)
fig.update_layout(barmode='stack', xaxis_tickangle=-45)
fig.show()


# ============================================================
# 4) DASHBOARD COM 4 SUBPLOTS (USANDO MATPLOTLIB)
#    2 linhas x 2 colunas:
#     (1,1) barras com quantidade de jogos por ano
#     (1,2) área com gols_1 e gols_2 por ano
#     (2,1) área com cartões amarelos e vermelhos por ano
#     (2,2) barras com total de gols contra por ano
# ============================================================



# jogos por ano
jogos_por_ano = wc.groupby('ano').size()

# gols por ano (casa e visitante)
gols_por_ano = wc.groupby('ano')[['gols_1', 'gols_2']].sum()

# função genérica para contar eventos em colunas textuais tipo lista
def conta_eventos_lista(valor):
    if pd.isna(valor):
        return 0
    try:
        lista = ast.literal_eval(str(valor))
        return len(lista)
    except (SyntaxError, ValueError):
        return 0

# cartões amarelos
wc['num_amarelo_1'] = wc['cartao_amarelo_1'].apply(conta_eventos_lista)
wc['num_amarelo_2'] = wc['cartao_amarelo_2'].apply(conta_eventos_lista)
wc['amarelos_total'] = wc['num_amarelo_1'] + wc['num_amarelo_2']

# cartões vermelhos
wc['num_vermelho_1'] = wc['cartao_vermelho_1'].apply(conta_eventos_lista)
wc['num_vermelho_2'] = wc['cartao_vermelho_2'].apply(conta_eventos_lista)
wc['vermelhos_total'] = wc['num_vermelho_1'] + wc['num_vermelho_2']

cartoes_por_ano = wc.groupby('ano')[['amarelos_total', 'vermelhos_total']].sum()

# gols contra (own goals)
wc['num_contra_1'] = wc['gols_1_contra'].apply(conta_eventos_lista)
wc['num_contra_2'] = wc['gols_2_contra'].apply(conta_eventos_lista)
wc['contra_total'] = wc['num_contra_1'] + wc['num_contra_2']
gols_contra_por_ano = wc.groupby('ano')['contra_total'].sum()

# ---------- criação dos subplots -----------

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# (1,1) barras com quantidade de jogos por ano
ax1 = axes[0, 0]
ax1.bar(jogos_por_ano.index, jogos_por_ano.values)
ax1.set_title('Quantidade de jogos por ano')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Número de jogos')

# (1,2) área com gols_1 e gols_2 por ano
ax2 = axes[0, 1]
ax2.stackplot(
    gols_por_ano.index,
    gols_por_ano['gols_1'],
    gols_por_ano['gols_2'],
    labels=['Gols time 1 (casa)', 'Gols time 2 (visitante)']
)
ax2.set_title('Total de gols por ano')
ax2.set_xlabel('Ano')
ax2.set_ylabel('Número de gols')
ax2.legend(loc='upper left')

# (2,1) área com cartões amarelos e vermelhos por ano
ax3 = axes[1, 0]
ax3.stackplot(
    cartoes_por_ano.index,
    cartoes_por_ano['amarelos_total'],
    cartoes_por_ano['vermelhos_total'],
    labels=['Cartões amarelos', 'Cartões vermelhos']
)
ax3.set_title('Total de cartões por ano')
ax3.set_xlabel('Ano')
ax3.set_ylabel('Número de cartões')
ax3.legend(loc='upper left')

# (2,2) barras com gols contra por ano
ax4 = axes[1, 1]
ax4.bar(gols_contra_por_ano.index, gols_contra_por_ano.values)
ax4.set_title('Total de gols contra por ano')
ax4.set_xlabel('Ano')
ax4.set_ylabel('Número de gols contra')

plt.tight_layout()
plt.show()
