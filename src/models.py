from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class job_category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class city(models.Model):
    city_name =  models.CharField(max_length=100)
    def __str__(self):
        return self.city_name
    
    class Meta:
        ordering = ['city_name']


class new_job(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    city        = models.ForeignKey(city , on_delete=models.CASCADE)
    salary      = models.PositiveIntegerField()
    company     = models.CharField(max_length=100)
    contact     = models.CharField(max_length=100)
    email       = models.EmailField()
    address     = models.CharField(max_length=100)
    category    = models.ForeignKey(job_category , on_delete=models.CASCADE)
    
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class candidate(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE , related_name='candidate')
    name       = models.CharField(max_length=100)
    email      = models.EmailField( null=True, blank=True, )
    phone      = models.PositiveIntegerField( null=True, blank=True, )
    profile     = models.ImageField(upload_to='Profile/' ,default="default.png" )
    
    
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class applied_job(models.Model):
    new_job_id      = models.ForeignKey(new_job, on_delete=models.CASCADE , related_name='new_job')
    candidate_id    = models.ForeignKey(candidate, on_delete=models.CASCADE , related_name='candidate')
    city            = models.ForeignKey(city , on_delete=models.CASCADE)
    address         = models.CharField(max_length=100 )
    experience      = models.CharField(max_length=100 )
    cover_letter     = models.TextField()
    resume          = models.FileField(upload_to='Resumes/' )
    
    
    selected        = models.BooleanField(default=False)
    rejected        = models.BooleanField(default=False)
    status          = models.BooleanField(default=False)
 


