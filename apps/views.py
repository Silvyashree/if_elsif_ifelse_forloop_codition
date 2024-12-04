from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'name':'niranjaaaaa' ,'age':24}
    
    return render (request,'condition.html',context=d) 