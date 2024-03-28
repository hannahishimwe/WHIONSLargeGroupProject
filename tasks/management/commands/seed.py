from django.core.management.base import BaseCommand, CommandError

from tasks.models import User,Template,JournalEntry

from random import randint, random
import pytz
from faker import Faker
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


user_fixtures = [
    {'username': '@johndoe', 'email': 'john.doe@example.org', 'first_name': 'John', 'last_name': 'Doe'},
    {'username': '@janedoe', 'email': 'jane.doe@example.org', 'first_name': 'Jane', 'last_name': 'Doe'},
    {'username': '@charlie', 'email': 'charlie.johnson@example.org', 'first_name': 'Charlie', 'last_name': 'Johnson'},
]




class Command(BaseCommand):
    """Build automation command to seed the database."""

    USER_COUNT = 3
    DEFAULT_PASSWORD = 'Password123'
    help = 'Seeds the database with sample data'

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        self.create_users()
        self.create_doe_journal_entries()
        self.users = User.objects.all()


    def create_users(self):
        self.generate_user_fixtures()
        self.generate_random_users()
    
  

    def generate_user_fixtures(self):
        for data in user_fixtures:
            self.try_create_user(data)

    def generate_random_users(self):
        user_count = User.objects.count()
        while  user_count < self.USER_COUNT:
            print(f"Seeding user {user_count}/{self.USER_COUNT}", end='\r')
            self.generate_user()
            user_count = User.objects.count()
        print("User seeding complete.      ")

    def generate_user(self):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = create_email(first_name, last_name)
        username = create_username(first_name, last_name)
        self.try_create_user({'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name})
       
    def try_create_user(self, data):
        try:
            self.create_user(data)
        except:
            pass

    def create_user(self, data):
        User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=Command.DEFAULT_PASSWORD,
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
    

    def create_doe_journal_entries(self):
            john_doe = User.objects.get(username='@johndoe')
            jane_doe = User.objects.get(username='@janedoe')

            titles = [
            "A Day to Remember",
            "Reflections on a Quiet Evening",
            "Journey of the Mind",
            "Self Reflection",
            "My Morning of Rest",
            "My Last Week",
            "My New Years Resolutiosn"
        ]
        
            for user in [john_doe, jane_doe]:
                for _ in range(3): 
                    title = self.faker.text(max_nb_chars=25)
                    text = self.faker.text(max_nb_chars=200) 
                    mood = 3

                    JournalEntry.objects.create(
                        user=user,
                        title=title,
                        text=text,
                        mood=mood,
                    )




def create_username(first_name, last_name):
    return '@' + first_name.lower() + last_name.lower()

def create_email(first_name, last_name):
    return first_name + '.' + last_name + '@example.org'
