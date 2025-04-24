# scripts/analisar_dados.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico(file_path):
    df = pd.read_csv(file_path)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Player', y='AST', data=df, palette='Blues_d')
    plt.title("Assistências por Jogador")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visuals/grafico_assistencias.png")
    plt.show()
