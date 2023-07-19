from django.shortcuts import render
from mironov_site.utils import DataMixin
from django.views.generic import ListView
from main.models import *



class MironovAbout(DataMixin, ListView):
    model = SiteSettings
    template_name = 'about/about_me.html'
    # Передача статических данных
    extra_context = {'id_selected': 2,}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):  # Передача динамических данных
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Обо мне', header_1='Немного', header_2='Обо мне',)
        
        return dict(list(context.items()) + list(mixin.items()))
