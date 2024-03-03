from django.core.management import BaseCommand

from collects.factory_collects import CollectFactory


class Command(BaseCommand):
    help = 'Команда добавляет нужное количество объектов Collects'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            help='Количество записей, которые необходимо создать'
        )

    def handle(self, *args, **options):
        count = options['count']
        for _ in range(count):
            CollectFactory.create()
        self.stdout.write(self.style.SUCCESS(f'Создано {count} записей'))
