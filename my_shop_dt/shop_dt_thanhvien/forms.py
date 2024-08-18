from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

us_help_text='''
  <ul>
    <li>Bắt buộc.</li>
    <li>Tối đa 150 kí tự.</li>
  </ul>
'''

class BieuMau_DangKi_ThanhVien(UserCreationForm):
  email = forms.CharField(max_length=254, 
                          required=True, 
                          widget=forms.EmailInput(),
                          label='Thư điện tử')
  
  def __init__(self, *args, **kwargs):
    super(BieuMau_DangKi_ThanhVien, self).__init__(*args, **kwargs)
    
    self.fields['username'].label = "Tài khoản"
    self.fields['username'].help_text = us_help_text
    
    self.fields['password1'].label = "Mật khẩu"
    self.fields['password2'].label = "Xác nhận mật khẩu"
    
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')