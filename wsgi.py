import django.core.handlers.wsgi
import sys

sys.path.append('/home/georg/projects/d/t/')

application = django.core.handlers.wsgi.WSGIHandler()