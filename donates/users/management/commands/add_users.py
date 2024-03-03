from django.core.management import BaseCommand

from users.factories import UserFactory


class Command(BaseCommand):
    help = 'Команда добавляет нужное количество пользователей'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            type=int,
            help='Количество записей, которые необходимо создать'
        )

    def handle(self, *args, **options):
        count = options['count']
        for _ in range(count):
            UserFactory.create()
        self.stdout.write(self.style.SUCCESS(f'Создано {count} пользователей'))
