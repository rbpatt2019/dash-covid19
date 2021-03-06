For contributors
================

Comments, criticisms, and concerns are always welcome! If you would like
to help with development, please follow the steps below. This project
depends on `Poetry <https://poetry.eustace.io>`_ for all
things dependency and development related. Make sure it\'s installed, or
else all this will fail. It\'s an awesome tool, I highly recommend you
check it out!

Clone the repo
--------------

.. code-block:: sh
   :linenos:

   git clone https://github.com/rbpatt2019/dash-covid19
   cd ToDonePy

Make a new environment
----------------------

Follow your own protocol! One option, using
`pyenv-virtualenv <https://github.com/pyenv/pyenv-virtualenv>`_, is:

.. code-block:: sh
   :linenos:

   pyenv virtualenv ToDonePy
   pyenv local ToDonePy

Regardless of how you do it, run the following once its created:

.. code-block:: sh
   :linenos:

   make develop

I have `poetry` configured to create its virtualenvs in
`\~/.pyenv/versions/`, so the above automatically creates my
environment. Then, I use `pyenv local` to set this
virtualenv in the root of the project!

Start developing
----------------

Checkout the
`Makefile <https://github.com/rbpatt2019/dash-covid19/blob/master/Makefile>`_
for lots of useful commands for testing, linting, and many others!
Before committing any changes, I\'d strongly recommend creating a new
branch:

.. code-block:: sh
   :linenos:

   git checkout -b new_feature

And contribute!
---------------

Once you\'re ready to share your changes, fork the repository on github.
Then, add it as a remote to the repo and push the changes there.

.. code-block:: sh
   :linenos:

   git remote add origin https://github.com/YOUR_USER/ToDonePy.git
   git push origin new_feature

Finally, open a pull request, and I\'ll review it as soon as I can!

If you\'re a command line nut like me, this can all be done from the
command line using `hub <https://github.com/github/hub>`_, a CLI for
interacting with the github api. See their
`repo <https://github.com/github/hub>`_ for installation instructions.
Instead of the above, do:

.. code-block:: sh
   :linenos:

   hub fork --remote-name=origin
   git push origin new_feature
   hub pull-request

This will fork the repo, push your changes, and create a pull request,
all without leaving the command line!
