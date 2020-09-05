from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Lomba , Kategori
from django.db.models import Count, Q
from .forms_submit import SubmitForm,BookmarkForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import Filter
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
# Create your views here.

def custom_404(request, exception=None):
    return HttpResponse('Error handler content', status=404)

def about (request):    
    template = 'competitions/about.html'
    return render(request, template)

def browse (request):
    listlomba = Lomba.objects.filter(deadline__gte =timezone.now())
    data = request.GET.copy()
        
    listlomba_filter = Filter(data, queryset=listlomba)
    paginator = Paginator(listlomba_filter.qs, 8)
    now = timezone.now()
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    template = 'competitions/browse_competitions.html'
    
    context = {'now':now, 'response':response, 'list_lomba':listlomba, 'filter': listlomba_filter}
    return render(request, template , context)

def home (request):
    listlomba = Lomba.objects.filter(deadline__gte =timezone.now()).order_by('-created')[:5]
    totallomba = Lomba.objects.all()
    listkategori = Kategori.objects.annotate(totalkategori = Count('lomba'))
    context = {'total':totallomba, 'list_lomba' : listlomba , 'list_kategori' : listkategori}

    template = 'competitions/index.html'
    return render(request, template , context)

def detaillomba (request, slug, pk):
    detaillomba = Lomba.objects.get(slug=slug, pk=pk)

    recent = Lomba.objects.filter(deadline__gte =timezone.now()).order_by('-created')[:5]
    related = detaillomba.tags.similar_objects()[:5]

    try:
        previous_page = detaillomba.get_previous_by_created()
    except Lomba.DoesNotExist:
        previous_page = detaillomba
        next_page = detaillomba.get_next_by_created()

    try:
        next_page = detaillomba.get_next_by_created()
    except Lomba.DoesNotExist:
        previous_page = detaillomba.get_previous_by_created()
        next_page = detaillomba
    

    listkategori = Kategori.objects.annotate(totalkategori = Count('lomba'))
    template = 'competitions/detail.html' 
    context = {'detail_lomba' : detaillomba, 'next':next_page, 'prev':previous_page, 'recent':recent, 'list_kategori' : listkategori, 'related':related}

    return render(request, template, context)

def bookmark(request, slug, pk):
    detaillomba = Lomba.objects.get(slug=slug, pk=pk)
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid(): 
            if form.cleaned_data['lomba'] in request.user.profile.favorite.all():
                request.user.profile.favorite.remove(form.cleaned_data['lomba'])
            else:
                request.user.profile.favorite.add(form.cleaned_data['lomba'])
            return HttpResponseRedirect( reverse('competitions:detail_lomba', kwargs={'slug':slug, 'pk':pk} ) )
    else:
        form = BookmarkForm()



class LombaCreate(LoginRequiredMixin, CreateView):
    model = Lomba
    form_class = SubmitForm
    template_name = 'competitions/submit.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.owner_email = self.request.user.email
        return super().form_valid(form)
    
    def username(request):
        username = None
        if request.user.is_authenticated():
            username = request.user.username
        context = {'username_' : username}
        template = 'competitions/submit.html'

        return render(request, template, context)
        

class LombaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lomba
    form_class = SubmitForm

    template_name = 'competitions/post_update.html'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.owner_email = self.request.user.email
        return super().form_valid(form)
    
    def test_func(self):
        lomba = self.get_object()
        if self.request.user == lomba.owner:
            return True
        return False

class LombaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lomba
    success_url = '/'

    def test_func(self):
        lomba = self.get_object()
        if self.request.user == lomba.owner:
            return True
        return False
