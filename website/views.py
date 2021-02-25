from django.shortcuts import render

from myblog.models import Article
from myrealisations.models import Portfolio
from myservices.models import Metier, Skill, Service
from website.models import Apropos, Statistique


# Create your views here.


def home(request):
    
    try:
        
        about = Apropos.objects.get(status=True)
        metiers = Metier.objects.filter(status=True)
        skills = Skill.objects.filter(status=True)
        stats = Statistique.objects.get(status=True)
        articles = Article.objects.filter(status=True)
        services = Service.objects.filter(status=True)
        portfolios = Portfolio.objects.filter(status=True)
        
    except Exception as e:
        print("except", str(e))
    

    data={
        'about':about,
        'metiers':metiers,
        'skills':skills,
        'stats':stats,
        'articles':articles,
        'services':services,
        'portfolios':portfolios,
    }
    return render(request ,'home.html', data)