from main.models import SiteSettings, Partners, Education, Project
from mironov_site import settings


menu = [#{'title': 'ОБО МНЕ', 'url_name': 'About'},
        #{'title': 'ПРОЕКТЫ', 'url_name': 'Projects'},
        #{'title': 'CREATION', 'url_name': 'Creation'},
        #{'title': 'КОНТАКТЫ', 'url_name': 'Contacts'},
]



if settings.DEBUG:
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





class DataMixin:        
    def get_user_context(self, **kwargs):
        context = kwargs
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
        return context