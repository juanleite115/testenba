# main.py
from scripts.coletar_dados import coletar_dados_time
from scripts.analisar_dados import gerar_grafico

if __name__ == "__main__":
    nome_time = "Los Angeles Lakers"
    coletar_dados_time(nome_time)
    gerar_grafico(f"data/{nome_time.replace(' ', '_').lower()}_stats.csv")
