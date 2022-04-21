from django.core.management import BaseCommand


class Command(BaseCommand):

				def add_arguments(self, parser):
								parser.add_argument('file', nargs='+', type=str)
								parser.add_argument('code', type=str)

				def handle(self, *args, **options):
								file, code = options['file'][0], options['code']
								with open(file, 'r') as result_file:
												for i in result_file:
																if i.count(code) > 1:
																				self.stderr.write(self.style.ERROR(f"Warning! Value not unique"))

												self.stdout.write(self.style.SUCCESS(f"Value are unique"))
