from django.urls import path
from django.contrib.auth import views as auth_views

from .views import dang_ki

urlpatterns = [
    path("quantri/dang_xuat/", auth_views.LogoutView.as_view(), name='dang_xuat'),
    path("quantri/dang_nhap/", auth_views.LoginView.as_view(template_name='dang_nhap.html'), name='dang_nhap'),
    
    path("quantri/dang_ki/", dang_ki, name='dang_ki'),
    
     #-- pass change --
    path("tllmk/",
         auth_views.PasswordResetView.as_view(
            template_name='thietlap_lai_matkhau.html',
            email_template_name='email.html',
            subject_template_name='tieu_de_email.txt'),
         name='tllmk'),    
    path("dge/",
        auth_views.PasswordResetDoneView.as_view(
            template_name='da_gui_duong_dan.html'),
        name='password_reset_done'),
    
    path("dmk/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
            template_name='doi_matkhau.html'),
         name='dmk'),
    path('doi-mat-khau/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path("htdmk/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name='hoanthanh_doi_matkhau.html'),
        name='password_reset_complete'),
]