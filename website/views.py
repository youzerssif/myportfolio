from django.shortcuts import render

from myblog.models import Article
from myrealisations.models import Portfolio
from myservices.models import Metier, Skill, Service
from website.models import Apropos, Statistique, Newsletter, Contact

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


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



@csrf_exempt
def sendNewsletter(request):
    
    succes = False
    message = ""

    if request.method == 'POST':
        nom = request.POST.get('nom')
        print('$$$$$$$$$$$$$$$$', nom)
        email = request.POST.get('email')
        print('$$$$$$$$$$$$$$$$', email)
        
        try:
            if nom is not None and not nom.isspace() and email is not None and not email.isspace():
                newsletter = Newsletter(nom=nom, email=email)
                print('OK OK OK OK ', newsletter)
                # newsletter.save()
                
                succes = True
                message = "Merci de vous avoir abonné à ma newsletter"
            else:
                succes = False
                message = "veillez bien renseigner les champs svp!"


        except Exception as e:
            print(e)
            message = "Un problème survenu lors de l'enregistrement"

    datas = {
        'succes':succes,
        'message': message,
    }

    return JsonResponse(datas, safe=False)



@csrf_exempt
def sendContact(request):
    
    succes = False
    message = ""

    if request.method == 'POST':
        nom = request.POST.get('nom')
        print('$$$$$$$$$$$$$$$$', nom)
        email = request.POST.get('email')
        print('$$$$$$$$$$$$$$$$', email)
        numero = request.POST.get('numero')
        print('$$$$$$$$$$$$$$$$', numero)
        sujet = request.POST.get('sujet')
        print('$$$$$$$$$$$$$$$$', sujet)
        message = request.POST.get('message')
        print('$$$$$$$$$$$$$$$$', message)
        
        try:
            if nom is not None and not nom.isspace() and email is not None and not email.isspace() and numero is not None and not numero.isspace() and sujet is not None and not sujet.isspace() and message is not None and not message.isspace():
                contact = Contact(nom=nom, email=email, numero=numero, sujet=sujet, message=message)
                print('OK OK OK OK ', contact)
                # contact.save()
                
                succes = True
                message = "Votre messages a été envoyer avec succès"
            else:
                succes = False
                message = "veillez bien renseigner les champs svp!"


        except Exception as e:
            print(e)
            message = "Un problème survenu lors de l'enregistrement"

    datas = {
        'succes':succes,
        'message': message,
    }

    return JsonResponse(datas, safe=False)