from django.conf.urls import include, url


urlpatterns = [
    url(r'^featured/', include('featured.urls')),
]
