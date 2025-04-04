from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

import copy
from .models import Postcode
from .forms import SearchForm
from .dashboards_vars import *

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def search_results(request):

    query = request.GET.get('search_str')
    query_nospace = query.replace(" ", "")

    results = []
    if query:
        results = Postcode.objects.filter(
            Q(postcode__icontains=query) | Q(postcode__icontains=query_nospace)
        )

    return render(request, 'search_results.html', {'query': query, 'results': results})

def postcode_details(request, postcode_str):

    postcode = get_object_or_404(Postcode, postcode=postcode_str)
    postcode_district = postcode.postcode_district
    postcode_unit = postcode_str.removeprefix(postcode_district)
    postcode_with_space = "{} {}".format(postcode_district, postcode_unit)

    query_postcode_hmlc_transactions_result = query_postcode_hmlc_transactions(postcode_with_space)
    
    return render(request, 'postcode_details.html', {'postcode': postcode,
                                                     'query_postcode_hmlc_transactions_result': query_postcode_hmlc_transactions_result})

@login_required(login_url='/login/')
def user_account(request):

    return render(request, 'user_account.html')