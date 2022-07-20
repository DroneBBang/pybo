from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm




# Create your views here.


def signup(request):
    # 회원가입

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# 페이지 못찾을 때의 표시
def page_not_found(request, exception):
    """
    404 page not found
    """
    return render(request, 'common/404.html', {})
