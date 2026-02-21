from django import setup as setup_django
from django.core.management.base import BaseCommand

from neomodel import db


class Command(BaseCommand):
    help = 'Install labels and constraints for your neo4j database'

    def handle(self, *args, **options):
        setup_django()
        db.install_all_labels(stdout=self.stdout)