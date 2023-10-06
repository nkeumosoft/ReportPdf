from __future__ import annotations

import logging
import os
from pathlib import Path

import matplotlib.pyplot as plt
import pdfkit
from django.shortcuts import render

from core.entity import PlotObject


def get_abosulte_path_of_file(filename):
    base_dir = Path(__file__).resolve().parent
    logging.error(base_dir)
    absolute_path: str = os.path.join(base_dir, filename)
    logging.error(absolute_path)
    return absolute_path


def render_string_to_pdf(request, template_name, outputfile='report.pdf', context={}, css='static/css/coverstyle.css'):

    # Render HTML template with elements from report
    source_html = bytes.decode(
        render(request, template_name, context=context).content,
    )
    logging.error(source_html)
    # Convert to PDF
    pdfkit.from_string(
        source_html,
        output_path=f'core/assets/{outputfile}', options={
            'enable-local-file-access': '',
            'encoding': 'UTF-8',
            'orientation': 'landscape',
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-bottom': '0',
            'margin-left': '0',
        },
        css=get_abosulte_path_of_file(css),
    )


def graph_targets(graph_to_plot: PlotObject):
    # Create graph
    plt.plot(
        graph_to_plot.dataFrameTarget,
    )

    # Save image as SVG
    plt.savefig(
        get_abosulte_path_of_file(graph_to_plot.target),
    )
