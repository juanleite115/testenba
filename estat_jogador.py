from nba_api.stats.static import teams
from nba_api.stats.endpoints import CommonTeamRoster, PlayerCareerStats, PlayerDashboardByGeneralSplits
import pandas as pd

# Buscar ID do time (ex: Miami)
team_dict = teams.get_teams()
miami_id = [team['id'] for team in team_dict if team['full_name'] == 'Miami Heat'][0]

# Buscar elenco atual
roster = CommonTeamRoster(team_id=miami_id).get_data_frames()[0]

# Mostrar nomes e IDs dos jogadores
players = roster[['PLAYER', 'PLAYER_ID']]
#---------------------------------------------

from nba_api.stats.endpoints import PlayerDashboardByYearOverYear
import time
def stats():
    all_stats = []

    for _, row in players.iterrows():
        player_id = row['PLAYER_ID']
        player_name = row['PLAYER']
    
    # Evitar bloqueio por excesso de requisições
        time.sleep(1)

    # Buscar estatísticas da temporada
        try:
            stats = PlayerDashboardByYearOverYear(player_id=player_id).get_data_frames()[1]
            current_season = stats.iloc[-1]  # última temporada

            all_stats.append({
                'Player': player_name,
                'PTS': current_season['PTS'],
                'AST': current_season['AST'],
                'REB': current_season['REB'],
                'GP': current_season['GP']
            })
        except:
            print(f"Erro com jogador {player_name}")

# Criar DataFrame final
    df_players_stats = pd.DataFrame(all_stats)
    print(df_players_stats)
