from django.db import models

# Create your models here.
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Company(SingletonModel):
    happy_clients = models.IntegerField(null=True, blank=True)
    project_completed = models.IntegerField(null=True, blank=True)
    positive_feedback = models.IntegerField(null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    insta_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        

class Portfolio(models.Model):
    name = models.CharField(max_length=300)
    project_category = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
       return self.name

class Skill(models.Model):
    name = models.CharField(max_length=300)
    percentage = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100,null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='team/', null=True, blank=True)
    facebook_profile = models.URLField(blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class FeaturedClient(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/', null=True, blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Testimonals(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, null=True, blank=True)
    image= models.FileField(upload_to='Testimonals', default='user.jpg')
    designation = models.CharField(max_length=200, null=True, blank=True)
    company=models.CharField(max_length=200, null=True, blank=True)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonal'
        verbose_name_plural = 'Testimonals'
