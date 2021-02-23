from django.shortcuts import render

from myblog.models import models as blog
from myrealisations.models import models as realisations
from myservices.models import models as services
from website.models import models as website


# Create your views here.


def home(request):
    
    data={}
    return render(request ,'home.html', data)