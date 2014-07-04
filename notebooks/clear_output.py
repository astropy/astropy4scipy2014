import os
import glob

from IPython.nbformat.current import read, write

for notebook in glob.glob('*.ipynb'):

    with open(notebook, 'r') as f:
        nb = read(f, 'json')

    for ws in nb.worksheets:
        for cell in ws.cells:
            if cell.cell_type == 'code':
                cell.outputs = []

    with open(notebook, 'w') as f:
        write(nb, f, 'json')