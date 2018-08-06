from django.contrib import admin
from django.urls import path, include
from landingpage.views import landingpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingpage, name='landingpage'), #sends user right to landing view in main
    path('accounts/', include('accounts.urls')),
    path('companies/', include('companies.urls')),
    path('explore/', include('explore.urls'))

]

