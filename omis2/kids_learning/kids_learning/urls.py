from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import login_register, register, user_login, main_screen, logout_view
from content.views import learning_screen, test_list, test_detail, submit_test, my_lessons_view
from user_profile.views import profile_view, achievements_view, settings_view, edit_profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_register, name='login_register'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('main_screen/', main_screen, name='main_screen'),
    path('lesson/<int:lesson_id>/', learning_screen, name='learning_screen'), 
    path('tests/', test_list, name='test_list'),
    path('test/<int:test_id>/', test_detail, name='test_detail'),
    path('test/<int:test_id>/submit/', submit_test, name='submit_test'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('my_lessons/', my_lessons_view, name='my_lessons'),
    path('achievements/', achievements_view, name='achievements'),
    path('user_settings/', settings_view, name='user_settings'),
    path('user_settings/edit-profile/', edit_profile_view, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)