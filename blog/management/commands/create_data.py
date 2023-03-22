from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

from blog.models import Post, Comment


class Command(BaseCommand):
    help = 'Create 20-posts. 10-users, 30-comments'

    def handle(self, *args, **options):
        Post.objects.all().delete()
        Comment.objects.all().delete()
        User.objects.exclude(username='admin').delete()

        fake = Faker()

        users = User.objects.bulk_create([User(
            username=fake.name(),
            password=make_password(fake.password())
        ) for _ in range(10)])

        for user in users:
            posts = Post.objects.bulk_create([Post(
                title=fake.text(max_nb_chars=20),
                text=fake.paragraph(nb_sentences=3),
                owner=user
            ) for _ in range(2)])

            for post in posts:
                Comment.objects.bulk_create([Comment(
                    owner=user,
                    post=post,
                    text=fake.paragraph(nb_sentences=1),
                ) for _ in range(3)])

        self.stdout.write(self.style.SUCCESS('Create 20-posts. 10-users, 30-comments'))
