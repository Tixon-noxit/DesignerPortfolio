# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u11111111/data/www/offmaxline.ru/mironov_site')
sys.path.insert(1, '/var/www/u11111111/data/mironov/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mironov_site.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()