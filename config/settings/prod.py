from .base import *

# AWS에서의 접속 관련

ALLOWED_HOSTS = ['13.124.30.106']
STATIC_ROOT = BASE_DIR / 'static/'                  #  /home/ubuntu/projects/mysite/static 등록
STATICFILES_DIRS = []                               # base.py에 정의된 것 가져옴.
DEBUG = False                                       # 오류발생시 디버그모드(코드노출)를 막는다.