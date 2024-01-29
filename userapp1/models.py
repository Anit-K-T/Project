from django.db import models
import re

class add_data(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    mail=models.EmailField()
    address=models.CharField(max_length=100)
    age=models.IntegerField()
    password=models.CharField(max_length=20)

    
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class CoursePage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    about_course = models.CharField(max_length=600)

    def __str__(self):
        return self.course.course_name
    
class pdf(models.Model):
    course=models.ForeignKey(CoursePage, on_delete=models.CASCADE)
    pdf_name=models.CharField(max_length=80)
    pdf_content=models.CharField(max_length=150)
    document = models.FileField(upload_to='pdf/')
    
    def __str__(self):
        return self.pdf_name
    
class Video(models.Model):
    course=models.ForeignKey(CoursePage, on_delete=models.CASCADE)
    video_name=models.CharField(max_length=80)
    video_description=models.CharField(max_length=150)
    video_content=models.FileField(upload_to="video/%y")

    def __str__(self):
        return self.video_name

class VideoLink(models.Model):
    course=models.ForeignKey(CoursePage, on_delete=models.CASCADE)
    video_name=models.CharField(max_length=80)
    video_link=models.URLField()

    def __str__(self):
        return self.video_name

    def save(self, *args, **kwargs):
        
        pattern = re.compile(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
    
        # Find the match in the provided URL
        match = pattern.search(self.video_link)

        # Return the video ID if found, otherwise return None
        self.video_link= match.group(1) if match else None
        print(self.video_link)  
        super(VideoLink, self).save(*args, **kwargs)
    