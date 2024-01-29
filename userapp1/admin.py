from django.contrib import admin
from .models import Course, CoursePage, pdf, Video, VideoLink, add_data

admin.site.register(add_data)
admin.site.register(Course)
admin.site.register(CoursePage)
admin.site.register(pdf)
admin.site.register(Video)
admin.site.register(VideoLink)