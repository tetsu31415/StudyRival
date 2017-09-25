from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
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

