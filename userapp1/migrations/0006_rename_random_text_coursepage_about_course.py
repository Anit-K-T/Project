# Generated by Django 4.2.6 on 2024-01-28 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp1', '0005_coursepage_random_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursepage',
            old_name='random_text',
            new_name='about_course',
        ),
    ]