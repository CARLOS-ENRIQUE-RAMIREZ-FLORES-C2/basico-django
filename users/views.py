"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

# http://ccbv.co.uk/projects/Django/3.0/django.views.generic.edit/FormView/
class SignupView(FormView):
    """ Users sign up views. """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ save form data """
        form.save()
        return super().form_valid(form)

# http://ccbv.co.uk/projects/Django/3.0/django.views.generic.edit/UpdateView/
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Update profile view """

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self):
        """ Return users profile"""
        return self.request.user.profile

    def get_success_url(self):
        """ Return to users profile """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

#https://docs.djangoproject.com/en/2.0/topics/auth/default/#module-django.contrib.auth.views
class LoginView(auth_views.LoginView):
    """ Login view """
    template_name = "users/login.html"


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """ Logout view  class optimizated """
    template_name = "users/login.html"
