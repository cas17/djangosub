from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def party(request):
    return render(request, 'party.html')

def leader(request):
    return render(request, 'leader.html')
