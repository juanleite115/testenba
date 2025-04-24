from nba_api.stats.static import teams
from nba_api.stats.endpoints import CommonTeamRoster, PlayerCareerStats, PlayerDashboardByGeneralSplits
import pandas as pd

# Buscar ID do time (ex: Miami)
def team_dict():
    team_dict = teams.get_teams()
    heat_id = [team['id'] for team in team_dict if team['full_name'] == "Miami Heat"][0]

# Buscar elenco atual
    roster = CommonTeamRoster(team_id=heat_id).get_data_frames()[0]

# Mostrar nomes e IDs dos jogadores
    players = roster[['PLAYER', 'PLAYER_ID']]
    print(players)
    print(team_dict)