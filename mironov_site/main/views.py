from django.views.generic import ListView, CreateView
from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail, BadHeaderError
from mironov_site.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL, DEBUG
from .forms import ContactForm
from .models import *
# from mironov_site.utils import DataMixin
from django.contrib import messages
from django.template import RequestContext



menu = [{'title': 'ОБО МНЕ', 'url_name': 'About'},
        {'title': 'ПРОЕКТЫ', 'url_name': 'Projects'},
        {'title': 'CREATION', 'url_name': 'Creation'},
        {'title': 'КОНТАКТЫ', 'url_name': 'Contacts'},
]


if DEBUG:
    master = 'Миронов'
    user = 'SiteSettings.objects.get(surname="Mironov")'
    quote = 'user.site_quote'
    quote_author = 'user.owner_site_quote'
    name = 'user.name'
    surname = 'user.surname'
    photo_about_me = 'user.photo'
    skills = 'user.skills'
    biography = 'user.biography'
    backgroundContact = 'user.contactPhoto'
    favicon = 'user.favicon'
    

    partners = 'Partners.objects.filter(is_published=True)'  # Сотрудничество

    education = 'Education.objects.filter(is_published=True)'  # Образование

    project = 'Project.objects.all()'  # Проекты
else:
    master = 'Миронов'
    user = SiteSettings.objects.get(surname="Mironov")
    quote = user.site_quote
    quote_author = user.owner_site_quote
    name = user.name
    surname = user.surname
    photo_about_me = user.photo
    skills = user.skills
    biography = user.biography
    backgroundContact = user.contactPhoto
    favicon = user.favicon
    background = user.background

    partners = Partners.objects.filter(is_published=True)  # Сотрудничество

    education = Education.objects.filter(is_published=True)  # Образование

    project = Project.objects.all()  # Проекты


# --------------------------------------------------------------
def index(request):
    data = {
            "greetingText": "O F F M A X L I N E",
            "title": "Миронов Максим",
            'id_selected': 0,
            'favicon': 'favicon',
            }
    return render(request, "main/index.html", context=data)


class MironovProject(ListView):
    # paginate_by = 6  # РАзбивка по 6 проектов на страницу пагинации
    model = Project
    template_name = 'main/projects.html'
    # Передача статических данных
    extra_context = {'id_selected': 1, }

    def get_context_data(self, *, object_list=None, **kwargs):  # Передача динамических данных
        context = super().get_context_data(**kwargs)
        #mixin = self.get_user_context(title='Проекты', header_1='Мои', header_2='Проекты',)
        context['menu'] = menu
        context['favicon'] = favicon
        context['name'] = name
        context["master"] = master
        context["surname"] = surname
        context["quote"] = quote
        context["quote_author"] = quote_author
        context["photo"] = photo_about_me
        context["biography"] = biography
        context["skills"] = skills
        context["education"] = education
        context["Partners"] = partners
        context['background'] = background
        context['title'] = 'Проекты'
        context['header_1'] ='Мои'
        context['header_2']='Проекты'

        return context #dict(list(context.items()) + list(mixin.items()))

    def get_queryset(self):  # Фильтруем выводимые значения
        return Project.objects.filter(is_published=True)



class MironovCreation(ListView):
    # paginate_by = 6  # РАзбивка по 6 проектов на страницу пагинации
    model = Creation
    template_name = 'main/creation.html'
    # Передача статических данных
    extra_context = {'id_selected': 1, }

    def get_context_data(self, *, object_list=None, **kwargs):  # Передача динамических данных
        context = super().get_context_data(**kwargs)
        #mixin = self.get_user_context(title='Creation', header_1='', header_2='Creation',)
        context['menu'] = menu
        context['favicon'] = favicon
        context['name'] = name
        context["master"] = master
        context["surname"] = surname
        context["quote"] = quote
        context["quote_author"] = quote_author
        context["photo"] = photo_about_me
        context["biography"] = biography
        context["skills"] = skills
        context["education"] = education
        context["Partners"] = partners
        context['background'] = background
        context['title'] = 'Creation'
        context['header_1'] ='Мои'
        context['header_2']='Creation'
        
        return context #dict(list(context.items()) + list(mixin.items()))

    def get_queryset(self):  # Фильтруем выводимые значения
        return Creation.objects.filter(is_published=True)


class MironovAbout(ListView):
    model = SiteSettings
    template_name = 'main/about_me.html'
    # Передача статических данных
    extra_context = {"header_1": "Немного", "header_2": "Обо мне", 'id_selected': 2, }
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):  # Передача динамических данных
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['favicon'] = favicon
        context['name'] = name
        context["master"] = master
        context["surname"] = surname
        context["quote"] = quote
        context["quote_author"] = quote_author
        context['title'] = "Обо мне"
        context["photo"] = photo_about_me
        context["biography"] = biography
        context["skills"] = skills
        context["education"] = education
        context["Partners"] = partners
        context['background'] = background
        # можно задать выбранную страницу для это
        # context['параметр'] = 0 ()
        return context


# --------------------------------------------------------------
def contacts(request):
    subjectForm = ContactForm()
    data = {"master": master,
            "title": "Контакты",
            "backgroundContact": backgroundContact,
            "name": name, "surname": surname,
            "menu": menu,
            "quote": quote,
            "quote_author": quote_author,
            "header_1": "Мои", "header_2": "Контакты",
            "form": subjectForm,
            'id_selected': 3,
            'favicon': favicon,
            }

    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm(request.POST)
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            telephone = form.cleaned_data['telephone']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {telephone} {first_name} {from_email}', message, RECIPIENTS_EMAIL,
                          [DEFAULT_FROM_EMAIL], fail_silently=False)
                messages.info(request, 'Соообщение успешно отправлено!   Спасибо за обращение!')          
            except BadHeaderError:
                messages.error(request, 'Ошибка при отправке сообщения!')
            return redirect('Contacts')
    else:
        messages.error(request, 'Неверный запрос!')
    return render(request, 'main/contacts.html', context=data)
    
    
    
# обработка страницы 404
def handler404(request, exception):
    return render(request, 'main/404.html', status=404)    


# обработка страницы 500
def handler500(request, *arg, **argv):
    return render(request, 'main/500.html', status=500)  