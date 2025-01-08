from django.shortcuts import render,get_object_or_404,redirect
from .models import Author, Article


def home(request):
    return render(request, 'index.html')


def create_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        email = request.POST.get('email')
        if name and bio and email:
            Author.objects.create(
                name=name,
                bio=bio,
                email=email,
            )
            return redirect('authors:home')
    return render(request, 'authors/create-authors.html')



def author_detail(request, year, month, day, slug):
    author = get_object_or_404(
        Author,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    ctx ={'author': author}
    return render(request, 'authors/blog-detail.html', ctx)


def article_detail(request, year, month, day, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    ctx ={'article': article}
    return render(request, 'articles/blog-detail.html', ctx)