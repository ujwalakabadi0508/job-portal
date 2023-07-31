from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name = "src"

urlpatterns = [
    path("", home  ,name="home"),
    path("job-view/<int:id>/", job_view  ,name="job_view"),
    path("job-apply/<int:id>/", job_apply  ,name="job_apply"),
    path('logout/', logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register_candidate, name='register'),
    path('candidate-profile/', candidate_profile, name='candidate_profile'),
    path('candidate_profile_update/', candidate_profile_update, name='candidate_profile_update')
]
