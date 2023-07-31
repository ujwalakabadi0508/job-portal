from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import login, authenticate ,logout as deauth
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import RegistrationForm , ApplyForm , Candidate_update

def register_candidate(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save user information
            user = form.save()
            
            # Save candidate information
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            candidate.objects.create(user=user, name=name, email=email, phone=phone)
            messages.success(request , "You account created Successfully ")
            return redirect('src:login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
        
    return render(request, 'register.html', {'form': form})

# Create your views here.
def home(request):
    user_type = ''
    if request.user.is_authenticated:
        pass
    
    # Get all jobs

    if request.POST:
        query_type = request.POST.get('query_type')
        query = request.POST.get('search_key')
        if query_type == 'category':
            all_jobs = new_job.objects.filter(category__category__contains= query)
        elif query_type == 'location':
            all_jobs = new_job.objects.filter(city__city_name__contains = query)
        else:
            all_jobs = []
    else:
        all_jobs = new_job.objects.all()

    # Set the number of jobs to display per page
    jobs_per_page = 3

    # Create a Paginator object
    paginator = Paginator(all_jobs, jobs_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'type': user_type,
    }    

    return render(request, 'home.html', context)


def job_view(request , id):
    return render(request,'job_view.html', {'job':new_job.objects.get(id=id)})

def job_apply(request , id):
    get_user=candidate.objects.get(user=request.user)
    job = new_job.objects.get(id=id)
    if applied_job.objects.filter(new_job_id__id=id ,candidate_id=get_user ).exists():
        messages.success(request , "You have alredy applied to this job")
        return redirect("src:job_view" , id)

    form=ApplyForm()
    if request.POST:
        job = new_job.objects.get(id=id)
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.new_job_id = job
            new_form.candidate_id = get_user
            new_form.save()
            messages.success(request , "You have applied Successfully")

            return redirect("src:job_view" , id)
        else:
            form=ApplyForm()


    return render(request,'job_apply.html',{'form':form , 'job':job} )

def logout_view(request):
    deauth(request)
    messages.success(request , "You are Logout Successfully")
    return redirect('src:home')


def candidate_profile(request):
    get_user = candidate.objects.get(user=request.user)
    applied_jobs=applied_job.objects.filter(candidate_id=get_user)

    context={
        'candidate': get_user ,
        'jobs': applied_jobs
    }
    return render(request , 'candidate-profile.html' , context)

def candidate_profile_update(request):

    get_user = candidate.objects.get(user=request.user)

    form = Candidate_update(instance=get_user)
    if request.POST:
        form = Candidate_update(request.POST , request.FILES , instance=get_user)
        if form.is_valid():
            form.save()
            messages.success(request , "Updated Successfully")
            return redirect('src:candidate_profile')
        else:
            form = Candidate_update(instance=get_user)

    return render(request , 'candidate-update.html' , {'form':form})    



  