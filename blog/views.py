from django.shortcuts import render, get_object_or_404
from .models import News


# Create your views here.
def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})


def news_detail(request, pk):
    news = get_object_or_404(News, id=pk)
    return render(request, 'news/news_detail.html', {'news': news})