"""dance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from dance import settings
from home_page import views as home_page_views
from static_pages import views as static_pages_views
from locations import views as locations_views
from event_scheme import views as events_views
from classes import views as classes_views
from articles import views as articles_views
from dance_styles import views as dance_styles_views
from should_know import views as should_know_views
from videos import views as videos_views
from audios import views as audios_views
from photos import views as photos_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page_views.index),
    url(r'^should-know/$', should_know_views.should_know_show),
    url(r'^about/$', static_pages_views.about_show),
    url(r'^contacts/$', static_pages_views.contacts_show),
    url(r'^dance-party-calendar/$', static_pages_views.dance_party_calendar_show),
    url(r'^locations/', include([
        url(r'^$', locations_views.locations_show),
    ])),
    url(r'^events/', include([
        url(r'^$', events_views.events_show),
        url(r'^(?:event-(?P<event_id>\d+)/)?$', events_views.event_show),
    ])),

    url(r'^classes/$', classes_views.classes_show),
    url(r'^articles/', include([
        url(r'^$', articles_views.article_list_show),
        url(r'^(?:article-(?P<article_id>\d+)/)?$', articles_views.article_show),
    ])),
    url(r'^videos/$', videos_views.videos_show),
    url(r'^audios/$', audios_views.audios_show),
    url(r'^photos/$', photos_views.photos_show),
    url(r'^dance-styles/', include([
        url(r'^$', dance_styles_views.dance_styles_show),
    ]))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'mysite.views.my_custom_page_not_found_view'
# handler500 = 'mysite.views.my_custom_error_view'
# handler403 = 'mysite.views.my_custom_permission_denied_view'
# handler400 = 'mysite.views.my_custom_bad_request_view'
