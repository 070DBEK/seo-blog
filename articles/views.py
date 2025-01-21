from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Article, Comment


def home(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def create_author(request):
    if request.method == 'POST':
        short_text = request.POST.get('short_text')
        long_text = request.POST.get('long_text')
        email = request.POST.get('email')
        if short_text and email:
            author = Author(
                short_text=short_text,
                long_text=long_text,
                email=email
            )
            author.save()
            return redirect('home')
    return render(request, 'articles/create-author.html')


def create_article(request):
    if request.method == 'POST':
        short_text = request.POST.get('short_text')
        long_text = request.POST.get('long_text')
        author_id = request.POST.get('author')
        image = request.FILES.get('image')
        if short_text and author_id:
            author = Author.objects.get(id=author_id)
            article = Article(
                short_text=short_text,
                long_text=long_text,
                author=author,
                image=image
            )
            article.save()
            return redirect('home')
    authors = Author.objects.all()
    return render(request, 'articles/create-article.html', {'authors': authors})


def create_comment(request):
    if request.method == 'POST':
        short_text = request.POST.get('short_text')
        long_text = request.POST.get('long_text')
        email = request.POST.get('email')
        article_id = request.POST.get('article')
        if short_text and email and long_text:
            article = Article.objects.get(id=article_id)
            comment = Comment(
                short_text=short_text,
                long_text=long_text,
                email=email,
                article=article
            )
            comment.save()
            return redirect('articles:comment-success', article_slug=article.slug)
    articles = Article.objects.all()
    return render(request, 'articles/blog-detail.html', {'articles': articles})


def comment_success(request, article_slug):
    return render(request, 'articles/success-commented.html')


def author_detail(request, year, month, day, slug):
    author = get_object_or_404(
        Author,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    return render(request, 'articles/blog-detail.html', {'author': author})


def article_detail(request, year, month, day, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    return render(request, 'articles/blog-detail.html', {'article': article})
