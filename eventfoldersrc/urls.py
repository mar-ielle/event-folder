from django.conf.urls import url
from eventfoldersrc import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^venues/$', views.VenuesPageView.as_view()),
	url(r'^caterings/$', views.CateringsPageView.as_view()),
	url(r'^lightssounds/$', views.LightsAndSoundsPageView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)