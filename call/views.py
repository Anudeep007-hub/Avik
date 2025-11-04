from django.shortcuts import render

def index(request):
    return render(request, 'call/index.html')

def chat(request):
    return render(request, 'call/chat.html')
