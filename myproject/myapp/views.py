from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
import models
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import never_cache

#@cache_page(4)

@never_cache
def home(request):
    a = models.Post.objects.all().order_by('?')[:1].get()
    return render_to_response('index.html', {'a': a})

def blitz(request):
    return HttpResponse("42")


