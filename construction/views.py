from django.http import Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from construction.models import ContactInfo, HeaderIntroduction, AboutUs, Chart, Services, Projects, Comments, SocialAccount
from construction.forms import contactInfoForms

def index(request):
    if request.method == "POST":
        form = contactInfoForms(request.POST)

        if form.is_valid():
            form.save()
    else:
            form = contactInfoForms() 

    contactinfo = ContactInfo.objects.first()
    headerintro = HeaderIntroduction.objects.all()
    aboutus = AboutUs.objects.first() 
    chart = Chart.objects.first()
    service = Services.objects.all()
    project = Projects.objects.all()
    comment = Comments.objects.all()
    social_account = SocialAccount.objects.first()

    return render(request, 'construction/index.html', {
        'continfo' : contactinfo,
        'header' : headerintro,
        'aboutus' : aboutus,
        'chart' : chart,
        'service' : service,
        'project' : project,
        'comment' : comment,
        'social_account' : social_account,
        "form": form
    })

def projects(request):
    projects = Projects.objects.all()

    paginator = Paginator(projects, 6)
    page = request.GET.get('page', 1)
    pagi_projects = paginator.page(page)

    return render(request, 'construction/projects_page.html', 
                   {
                        'project' : pagi_projects,
                   })

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        projects = Projects.objects.filter(isActive = True, heading__contains = q)
    else:
        return redirect("/projects")

    return render (request, "construction/search.html",
                   {
                        'project' : projects
                   })

def projectdetails(request, project_slug):
    contactinfo = ContactInfo.objects.first()
    try:
          project_now = Projects.objects.get(slug = project_slug)
    except:
         raise Http404()
    
    return render(request, 'construction/project_detailpage.html',{
         "project" : project_now,
         "continfo" : contactinfo
    })

