from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
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
        if short_text and long_text and image and author_id:
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


def article_detail(request, year, month, day, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    if request.method == 'POST':
        short_text = request.POST.get('short_text')
        long_text = request.POST.get('long_text')
        email = request.POST.get('email')
        if short_text and email and long_text:
            Comment.objects.create(
                article=article,
                short_text=short_text,
                email=email,
                long_text=long_text,
            )
            return redirect('articles:comment-success', slug=article.slug)
    comments = article.comment_set.all()
    related_articles = Article.objects.filter(
        Q(author=article.author) | Q(short_text__icontains=article.long_text.split()[0])
    ).exclude(id=article.id)[:3]
    return render(request, 'articles/blog-detail.html', {
        'article': article,
        'comments': comments,
        'related_articles': related_articles
    })


def comment_success(request, slug):
    related_article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/success-commented.html', {'related_article': related_article})
