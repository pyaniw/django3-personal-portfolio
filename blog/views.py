from django.shortcuts import render,get_object_or_404
from .models import all_blogs1

def all_blog (request):
    blog= all_blogs1.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs':blog})
def detail(request, blog_id):
    blog = get_object_or_404(all_blogs1, pk=blog_id)
    return render(request, 'blog/detail.html', {'id':blog})
def somehtml (request):
    return render(request, 'blog/somehtml.html')