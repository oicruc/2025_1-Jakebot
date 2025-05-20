import csv
import json
from datetime import datetime

def processar_csv_para_json(nome_arquivo_csv, nome_arquivo_json):
    # Lê o arquivo CSV
    with open(nome_arquivo_csv, mode='r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        comentarios = []
        
        for linha in leitor_csv:
            # Pula entradas que não são comentários (se necessário)
            if linha['Decidim Commentable Type'] != 'Decidim::Comments::Comment':
                continue
                
            # Converte a data de criação
            data_criacao = datetime.fromisoformat(linha['Created At'])
            
            # Extrai o corpo do comentário (tratando a string tipo JSON)
            corpo = linha['Body']
            try:
                # O corpo está armazenado como uma string JSON como {"pt-BR": "texto do comentário"}
                corpo_dict = json.loads(corpo.replace('""', '"'))
                texto_comentario = corpo_dict.get('pt-BR', '')
            except:
                texto_comentario = corpo
                
            comentario = {
                'id': linha['ID'],
                'id_comentavel': linha['Decidim Commentable ID'],
                'id_autor': linha['Decidim Author ID'],
                'data_criacao': linha['Created At'],
                'corpo': texto_comentario,
                'nivel': linha['Depth'],
                'alinhamento': linha['Alignment'],
                'id_comentavel_raiz': linha['Decidim Root Commentable ID'],
                'tipo_comentavel_raiz': linha['Decidim Root Commentable Type']
            }
            comentarios.append(comentario)
    
    # Ordena os comentários por data de criação
    comentarios.sort(key=lambda x: x['data_criacao'])
    
    # Escreve no arquivo JSON
    with open(nome_arquivo_json, 'w', encoding='utf-8') as arquivo_json:
        json.dump(comentarios, arquivo_json, ensure_ascii=False, indent=2)

# Uso
nome_arquivo_csv = 'backend/bots/assets/query_result_2025-04-28T13_17_30.156542Z.csv'
nome_arquivo_json = 'backend/bots/comentarios_organizados.json'
processar_csv_para_json(nome_arquivo_csv, nome_arquivo_json)

print(f"Os comentários foram organizados e salvos em {nome_arquivo_json}")
