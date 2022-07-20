from .base import *

ALLOWED_HOSTS = ['13.124.30.106']
STATIC_ROOT = BASE_DIR / 'static/'                  #  /home/ubuntu/projects/mysite/static 등록
STATICFILES_DIRS = []                               # base.py에 정의된 것 가져옴.