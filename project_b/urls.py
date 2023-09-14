from django.urls import path, re_path
from . import views
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'project_b'  # Define the app name

schema_view_register_license = get_schema_view(
    openapi.Info(
        title="Register License API",
        default_version='v1',
        description="API to register new licenses",
        terms_of_service="https://www.project_b.com/terms/register_license/",
        contact=openapi.Contact(email="contact@register_license.local"),
        license=openapi.License(name="License for Register API"),
    ),
    public=True,
    permission_classes=(),
)

schema_view_get_license = get_schema_view(
    openapi.Info(
        title="Get License API",
        default_version='v1',
        description="API to retrieve license information",
        terms_of_service="https://www.project_b.com/terms/get_license/",
        contact=openapi.Contact(email="contact@get_license.local"),
        license=openapi.License(name="License for Get API"),
    ),
    public=True,
    permission_classes=(),
)

schema_view_check_validity = get_schema_view(
    openapi.Info(
        title="Check Validity API",
        default_version='v1',
        description="API to check license validity",
        terms_of_service="https://www.project_b.com/terms/check_validity/",
        contact=openapi.Contact(email="contact@check_validity.local"),
        license=openapi.License(name="License for Check Validity API"),
    ),
    public=True,
    permission_classes=(),
)

urlpatterns = [
    path('register_license/', views.register_license, name='register_license'),
    path('get_license/<str:device_id>/<str:mac_address>/', views.get_license, name='get_license'),
    path('check_validity/<str:device_id>/<str:mac_address>/', views.check_validity, name='check_validity'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_register_license.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view_register_license.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view_register_license.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view_get_license.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

