from celery import Celery


class CeleryConf(object):
    BROKER_URL = 'redis://localhost:6379/2'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_IMPORTS = ('apps.tasks.tasks')


app = Celery('apps.tasks.conf')
app.config_from_object(CeleryConf)
