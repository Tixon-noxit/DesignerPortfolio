from django.conf.urls.static import static
from django.urls import path
from .views import MironovAbout

app_name = "about"

urlpatterns = [
    path('', MironovAbout.as_view(), name='About'),

]