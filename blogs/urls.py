# @Time    : 18-6-5 下午2:19
# @Author  : wengwenyu
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.conf.urls import url
from.views import index


urlpatterns = [
    url(r'^index/$', index, name='index'),
    # url(r'^search$', SearchView.as_view(), name='search'),
]
