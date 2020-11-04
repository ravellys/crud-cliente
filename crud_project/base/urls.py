from django.urls import path

from crud_project.base.views import HomeTemplateView

app_name = 'base'
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
]
