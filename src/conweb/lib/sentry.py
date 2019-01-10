from django.conf import settings

client = None
raven_config = settings.RAVEN_CONFIG
if raven_config:
    from raven import Client
    client = Client(raven_config['dsn'])
