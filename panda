
import pandas as pd
import numpy as np
from collections import Counter
import ast

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 12)

wcwomen_df = pd.read_csv('matches_1991_2023.csv')
wcmen_df   = pd.read_csv('matches_1930_2022.csv')

wc = pd.concat((wcwomen_df, wcmen_df)).reset_index(drop=True)

nomes_traduzidos = {
    'home_team': 'time_1',
    'away_team': 'time_2',
    'home_score': 'gols_1',
    'away_score': 'gols_2',
    'Date': 'data',
    'Year': 'ano',
    'Host': 'país_sede',
    'Attendance': 'comparecimento',
    'Score': 'resultado',
    'Round': 'rodada',
    'home_goal': 'gols_1_detalhes',
    'away_goal': 'gols_2_detalhes',
    'home_own_goal': 'gols_1_contra',
    'away_own_goal': 'gols_2_contra',
    'home_penalty_goal': 'gols_1_penalti',
    'away_penalty_goal': 'gols_2_penalti',
    'home_red_card': 'cartao_vermelho_1',
    'away_red_card': 'cartao_vermelho_2',
    'home_yellow_card': 'cartao_amarelo_1',
    'away_yellow_card': 'cartao_amarelo_2',
    'Gender': 'copa',         
}

wc = wc.rename(columns=nomes_traduzidos)

wc['copa'] = wc['copa'].replace({'Men': 'Masculina', 'Women': 'Feminina'})

print('Primeiras linhas do wc:')
display(wc.head())

# ============================================================
# ATIVIDADE 1 - AJUSTAR TIPOS E SALVAR wc_formatado.csv
# ============================================================

wc['data'] = pd.to_datetime(wc['data'])

for col in ['gols_1', 'gols_2', 'ano']:
    wc[col] = wc[col].astype('int64')

wc['comparecimento'] = (
    wc['comparecimento']
      .astype('string')
      .str.replace('.', '', regex=False)
      .str.replace(',', '', regex=False)
)
wc['comparecimento'] = wc['comparecimento'].astype('int64')

cols_string = [
    'time_1', 'time_2', 'país_sede', 'resultado',
    'gols_1_detalhes', 'gols_2_detalhes',
    'gols_1_contra', 'gols_2_contra',
    'gols_1_penalti', 'gols_2_penalti',
    'cartao_vermelho_1', 'cartao_vermelho_2',
    'cartao_amarelo_1', 'cartao_amarelo_2',
    'copa'
]
wc[cols_string] = wc[cols_string].astype('string')

wc['rodada'] = wc['rodada'].astype('category')

print('\nINFO DO DATAFRAME APÓS CONVERSÕES:')
wc.info()

wc.to_csv('wc_formatado.csv', index=False)
print('\nArquivo wc_formatado.csv salvo com sucesso!')

# ============================================================
# ATIVIDADE 2 - JOGO COM MAIOR AUDIÊNCIA (MAIOR COMPARECIMENTO)
# ============================================================

idx_max_publico = wc['comparecimento'].idxmax()
jogo_maior_publico = wc.loc[[idx_max_publico]]  

print('\n=== JOGO COM MAIOR PÚBLICO DA HISTÓRIA ===')
display(jogo_maior_publico)

# ============================================================
# ATIVIDADE 3 - QUANTAS COPAS MASCULINAS E FEMININAS
# ============================================================

copas_unicas = wc[['ano', 'copa']].drop_duplicates()
copas_por_tipo = copas_unicas['copa'].value_counts()

print('\n=== QUANTIDADE DE COPAS POR TIPO ===')
print('Masculina:', int(copas_por_tipo.get('Masculina', 0)))
print('Feminina :', int(copas_por_tipo.get('Feminina', 0)))
print('\nDetalhe do value_counts():')
print(copas_por_tipo)

# ============================================================
# ATIVIDADE 4 - DATAFRAME participacao (país, copa, num_copas)
#            + TOP 5 DE CADA COMPETIÇÃO
# ============================================================

part1 = wc[['time_1', 'ano', 'copa']].rename(columns={'time_1': 'país'})
part2 = wc[['time_2', 'ano', 'copa']].rename(columns={'time_2': 'país'})

participacoes = pd.concat([part1, part2], ignore_index=True)

participacoes = participacoes.drop_duplicates()

participacao = (
    participacoes
      .groupby(['país', 'copa'])
      .size()
      .reset_index(name='num_copas')
)

print('\n=== DATAFRAME participacao (primeiras linhas) ===')
display(participacao.head())

top5_fem = (
    participacao[participacao['copa'] == 'Feminina']
      .sort_values('num_copas', ascending=False)
      .head(5)
)

print('\n=== TOP 5 PARTICIPAÇÕES - COPA FEMININA ===')
display(top5_fem)

top5_masc = (
    participacao[participacao['copa'] == 'Masculina']
      .sort_values('num_copas', ascending=False)
      .head(5)
)

print('\n=== TOP 5 PARTICIPAÇÕES - COPA MASCULINA ===')
display(top5_masc)

# ============================================================
# ATIVIDADE 5 - DATAFRAME gols (país, total_gols)
# ============================================================

gols_casa = wc[['time_1', 'gols_1']].rename(columns={'time_1': 'país', 'gols_1': 'gols'})
gols_fora = wc[['time_2', 'gols_2']].rename(columns={'time_2': 'país', 'gols_2': 'gols'})

gols = pd.concat([gols_casa, gols_fora], ignore_index=True)

gols = (
    gols
      .groupby('país')['gols']
      .sum()
      .reset_index(name='total_gols')
      .sort_values('total_gols', ascending=False)
)

print('\n=== DATAFRAME gols (país x total_gols) ===')
display(gols.head(20))   

# ============================================================
# ATIVIDADE 6 - PAÍS QUE TOMOU MAIS CARTÕES AMARELOS
# ============================================================

def conta_cartoes(valor):
    """Recebe a string da lista de cartões e devolve a quantidade."""
    if pd.isna(valor):
        return 0
    lista = ast.literal_eval(str(valor))
    return len(lista)

wc['num_cartoes_1'] = wc['cartao_amarelo_1'].apply(conta_cartoes)
wc['num_cartoes_2'] = wc['cartao_amarelo_2'].apply(conta_cartoes)

cartoes_casa = wc[['time_1', 'num_cartoes_1']].rename(
    columns={'time_1': 'país', 'num_cartoes_1': 'cartoes'}
)
cartoes_fora = wc[['time_2', 'num_cartoes_2']].rename(
    columns={'time_2': 'país', 'num_cartoes_2': 'cartoes'}
)

cartoes = pd.concat([cartoes_casa, cartoes_fora], ignore_index=True)

cartoes_pais = (
    cartoes
      .groupby('país')['cartoes']
      .sum()
      .reset_index(name='cartoes_amarelos')
      .sort_values('cartoes_amarelos', ascending=False)
)

print('\n=== TOP 10 PAÍSES COM MAIS CARTÕES AMARELOS ===')
display(cartoes_pais.head(10))

print('\nPaís com mais cartões amarelos:')
display(cartoes_pais.iloc[[0]])

# ============================================================
# ATIVIDADE 7 - TOP 10 JOGADORES COM MAIS GOLS EM COPAS
#              (GOLS NORMAIS + GOLS DE PÊNALTI)
# ============================================================

colunas_gols = [
    'gols_1_detalhes', 'gols_2_detalhes',
    'gols_1_penalti',  'gols_2_penalti'
]

contagem = Counter()

for col in colunas_gols:
    for valor in wc[col].dropna():
        if not isinstance(valor, str):
            valor = str(valor)
        gols_partida = valor.split('|')
        for gol in gols_partida:
            gol = gol.strip()
            if not gol:
                continue
            
            nome = gol.split('·', 1)[0].strip()
            contagem[nome] += 1

gols_jogadores = (
    pd.DataFrame.from_dict(contagem, orient='index', columns=['num_gols'])
      .reset_index()
      .rename(columns={'index': 'jogador(a)'})
      .sort_values('num_gols', ascending=False)
)

print('\n=== TOP 10 ARTILHEIROS/ARTILHEIRAS DE COPAS ===')
display(gols_jogadores.head(10))
