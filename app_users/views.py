import threading

from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.views import View
from django.views.generic import FormView, TemplateView,View


from app_users.forms import RegisterForm, LoginForm,PasswordChangeForm
from app_users.utils import send_email_confirmation
from app_users.forms import UserUpdateForm, ProfileUpdateForm

UserModel = get_user_model()


class EmailVerificationView(TemplateView):
    template_name = "auth/email-verification-page.html"


class RegisterView(FormView):
    template_name = "auth/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:verification-page")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        email_thread = threading.Thread(target=send_email_confirmation, args=(user, self.request,))
        email_thread.start()
        print(email_thread)

        return super().form_valid(form)

    def form_invalid(self, form):
        for errors in form.errors.values():
            for error in errors:
                messages.error(self.request, f"Xatolik: {error}")
        return super().form_invalid(form)


class VerificationView(View):
    def get(self, request, *args, **kwargs):
        try:
            uid = kwargs.get('uid')
            token = kwargs.get('token')

            user = UserModel.objects.get(id=uid)
        except UserModel.DoesNotExist:
            return redirect('/')
        try:
            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return redirect('/')
            else:
                return redirect('/')
        except Exception as e:
            print(e)
            return redirect('/')


class LoginFormView(FormView):
    template_name = "auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("news:list")

    def form_valid(self, form):
        if form.is_valid():
            user = form.cleaned_data.get("user")
            login(request=self.request, user=user)
            return redirect('pages:home')
        else:
            self.form_invalid(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        for errors in form.errors.values():
            for error in errors:
                messages.error(self.request, f"Xatolik: {error}")
        return super().form_invalid(form)

class DashboardTemplateView(TemplateView):
    template_name = 'auth/account.html'

def user_logout(request):
    logout(request)
    return redirect('pages:home')

class ChangePasswordView(FormView):
    template_name = 'auth/change_password.html'
    success_url = reverse_lazy('users:change-password')

    def get_form_class(self):
        return PasswordChangeForm 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  
        return kwargs

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Parolingiz muvaffaqiyatli yangilandi!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Parolni yangilashda xatolik yuz berdi.')
        return super().form_invalid(form)
    


class ProfileEditView(LoginRequiredMixin, View):
    template_name = 'auth/profile_edit.html'

    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:account') 
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template_name, context)

    