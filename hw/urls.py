"""
URL configuration for hw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from app.views import client_orders, add_product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/<int:client_id>/orders/', client_orders, name='client_orders'),
    path('product/add_product/', add_product, name='add_product'),
    path(
        'product/add_product/success_page',
        TemplateView.as_view(template_name='success_page.html'),
        name='add_product_success_page'
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
