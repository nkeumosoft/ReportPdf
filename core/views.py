from __future__ import annotations

import datetime

from django.shortcuts import render
from django.views import View

from core.use_case import get_abosulte_path_of_file
from core.use_case import render_string_pdf


# Create your views here.
class HomeView(View):
    template_name = 'core/coverpage.html'

    def get(self, request, *args, **kwargs):
        background_default = '/static/img/cover_page.png'
        context = {
            'metric': '/static/img/report-cover-page.png',
            'start_date': datetime.datetime.now(),
            'end_date': datetime.datetime.now(),
            'logo': '/static/img/somate-verticle.svg',
            'background_default': background_default,
        }

        background_default = get_abosulte_path_of_file(
            'static/img/cover_page.png',
        )
        context_pdf = {
            'metric': get_abosulte_path_of_file('static/img/report-cover-page.png'),
            'start_date': datetime.datetime.now(),
            'end_date': datetime.datetime.now(),
            'logo': get_abosulte_path_of_file('static/img/somate-verticle.svg'),
            'background_default': background_default,
        }
        render_string_pdf(
            request, self.template_name,
            css='static/css/coverstyle.css', context=context_pdf,
        )

        return render(request, self.template_name, context=context)


def template1(request):

    output_pdf = 'convert_html_to_pdf.pdf'
    background_default = 'static/img/template_background.png'

    context = {
        'title': 'Community Grow',
        'subTitle': 'metricool',
        'start_date': datetime.datetime.now(),
        'end_date': datetime.datetime.now(),
        'logo': '/static/img/somate-verticle.svg',
        'background_default': f'/{background_default}',
        'tmpIMage': '/static/img/report-pages-bg.png',
    }

    background_default = get_abosulte_path_of_file(background_default)
    context_pdf = {
        'title': 'Community Grow',
        'subTitle': 'metricool',
        'start_date': datetime.datetime.now(),
        'end_date': datetime.datetime.now(),
        'logo': get_abosulte_path_of_file('static/img/somate-verticle.svg'),
        'background_default': background_default,
        'tmpIMage': get_abosulte_path_of_file('static/img/report-pages-bg.png'),
    }
    render_string_pdf(
        request, 'core/template_1.html',
        css='static/css/style.css', context=context_pdf,
        outputfile=output_pdf,
    )
    return render(request, 'core/template_1.html',  context=context)
