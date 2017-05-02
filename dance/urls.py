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
from event_scheme import views as event_scheme_views
from classes import views as classes_views
from articles import views as articles_views
from static_pages import views as static_pages_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page_views.index),
    url(r'^event_scheme/', include([
        url(r'^$', event_scheme_views.event_scheme_show),
        url(r'^(?:event-(?P<event_id>\d+)/)?$', event_scheme_views.event_show),
    ])),
    url(r'^about/$', static_pages_views.about_show),
    url(r'^contacts/$', static_pages_views.contacts_show),
    url(r'^classes/$', classes_views.classes_show),
    url(r'^articles/$', articles_views.article_list_show)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = 'mysite.views.my_custom_page_not_found_view'
# handler500 = 'mysite.views.my_custom_error_view'
# handler403 = 'mysite.views.my_custom_permission_denied_view'
# handler400 = 'mysite.views.my_custom_bad_request_view'
