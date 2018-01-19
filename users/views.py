from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import time
import short_url
from django.core.mail import send_mail

from .models import InviteUrl
from .forms import SignUpForm


class UserInviteView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_invitepage.html'

    def get_context_data(self, **kwargs):
        context = super(UserInviteView, self).get_context_data(**kwargs)
        context['sent_invite'] = InviteUrl.objects.filter(user=self.request.user)
        return context

    def post(self, value):
        domain = self.request.build_absolute_uri('invite/')
        inviter = str(time.time()).replace('.', '') + short_url.encode_url(self.request.user.id)
        invite_url = InviteUrl.objects.create(user=self.request.user, email=self.request.POST['Email'], url=inviter)
        invite_url.save()
        send_mail('Invite message', 'Hello! Your invite URL: ' + domain + inviter, 'from@example.com',
                  [self.request.POST['Email']], fail_silently=False)
        return HttpResponseRedirect('/')


def signup(request, invite_data=''):
    if not request.user.is_authenticated and len(InviteUrl.objects.filter(url=invite_data)) == 1:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user_login = authenticate(username=username, password=raw_password)
                login(request, user_login)
                InviteUrl.objects.filter(url=invite_data).update(user_invite=user_login)
                InviteUrl.objects.filter(url=invite_data).update(status=True)

                return redirect('/')
        else:
            form = SignUpForm()
        return render(request, 'registration/registration_form.html', {'form': form})
    return HttpResponseRedirect('/')
