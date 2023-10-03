from __future__ import annotations

from django.shortcuts import render
from django.views import View


# Create your views here.
class HomeView(View):
    template_name = 'core/coverpage.html'

    def get(self, request, *args, **kwargs):
        background_default = '/static/img/cover_page.png'
        context = {
            'metric': '',
            'start_date': '',
            'end_date': '',
            'logo': '',
            'background_default': background_default,
        }
        return render(request, self.template_name, context=context)


def template1(request):
    background_default = '/static/img/template_background.png'
    context = {
        'background_default': background_default,
        'chart_list': [],
        'logo': '',
        'start_date': '',
        'end_date': '',
    }
    return render(request, 'core/template_1.html',  context=context)
