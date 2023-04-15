from django.apps import AppConfig

# We also need to configure the signals (when we make another file called "signals.py")

class PostsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'posts'

    '''
    (configuring the signals)

    def ready(self):
        import base.signals

this code will only run if we add "appname.apps.AppnameConfig" in installed apps in settings.py'''
