from django.core.management.base import BaseCommand

from neomodel import db


class Command(BaseCommand):
    help = 'Clear the neo4j database'

    def handle(self, *args, **options):
        self.stdout.write('Deleting all nodes..\n')
        db.clear_neo4j_database(True, True)
        self.stdout.write('Done.\n')