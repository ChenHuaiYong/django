from django.shortcuts import render
from .models import Banner,BlogCategory,Post,Comment
# ***********************************
from django.views.generic.base import View
from django.db.models import Q
# ***********************************

# Create your views here.


# **************************************************************
class SearchView(View):
    def post(self, request):
        kw = request.POST.get('keyword')
        post_list = Post.objects.filter(Q(title__icontains=kw)|Q(content__icontains=kw))

        ctx = {
                    'post_list': post_list
        }
        return render(request, 'list.html', ctx)

#     **********************************************************

def index(request):
    banner_list = Banner.objects.all()
    feilei = BlogCategory.objects.all()
    tuijian = Post.objects.filter(is_recomment=True)
    fabu = Post.objects.order_by("-pub_date")


    zuixin = Comment.objects.order_by("-pub_date")
    pinglun = []
    for foo in zuixin:
        if foo.post not in pinglun:
            pinglun.append(foo.post)

    ctx = {
        'banner_list':banner_list,
        'feilei':feilei,
        'tuijian':tuijian,
        'fabu':fabu,
        'pinglun':pinglun
    }
    return render(request, 'index.html', ctx)

