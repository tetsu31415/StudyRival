from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic
 
from .forms import UpdateForm
 
class TopPageView(generic.TemplateView):
    template_name = "easy_regist/index.html"
 
class MyPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "easy_regist/info.html"
 
class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UpdateForm
    success_url = reverse_lazy('easy_regist:mypage')
    template_name = "easy_regist/user_update.html"
 
def logout(request):
    context = {
        'template_name': 'easy_regist/index.html',
    }
    return auth_views.logout(request, **context)

def login(request):
    return render(request, 'easy_regist/login_t.html', {})

