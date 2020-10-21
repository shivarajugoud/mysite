from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from ads.models import Ad
from django.views import View
from ads.forms import CreateForm
from ads.owner import OwnerListView, OwnerDetailView,OwnerCreateView,OwnerUpdateView,OwnerDeleteView
class AdListView(OwnerListView):
    model = Ad
    template_name = "ads/list.html"
# Create your views here.
class AdDetailView(OwnerDetailView):
    model = Ad
    template_name ="ads/detail.html"
class AdCreateView(LoginRequiredMixin,  View):
    template_name = 'ads/form.html'
    success_url = reverse_lazy('ads:all')
    def get(self, request,pk = None):
        form = CreateForm()
        ctx{
    model = Ad
    fields = ['title','price','text']
class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title','price','text']
class AdDeleteView(OwnerDeleteView):
    model = Ad