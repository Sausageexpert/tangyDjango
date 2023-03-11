from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import foodItems
from django.template import loader
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list=foodItems.objects.all()
    #template=loader.get_template('tangyDjango/index.html')
    context={
    'item_list':item_list
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'tangyDjango/index.html', context)
    
def Check(request):
    return HttpResponse('Hello Check')

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request, item_id):
    item = foodItems.objects.get(pk = item_id)
    context = {
        'item':item,
    }
    return render(request, 'tangyDjango/detail.html', context)          

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tangyDjango:index')
    return render(request, 'tangyDjango/item_form.html', {'form':form})                                  