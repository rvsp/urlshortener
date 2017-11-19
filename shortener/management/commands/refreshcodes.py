from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll

from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'refresh all KirrURL shortcode'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcode(items=options['items'])    