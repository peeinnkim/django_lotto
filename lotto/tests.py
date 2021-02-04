from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        print('생성된 g->>', g)
        g.generate() # GuessNumbers 클래스의 generate 함수를 실행
        print(g.update_date)
        print(g.lottos)

        # 실제 Test Case(assertTrue() -> 참인지 거짓인지 확인하여 OK or FAILED 반환)
        # default 6개 숫자 x 5set = 30개의 숫자가 생성됨을 확인
        self.assertTrue(len(g.lottos) > 20)
