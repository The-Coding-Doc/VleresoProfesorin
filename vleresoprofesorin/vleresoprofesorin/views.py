from django.views.generic import TemplateView

class LoginPage(TemplateView):
    template_name = 'login.html'

class HomePage(TemplateView):
    template_name = 'index.html'
