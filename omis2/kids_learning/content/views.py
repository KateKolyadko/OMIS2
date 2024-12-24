from django.shortcuts import render, get_object_or_404
from .models import Lesson
from .models import Test

def learning_screen(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    
    multimedia_url = lesson.multimedia.url if lesson.multimedia else 'Нет мультимедиа'
    print(multimedia_url)
    return render(request, 'content/learning_screen.html', {
        'lesson': lesson,
        'multimedia_url': multimedia_url  
    })

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'content/test_list.html', {'tests': tests})

def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions_list.all()  
    return render(request, 'content/test_detail.html', {'test': test, 'questions': questions})

def submit_test(request, test_id):
    if request.method == 'POST':
        test = get_object_or_404(Test, id=test_id)
        score = 0
        for question in test.questions_list.all():
            selected_answer = request.POST.get(f'question_{question.id}')
            if selected_answer == question.correct_answer:
                score += 1
        return render(request, 'content/test_result.html', {'score': score, 'total': test.questions_list.count()})
    
def my_lessons_view(request):
    lessons = Lesson.objects.all() 
    return render(request, 'my_lessons.html', {'lessons': lessons})

