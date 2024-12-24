from django.shortcuts import render, get_object_or_404, redirect
from .models import ChildProfile, Achievement, Interest
from django.contrib.auth.decorators import login_required

def profile_view(request, user_id):
    child_profile = get_object_or_404(ChildProfile, user__id=user_id)
    return render(request, 'user_profile/profile.html', {'child_profile': child_profile})

def achievements_view(request):
    achievements = Achievement.objects.filter(child_profile=request.user.childprofile)
    return render(request, 'user_profile/achievements.html', {'achievements': achievements})

@login_required
def settings_view(request):
    return render(request, 'user_profile/user_settings.html')



@login_required
def edit_profile_view(request):
    if not hasattr(request.user, 'СhildЗrofile'):
        print("stop")
    profile = request.user.childprofile
    interests = Interest.objects.all() 

    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.email = request.POST.get('email')

        selected_interests = request.POST.getlist('interests')
        profile.interests.set(selected_interests)
        profile.save()

        print("Профиль сохранен:", profile.name, profile.email, profile.interests.all())  # Для отладки
        return redirect('user_settings') 

    return render(request, 'user_profile/edit_profile.html', {
        'profile': profile,
        'interests': interests  
    })