from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Object$', views.ShowObject.as_view(), name='show_self'),
    url(r'^Object/edit$', views.EditObject.as_view(), name='edit_self'),
#     url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),
#         name='show'),
  ]
