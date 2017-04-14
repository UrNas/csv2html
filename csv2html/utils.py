"""
utils file include helper function
"""
import pathlib


def get_static_folder(file_name):
    p = pathlib.Path('.')
    return p / f'csv2html/static/{file_name}'
