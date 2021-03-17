from django.contrib import admin

from website.api.forms import CustomAuthForm

admin.AdminSite.login_form = CustomAuthForm
