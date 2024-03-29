# Generated by Django 4.2.6 on 2024-01-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp1', '0007_alter_coursepage_about_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='pdfs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_name', models.CharField(max_length=80)),
                ('pdf_content', models.CharField(max_length=150)),
                ('document', models.FileField(upload_to='pdf/')),
            ],
        ),
    ]
