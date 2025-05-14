from django.core.management.base import BaseCommand
import pandas as pd
import os


class Command(BaseCommand):
    help = 'Lê um arquivo CSV e imprime as primeiras linhas'

    def add_arguments(self, parser):
        parser.add_argument('caminho_csv', type=str, help='Caminho do csv')
        parser.add_argument('--output', type=str,
                            help='Nome do arquivo JSON de saida')

    def handle(self, *args, **kwargs):
        caminho_csv = kwargs['caminho_csv']
        output_path = kwargs.get('output')

        if not os.path.exists(caminho_csv):
            self.stderr.write(self.style.ERROR(
                f"Arquivo nao encontrado: {caminho_csv}"))
            return

        try:
            df = pd.read_csv(caminho_csv, encoding='utf-8')

            if not output_path:
                output_path = os.path.splitext(caminho_csv)[0] + '.json'

            df.to_json(output_path, orient='records',
                       force_ascii=False, indent=2)

            self.stdout.write(self.style.SUCCESS(
                f"Arquivo JSON salvo em: {output_path}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f"Erro ao processar o CSV: {e}"))
