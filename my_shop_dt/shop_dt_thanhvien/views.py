from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth import login as qldn
from .forms import BieuMau_DangKi_ThanhVien
# Create your views here.
def dang_ki(req):
    if req.method == 'POST':
        ucf = BieuMau_DangKi_ThanhVien(req.POST)
        if ucf.is_valid():
            user = ucf.save()
            qldn(req, user)
            
            return redirect('home')
    else:
        ucf = BieuMau_DangKi_ThanhVien()
        
    return render(req, 'dang_ki.html', {'form':ucf})

