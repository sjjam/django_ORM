from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content
    }
    return render(request, 'articles/create.html', context)


# 1. /introduce/
# 2. h1 태그로 이루어진 제목
# 2-1. 각각의 p 태그에 이름과 나이 작성
# 3. back 링크로 index로 돌아갈 수 있는 링크 하나
# 4. index에서 introduce 이동할 수 있는 링크 하나
# 5. base.html 상속받아서 block body 안에 작성
def introduce(request):
    return render(request, 'articles/introduce.html')
