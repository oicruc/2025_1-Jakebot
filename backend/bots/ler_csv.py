import pandas as pd
import json
import sys
import os

if len(sys.argv) < 2:
    print("Uso: python ler_csv.py caminho/do/arquivo.csv")
    sys.exit(1)

csv_path = sys.argv[1]

df = pd.read_csv(csv_path, encoding='utf-8')

df_filtrado = df[['Decidim Commentable ID', 'Body']].copy()


def extrair_comentario(body):
    try:
        return json.loads(body).get("pt-BR", "")
    except Exception:
        return body


df_filtrado['Body'] = df_filtrado['Body'].apply(extrair_comentario)

os.makedirs('assets', exist_ok=True)

df_filtrado.to_csv(r'assets/Comentários_por_ID.csv',
                   index=False, encoding='utf-8')

df = pd.read_csv(r'assets/Comentários_por_ID.csv', encoding='utf-8')

df_grouped = df.groupby('Decidim Commentable ID')[
    'Body'].apply(list).reset_index()

resultado_json = df_grouped.to_dict(orient='records')

with open('Comentarios_por_ID.json', 'w', encoding='utf-8') as f:
    json.dump(resultado_json, f, ensure_ascii=False, indent=2)
