from django.contrib import admin
from user_profile.models import ChildProfile
from assessment.models import Assessment
from feedback.models import Feedback

admin.site.register(ChildProfile)
admin.site.register(Assessment)
admin.site.register(Feedback)