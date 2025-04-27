from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def comments(request):
    return render(request, 'comments.html')


def new_comment(request):
    from ws.forms.captcha_form import CaptchaForm
    form = CaptchaForm()
    parent_comment_id = request.GET.get('parent_comment_id')
    return render(request, 'new_comment.html', {'parent_comment_id': parent_comment_id, 'form': form})
