from django.urls import path, include
from api import views as api_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

app_name = "api"


urlpatterns = [
    path("<str:UF>/cidades/<str:city_name>", api_views.get_cidades_by_estado, name="cidadeByEstado"),
    path("imoveis/<str:UF>/<str:city_name>", api_views.get_imoveis, name="getImoveis"),
    path("meusImoveis", api_views.meusImoveis, name="meusImoveis"),
    path("imovel/<int:id>", api_views.getImovel, name="imvoelById")
]

urlpatterns += [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

schema_view = get_schema_view(
   openapi.Info(
      title="API ALUGAAQUI",
      default_version='v1',
      description="Documentação Aluga Aqui",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alugaaqui@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]