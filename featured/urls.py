from django.conf.urls import patterns, url

from featured.views import FeaturedListView


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/(?P<model>(\w+\.\w+))/$', FeaturedListView.as_view(), name='featured_category_list'),
]
