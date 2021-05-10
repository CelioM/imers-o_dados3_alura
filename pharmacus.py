# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 

farmacosDf = pd.read_csv('./data/dados_experimentos.csv')


# %%
farmacosDf.head()

# %% [markdown]
# ### Desafio 1: Pq classe de tratamento é tão desbalanceado?

# %%
treatment = farmacosDf['tratamento'].value_counts(normalize=True)
treatment

# %% [markdown]
# ### Desafio 2: Proporção das classes de tratamento

# %%


# %% [markdown]
# ### Desafio 3: Quantos tipos de drogas foram investigados?

# %%
drugs_filtered = farmacosDf['droga'].unique().size
drugs_filtered

# %% [markdown]
# ### Desafio 4: Procurar na documentação o metodo query

# %%


# %% [markdown]
# ### Desafio 5: Renomear as colunas tirando o hífen

# %%
import re

hifen_columns = farmacosDf.loc[farmacosDf.columns].str.contains()


# %%



