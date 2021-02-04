from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model): # Model: class생성에 모든걸 담고있음
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField() # 갱신 날짜


    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1,46)) # 1~45의 숫자 리스트

        # 6개 번호 set 갯수만큼 1~45를 섞은 다음 앞의 6개를 골라내 정렬
        for _ in range(0, self.num_lotto):
            random.shuffle(origin) # 원본을 섞고 덮어씌움
            guess = origin[:6] # 섞인 리스트에서 앞의 6개만 가져옴
            guess.sort() # 오름차순 정렬
            self.lottos += str(guess) + '\n' # 로또 번호 str에 6개 번호 set 추가

        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장
        # save() -> Model 클래스에 들어있는 함수로 하나하나의 행을 저장해줌 commit 같은 늑김


    def __str__(self): # Admin page에 display되는 텍스트에 대한 변경
        return "pk {}: {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성
