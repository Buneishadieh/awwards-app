# Generated by Django 3.1.7 on 2021-04-04 13:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Revieww',
            new_name='Review',
        ),
    ]