from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def form(request):
    #return HttpResponse('<h1>Form without a form.</h1>')
    return render(request, 'Form/index.html')
