from django.contrib import admin
from django.urls import path, include
from core.views import index, login_view, register_view, item_detail_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("wallet/", include("wallet.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("items/<int:pk>/", item_detail_view, name="item-detail-page"),
    path("", include("market.urls")),
    path("", index, name="home"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
