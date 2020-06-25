
from django.urls import include, path
from Form import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('Form/', include('Form.urls')),
    path('', views.form)
]
