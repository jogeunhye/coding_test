from django.shortcuts import render,redirect
from .models import Board, Comment, Like
from django.contrib.auth.models import User
from .forms import BoardForm
from django.contrib import messages
# Create your views here.


#등록
def new(request):
    if request.method == "POST" :
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid() :
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            messages.success(request, '등록이 완료되었습니다.')
            return redirect('board:new')
        else :
            print("error")
            print(form.errors)
            messages.error(request, '문제가 발생했습니다. 개발자에게 문의하세요')
    else :
        form = BoardForm()
    return render(request, 'new.html', {'form':form})