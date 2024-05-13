from django.shortcuts import render, redirect
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Repository

def home(request):
    return render(request, 'github_temp/home.html')

def search(request):
    query = request.GET.get('query')
    if query:
        repositories = search_repositories(query)
        if repositories:
            paginator = Paginator(repositories, 10)  # Show 10 objs per page
            page = request.GET.get('page')
            try:
                repositories = paginator.page(page)
            except PageNotAnInteger:
                repositories = paginator.page(1)
            except EmptyPage:
                repositories = paginator.page(paginator.num_pages)
            return render(request, 'github_temp/search.html', {'repositories': repositories, 'query': query})
        else:
            return render(request, 'github_temp/home.html', {'error': 'No repositories found for the given query.'})
    else:
        return render(request, 'github_temp/home.html', {'error': 'Please enter a search query.'})
    
def search_repositories(query):
    url = 'https://api.github.com/search/repositories'
    params = {'q': query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['items']
    else:
        return None

# View for save repository data 
def save_repository(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        owner = request.POST.get('owner')
        description = request.POST.get('description')
        stars = request.POST.get('stars')
        forks = request.POST.get('forks')
        
        try:
            # Create a new Repository object and save it
            repository = Repository.objects.create(
                name=name,
                owner=owner,
                description=description,
                stars=int(stars),
                forks=int(forks)
            )
            repository.save()
            messages.success(request, 'Repository saved successfully!')
        except Exception as e:
            messages.error(request, f'Failed to save repository: {e}')