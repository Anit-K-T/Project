# Generated by Django 4.2.6 on 2024-01-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp1', '0002_rename_mail_add_data_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='add_data',
        ),
    ]
