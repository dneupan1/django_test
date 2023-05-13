from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def register_player(request):
    return render(request, template_name="register_player.html")
