Optional: Emergency Installation
================================

If you already have a Scientific Python distribution, but not Astropy and APLpy, just do::

    pip install astropy
    pip install aplpy

If you have *not* previously installed a Scientific Python distribution, use the
following instructions for an EMERGENCY scientific Python install :-)

1. Go to the Anaconda `Downloads <http://continuum.io/anacondace.html>`_ page.

2. Download the file for your platform

3. On Linux or Mac, do::

      bash <downloaded_file>

  and answer the questions with the default by just pressing ``<enter>``. At
  the end of the install, you will get a message like::

      export PATH=/Users/tom/anaconda/bin:$PATH

  Follow these instructions, rehash or open a new terminal, and then test that
  if you type ``python``, you get a prompt similar to::

      Python 2.7.3 |AnacondaCE 1.3.1 (x86_64)| (default, Jan 10 2013, 12:10:41) 
      [GCC 4.0.1 (Apple Inc. build 5493)] on darwin
      Type "help", "copyright", "credits" or "license" for more information.
      >>>
      
  with ``AnacondaCE`` in the first line.

  On Windows, double click the .exe file to install.

4. Install Astropy with::

      conda install astropy
      pip install aplpy