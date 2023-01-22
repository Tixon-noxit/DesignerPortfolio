from django.views.generic import ListView, CreateView
from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail, BadHeaderError
from OFFMAXLINE.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import ContactForm
from .models import *

menu = [{'title': 'ОБО МНЕ', 'url_name': 'About'},
        {'title': 'ПРОЕКТЫ', 'url_name': 'Projects'},
        {'title': 'КОНТАКТЫ', 'url_name': 'Contacts'},
        ]

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

partners = Partners.objects.all()  # Сотрудничество

education = Education.objects.all()  # Образование

project = Project.objects.all()  # Проекты


# --------------------------------------------------------------
def index(request):
    data = {"menu": menu,
            "greetingText": "O F F M A X L I N E",
            "title": "OFFMAXLINE",
            "header_1": "Мои", "header_2": "Проекты",
            "name": name, "surname": surname,
            'id_selected': 0,
            'favicon': favicon,
            }
    return render(request, "main/index.html", context=data)


class MironovProject(ListView):
    paginate_by = 6  # РАзбивка по 6 проектов на страницу пагинации
    model = Project
    template_name = 'main/projects.html'
    # Передача статических данных
    extra_context = {"header_1": "Мои", "header_2": "Проекты", 'id_selected': 1, }

    def get_context_data(self, *, object_list=None, **kwargs):  # Передача динамических данных
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['name'] = name
        context['favicon'] = favicon
        context["master"] = master
        context["surname"] = surname
        context["quote"] = quote
        context["project"] = project
        context["quote_author"] = quote_author
        context['title'] = "Проекты"
        # можно задать выбранную страницу для это
        # context['параметр'] = 0 ()
        return context

    def get_queryset(self):  # Фильтруем выводимые значения
        return Project.objects.filter(is_published=True)


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
        context["Education"] = education
        context["Partners"] = partners
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
            last_name = form.cleaned_data['last_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {last_name} {first_name} {from_email}', message, 'tixon.noxit@yandex.ru', ['chabysow@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('Contacts')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "main/contacts.html", context=data)

