from django.shortcuts import render, get_object_or_404, redirect 
from content.models import Lesson
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from user_profile.models import ChildProfile 
from django.contrib.auth import logout

def main_screen(request):
    user = request.user
    child_profile = None
    lessons = Lesson.objects.all()  

    if user.is_authenticated:
        try:
            child_profile = ChildProfile.objects.get(user=user)
        except ChildProfile.DoesNotExist:
            pass  # отсутствие профиля

    return render(request, 'core/main_screen.html', {
        'child_profile': child_profile,
        'lessons': lessons,
    })


def learning_screen(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'core/learning_screen.html', {'lesson': lesson})

def login_register(request):
    return render(request, 'core/login_register.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            selected_interests = form.cleaned_data.get('interests', [])  # Получаем выбранные интересы

            # Создаем пользователя
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)  # Вход в систему после создания пользователя

            # Создайте профиль после успешной регистрации
            profile = ChildProfile.objects.create(user=user, level='Начальный')

            # Устанавливаем интересы, если они были выбраны
            if selected_interests:
                profile.interests.set(selected_interests)  # Устанавливаем интересы

            return redirect('main_screen')  
    else:
        form = UserRegistrationForm()

    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user) 
                return redirect('main_screen')  
            else:
                form.add_error(None, "Неверное имя пользователя или пароль.")
    else:
        form = UserLoginForm()

    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request) 
    return redirect('login_register') 