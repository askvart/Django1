from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:   #Если стра-ца не явл-тся целым чис-м. передает первую страницу
        posts = paginator.page(1)
    except EmptyPage: # Если стр за пределами допустимого диапазона - посл.стр
        posts = paginator.page(paginator.num_pages)
    return  render(request,
                   'blog/post/list.html',
                   {'page':page,
                    'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,'blog/post/detail.html',
                  {'post':post})
