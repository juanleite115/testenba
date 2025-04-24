import matplotlib.pyplot as plt
import seaborn as sns

# Exemplo: Gráfico de barras
def graf_barras():
    sns.barplot(x='GROUP_VALUE', y='W_PCT', data=df)
    plt.title('Porcentagem de Vitórias por Tipo de Jogo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#BAIXAR OS DADOS EM CSV
#df = pd.read_csv("nba_team_stats.csv")
