"""
create html file
"""
import csv
from jinja2 import Environment, PackageLoader, select_autoescape

from .utils import get_static_folder

__all__ = ['create_output_html']

env = Environment(
    loader=PackageLoader('csv2html', 'templates'),
    autoescape=select_autoescape('html')
)


def get_data(csv_file):
    file = open(csv_file, 'r')
    csv_data = csv.reader(file)
    csv_headers = next(csv_data)
    return csv_headers, csv_data


template = env.get_template('main.html')


def create_output_html(file_name):
    headers, data = get_data(file_name.csv_input)
    with open(file_name.html_output, 'w') as output:
        static_file = 'style.css'
        output.write(template.render(headers=headers, rows=data, style_url=get_static_folder(static_file).resolve()))
