from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from libgravatar import Gravatar
from django.contrib import messages
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField

class User(AbstractUser):
    """Model used for user authentication, and team member related information."""

    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of @ followed by at least three alphanumericals'
        )]
    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        """Model options."""

        ordering = ['last_name', 'first_name']

    def full_name(self):
        """Return a string containing the user's full name."""

        return f'{self.first_name} {self.last_name}'

    def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""

        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url

    def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        
        return self.gravatar(size=60)
    
class UserPreferences(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)
    sunday = models.BooleanField(default=True)
    journal_time = models.TimeField()
    

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = RichTextUploadingField(config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default = False)
    permanently_deleted = models.BooleanField(default = False)
    favourited = models.BooleanField(default = False)
    MOOD_CHOICES = [
        (1, 'Very Sad 😔'),  
        (2, 'Sad 🙁'),  
        (3, 'Neutral 😐'),  
        (4, 'Happy 🙂'),  
        (5, 'Very Happy😄'),  
    ]
    mood = models.IntegerField(choices=MOOD_CHOICES, default=3)  

    def delete_entry(self):
        self.deleted = True
        self.save()

    def permanently_delete(self):
        self.deleted = True
        self.permanently_deleted = True
        self.title = ""
        self.text = ""
        self.mood = 3
        self.save()

    def recover_entry(self):
        self.deleted = False
        self.save()


class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()


class Template(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    questions = models.CharField(max_length =255,blank = True)
    user_entry = models.BooleanField(default = True)
    deleted = models.BooleanField(default = False)
     

    def get_questions(self):
        return self.questions

    def get_questions_array(self):
        return self.questions.split(',')

    def set_questions_array(self, values):
        self.questions = ','.join(values)

class FlowerGrowth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stage = models.IntegerField(default=0)
    last_entry_date = models.DateField(null=True, blank=True)

    def reset_to_stage_zero(self):
        self.stage = 0
        self.save()

    def increment_stage(self):
        self.stage += 1
        self.save()

    def update_last_entry_date(self, date):
        self.last_entry_date = date
        self.save()


