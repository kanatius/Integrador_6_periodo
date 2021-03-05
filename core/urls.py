from django.urls import path
from core.views import index_page


urlpatterns = [
    path("", index_page.as_view(), name="index")
]