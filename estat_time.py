from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamDashboardByGeneralSplits
import pandas as pd

# Pegar lista de times
nba_teams = teams.get_teams()
print(nba_teams[0])  # Exemplo de estrutura

# Escolher um time pelo ID (ex: Lakers)
lakers_id = [team['id'] for team in nba_teams if team['full_name'] == 'Los Angeles Lakers'][0]

# Buscar dados
team_stats = TeamDashboardByGeneralSplits(team_id=lakers_id)
df = team_stats.get_data_frames()[0]

# Visualizar
print(df.head())
df.to_csv("miami_heat.csv", index=False)