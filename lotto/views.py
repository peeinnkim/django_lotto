from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm


# lotto main page
def index(request):

    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {}에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음



# test page
def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello World!</h1>')



# create new lotto num page
def post(request):
    if request.method == "POST":
        # print(request.POST) # 유저가 제출한 모든 정보 ex -> request.POST['text']: 유저가 입력한 텍스트
        # print(request.method) #  post인지 get인지

        form = PostForm(request.POST) # filled form

        if form.is_valid(): # Validation Check
            # form.save() -> 바로 DB에 저장됨
            lotto = form.save(commit = False) # 임시 저장. DB 하나의 행이 리턴됨
            lotto.generate()
            return redirect('lotto_main') # views에 저장해놓은 name명

    else:
        form = PostForm() # empty form 생성
        return render(request, 'lotto/form.html', {'form':form})



# show detail lotto num by lottokey
def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey) # primary key. DB하나의 행이 리턴
    return render(request, 'lotto/detail.html', {'lotto':lotto})
