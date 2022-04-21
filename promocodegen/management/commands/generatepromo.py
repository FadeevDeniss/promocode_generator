import secrets

from django.core import serializers
from django.core.management.base import BaseCommand

from promocodegen.models import PromoCode


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('amount', nargs='+', type=int)
        parser.add_argument('group', nargs='+', type=str)

    def handle(self, *args, **options):
        amount, group = options['amount'][0], options['group']
        JSON_serializer = serializers.get_serializer('json')
        json_serializer = JSON_serializer()
        for _ in range(amount):
            with open('promocodes.json', 'a') as out:
                code = PromoCode.objects.create(group=group)
                code.save()
                code_id = str(code.id)
                code_symbols = "ABCDEFGHJKLMNPQRSTVWXYZ1234567890"
                random_string = "".join(secrets.choice(code_symbols) for _ in range(12))
                code.code = (random_string + code_id)[-12:]
                code.save()

                json_serializer.serialize(PromoCode.objects.filter(id=code.id), fields='code', stream=out)

        self.stdout.write(self.style.SUCCESS(f"Successfully create {amount} promocodes for {group} group"))
