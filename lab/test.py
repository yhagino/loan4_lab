# -*- coding:utf-8 -*-
from django.conf import settings
settings.configure()
from django.http import QueryDict


dct = QueryDict('loantime_id=1&limit_id=50&sokujitu=1&diff=aiful&diff=mobit')
get_param = dict(dct)
query_l = []