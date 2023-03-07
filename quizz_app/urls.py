from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path("", include('quizz.urls', namespace='quizz'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Quizz App Administration"
admin.site.site_title = "Quizz App Admin Portal"
admin.site.index_title = "Welcome to Quizz App Admin Portal"
