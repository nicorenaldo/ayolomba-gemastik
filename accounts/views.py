from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from competitions.views import browse
from competitions.models import Lomba , Kategori
from django.db.models import Count
from django.core.mail import send_mail as sm
from .models import Profile
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.forms import PasswordChangeForm


def kirimemail(request):
    res = sm(
        subject = 'Dari hati ke hati',
        message = 'Aku cinta kamu, jangan kerja terus terusan, aku sayang kamu hehe',
        from_email = 'nicorenaldo14@gmail.com',
        recipient_list = ['doravalerie@gmail.com'],
        fail_silently=False,
    )    

    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            login(request, new_user)

            return redirect('profile:personalize')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            # request.user.profile.subscribe.add(p_form.cleaned_data['subscribe2'])
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('dashboard')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    listlomba = Lomba.objects.filter(owner=request.user)
    listkategori = Kategori.objects.annotate(totalkategori = Count('lomba'))
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'list_lomba' : listlomba,
        'list_kategori' : listkategori,
    }
    template = 'accounts/profile.html'
    return render(request, template, context)



@login_required
def settings(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        password_form = PasswordChangeForm(request.user, request.POST)
        if u_form.is_valid() and p_form.is_valid():
            # request.user.profile.subscribe.add(p_form.cleaned_data['subscribe2'])
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('dashboard')

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        password_form = PasswordChangeForm(request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'pass_form' : password_form,
    }
    template = 'accounts/settings.html'
    return render(request, template, context)

@login_required
def personalize(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        password_form = PasswordChangeForm(request.user, request.POST)
        if p_form.is_valid():

            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('dashboard')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }
    template = 'accounts/personalize.html'
    return render(request, template, context)
