from django import forms
from .models import GuessNumbers

# django에서 제공하는 ModelForm을 활용
class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # 사용자로부터 form을 통해 입력받을 데이터
        
