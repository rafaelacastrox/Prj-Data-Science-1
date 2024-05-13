import pandas as pd

dados_orgaos = pd.read_csv('lista_de_espera.csv', encoding='latin1')

prioridade_sim = dados_orgaos[dados_orgaos['prior_transplant'] == 'SIM']

# Salvar os casos com prioridade "SIM" em uma nova tabela
prioridade_sim.to_csv('casos_prioridade_sim.csv', index=False)