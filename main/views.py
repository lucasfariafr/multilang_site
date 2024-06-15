from django.shortcuts import render
from .models import Article

# Create your views here.
def displayArticle(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'blog.html', {'articles': articles})