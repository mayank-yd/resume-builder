from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        phone = request.POST.get("phone","")
        email = request.POST.get("email", "")
        school = request.POST.get("school", "")
        degree = request.POST.get("degree", "")
        university = request.POST.get("university", "")
        skills = request.POST.get("skills", "")
        summary = request.POST.get("summary", "")
        workexperince = request.POST.get("workexperience", "")

        profile = Profile(name=name, phone=phone, email=email, school=school, degree=degree, university=university, skills=skills, summary=summary, workexperince=workexperince)
        profile.save()

    return render(request,"accept.html")

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template = loader.get_template("resume.html")
    html = template.render({'user_profile': user_profile})
    options= {
        'page-size': 'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options)

    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Dispostion'] = 'attachements'
    return response

def list(request):
    profile=Profile.objects.all()
    return render(request, "list.html", {'profile': profile})