from django.shortcuts import redirect, render
from .models import Course, CoursePage, pdf, Video, VideoLink, add_data

def welcome(request):
    if request.method == 'POST':
        option = request.POST.get('option')
        if option == 'login':
            return redirect('login')  # Assuming you have a 'login' URL pattern
        elif option == 'signup':
            return redirect('signup')  # Assuming you have a 'form' URL pattern

    return render(request, 'welcome.html')


def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        age=request.POST.get('age')
        password=request.POST.get('password')
        add_data(name=name,phone=phone,mail=email,address=address,age=age,password=password).save()
        return redirect('index')
    
    else:
        return render(request,'signup.html')




def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        print(name)
        password=request.POST.get('password')
        cr=add_data.objects.filter(name=name,password=password)
        if cr:
            userd=add_data.objects.get(name=name,password=password)
            name=userd.name
            password=userd.password
            request.session['name']=name
            return redirect('index')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def index(request):
    courses=Course.objects.all()
    print(courses)
    context = {
        'courses': courses,
    }
    return render(request,'index.html', context)

def course(request, course):
    course = Course.objects.filter(course_name=course)
    coursePage = CoursePage.objects.filter(course=course[0])[0]
    pdfs=pdf.objects.filter(course=coursePage)
    videos=Video.objects.filter(course=coursePage)
    videoLinks=VideoLink.objects.filter(course=coursePage)
    context = {
        'coursePage': coursePage,
        'pdfs': pdfs,
        'videos': videos,
        'videoLinks':videoLinks
    }
    return render(request,'about.html', context)

