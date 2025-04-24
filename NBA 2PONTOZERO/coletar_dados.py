# scripts/coletar_dados.py
from nba_api.stats.static import teams
from nba_api.stats.endpoints import CommonTeamRoster, PlayerDashboardByYearOverYear
import pandas as pd
import time

def coletar_dados_time(nome_time="Los Angeles Lakers"):
    team_id = [t["id"] for t in teams.get_teams() if t["full_name"] == nome_time][0]
    roster = CommonTeamRoster(team_id=team_id).get_data_frames()[0]
    players = roster[['PLAYER', 'PLAYER_ID']]

    all_stats = []
    for _, row in players.iterrows():
        time.sleep(1)
        try:
            stats = PlayerDashboardByYearOverYear(player_id=row['PLAYER_ID']).get_data_frames()[1]
            atual = stats.iloc[-1]
            all_stats.append({
                'Player': row['PLAYER'],
                'PTS': atual['PTS'],
                'AST': atual['AST'],
                'REB': atual['REB'],
                'GP': atual['GP']
            })
        except:
            continue

    df = pd.DataFrame(all_stats)
    df.to_csv(f"data/{nome_time.replace(' ', '_').lower()}_stats.csv", index=False)
    print("Dados salvos com sucesso!")

# Teste rápido (se rodar diretamente esse script)
if __name__ == "__main__":
    coletar_dados_time()
