#!/usr/bin/env python

import os
import glob

from setuptools import setup, Command


class BuildNotes(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        import os
        import shutil
        import tempfile

        from IPython.nbconvert.nbconvertapp import NbConvertApp

        import sys
        for arg in range(len(sys.argv[1:])):
            sys.argv.pop(-1)

        # Convert the solutions to HTML notebooks.

        app = NbConvertApp()
        app.initialize()
        app.export_format = 'html'
        for notebook in (glob.glob('solutions/*.ipynb')):
            app.notebooks = [notebook]
            app.output_base = notebook.replace('.ipynb', '')
            app.start()

        # Make an index of all notes
        f = open('solutions.html', 'w')
        f.write("<html>\n  <body>\n")

        f.write("    <h1>Solutions:</h1>\n")
        f.write("    <ul>\n")
        for page in glob.glob('solutions/*.html'):
            f.write('      <li><a href="{0}">{1}</a></li>\n'.format(page, os.path.basename(page).replace('.html', '')))
        f.write('    </ul>\n')

        f.write('  </body>\n</html>')
        f.close()


class DeployNotes(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        SERVER = os.environ["PY4SCI_SERVER"]
        USER = os.environ["PY4SCI_USER"]

        import getpass
        from ftplib import FTP
        from astropy.utils.console import ProgressBar

        ftp = FTP(SERVER)
        ftp.login(user=USER, passwd=getpass.getpass())

        ftp.cwd('/public_html/PY4SCI_WS_2013_14')

        for slides in ProgressBar.iterate(glob.glob('solutions/data/*')
                                          + glob.glob('solutions/*.html')):
            try:
                remote_size = ftp.size(slides)
            except:
                remote_size = None
            local_size = os.path.getsize(slides)
            if local_size != remote_size:
                ftp.storbinary('STOR ' + slides, open(slides, 'rb'))

        ftp.storbinary('STOR solutions.html', open('solutions.html', 'rb'))

        ftp.quit()


class RunNotes(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        # Now convert the lecture notes, problem sets, and practice problems to
        # HTML notebooks.

        from runipy.notebook_runner import NotebookRunner

        start_dir = os.path.abspath('.')

        for notebook in (glob.glob('solutions/*.ipynb')):
            os.chdir(os.path.dirname(notebook))
            r = NotebookRunner(os.path.basename(notebook), pylab=True)
            r.run_notebook(skip_exceptions=True)
            r.save_notebook(os.path.basename(notebook))
            os.chdir(start_dir)


setup(name='py4sci_solutions', cmdclass={'run':RunNotes, 'build': BuildNotes, 'deploy':DeployNotes})
