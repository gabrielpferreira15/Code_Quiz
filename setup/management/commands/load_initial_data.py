from django.core.management.base import BaseCommand
from django.core.management import call_command
from setup.models import Linguagem  # ← AJUSTE AQUI (era quiz.models)

class Command(BaseCommand):
    help = 'Load initial quiz data safely without duplicates'

    def handle(self, *args, **options):
        # Verifica se já existem dados (usando Linguagem como referência)
        if Linguagem.objects.exists():
            self.stdout.write(
                self.style.WARNING('Quiz data already exists. Skipping fixture load.')
            )
            return

        # Carrega fixtures apenas se banco estiver vazio
        try:
            self.stdout.write('Loading initial quiz data...')
            call_command('loaddata', 'setup/fixtures/quiz_data.json')
            self.stdout.write(
                self.style.SUCCESS('Quiz data loaded successfully!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error loading fixtures: {e}')
            )
            raise