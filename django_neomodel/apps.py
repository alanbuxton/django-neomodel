from django.apps import AppConfig
from django.conf import settings
from neomodel import get_config


class NeomodelConfig(AppConfig):
    name = "django_neomodel"
    verbose_name = "Django neomodel"

    def read_settings(self):
        config = get_config()
        config.database_url = getattr(
            settings, "NEOMODEL_NEO4J_BOLT_URL", config.database_url
        )
        config.force_timezone = getattr(settings, "NEOMODEL_FORCE_TIMEZONE", False)
        config.max_connection_pool_size = getattr(
            settings,
            "NEOMODEL_MAX_CONNECTION_POOL_SIZE",
            config.max_connection_pool_size,
        )

    def ready(self):
        self.read_settings()
