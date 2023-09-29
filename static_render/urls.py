from django.urls import path
from .views import static_home, portfolio


urlpatterns = [
    path('portfolio/', portfolio),
    path("", static_home)
]
