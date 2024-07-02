from django.shortcuts import render

from portfolio.models import About, Global, Skills

# Create your views here.
def index(request):
    global_data = Global.objects.all()[0]
    about = About.objects.all()[0]
    technical_skills = Skills.objects.filter(type = "Technical")
    proffesional_skills = Skills.objects.filter(type = "Proffesional")
    context={
        "global":global_data,
        "about": about,
        "technical_skills":technical_skills,
        "proffesional_skills":proffesional_skills,

    }
    return render (request,'portfolio/index.html',context)