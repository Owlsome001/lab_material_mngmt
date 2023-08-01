from django.shortcuts import render

# Create your views here.

def home(request):
    data = {
        'name': "Arthur",
        'gender' : "F"
        
    }
    if data['gender'] == "M":
        return render(request, "home.html", context={'title': "Monsieur"})
    else:
        return render(request, "home.html", context={'title': "Madame"})