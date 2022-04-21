import secrets

from django.core.management.base import BaseCommand

from promocodegen.models import PromoCode


class CreatePromoCommand(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('amount', nargs='+', type=int)
        parser.add_argument('group', type=str)

    def handle(self, *args, **options):
        amount, group = options['amount'], options['group']
        for _ in amount:
            code = PromoCode.objects.create(group=group)
            code.save()
            code_id = str(code.id)
            code_symbols = "ABCDEFGHJKLMNPQRSTVWXYZ1234567890"
            random_string = "".join(secrets.choice(code_symbols) for _ in range(12))
            code.code = (random_string + code_id)[-12:]
            code.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully create {amount} promocodes for {group} group"))