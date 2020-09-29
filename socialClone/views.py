from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'

class TestPageView(TemplateView):
    template_name = 'test.html'

class ThanksPageView(TemplateView):
    template_name = 'thanks.html'    
