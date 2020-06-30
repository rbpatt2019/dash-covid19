dash-covid19: A Dash App for Covid-19 Data
==========================================

.. image:: https://www.repostatus.org/badges/latest/active.svg
   :alt: Project Status: Active – The project has reached a stable, usable state and is being actively developed.
   :target: https://www.repostatus.org/#active
.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :alt: GPLv3 License
   :target: https://www.gnu.org/licenses/gpl-3.0
.. image:: https://travis-ci.org/rbpatt2019/dash-covid19.svg?branch=master
   :alt: Travis Build Status
   :target: https://travis-ci.org/rbpatt2019/dash-covid19
.. image:: https://percy.io/static/images/percy-badge.svg
   :alt: This project is using Percy.io for visual regression testing.
   :target: https://percy.io/rbpatt2019/dash-covid19)
.. image:: https://codecov.io/gh/rbpatt2019/dash-covid19/branch/master/graph/badge.svg
   :alt: Code Coverage
   :target: https://codecov.io/gh/rbpatt2019/dash-covid19
.. image:: https://pyup.io/repos/github/rbpatt2019/dash-covid19/shield.svg
   :alt: Updates
   :target: https://pyup.io/repos/github/rbpatt2019/dash-covid19/
.. image:: https://readthedocs.org/projects/dash-covid19/badge/?version=latest
   :target: https://dash-covid19.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :alt: Codestyle - Blacks
   :target: https://github.com/ambv/black

Introduction
------------

`dash-covid19 <https://github.com/rbpatt2019/dash-covid19/>`_ is a
`Dash <https://dash.plotly.com/>`_ app for viewing up-to-date information related
to the spread of Covid-19 using the data provided by a variety of sources collated by `Our World in Data <https://ourworldindata.org/>`_.

Docs and Code
-------------

This app is hosted by Heroku and lives `here <https://dash-covid19-pro.herokuapp.com/>`_.

The helpful hints are embedded throughout the app. Any where you see underlined text, you can mouse over to get a pop-up about what each component does.

The documentation lines `here <https://dash-covid19.readthedocs.io/en/latest/>`_.

The code lives in `here <https://github.com/rbpatt2019/dash-covid19/>`_.

Usage
-----

The app contains 4 pages and 3 external links. The home page provides a brief summary of all the assorted links within the app, as well as an explanation of why I built the app.

The "Explorer" page provides an interactive graph to help the user, well, explore the most up-to-date Covid-19 data.
This page is constantly changing, so check back to see how the graphs evolve!

The "World Map" pages provides an interactive, global map that plots information on top of, well, a map! Here you can see not only interactions,
but regional impacts as well. You can change the data represented by the size and colour of the dots.

The "Data Table" pages displays the data in an interactive table that allows the user to sort and filter columns of interest.
The four left-most columns (iso_code, continent, location, and date) remain fixed as you scroll.

As this project is proudly open source, the Navbar also includes three external links. These will take you back to this repo to view the code, to OWID's repo to view the data, or to ReadTheDocs to view the source code documentation. This way, you can see exactly where the data comes from, and how it is being handled.

About the Data
--------------

Fundametally, good data science requires two things: good data and good questions.
Since good questions frequently evolve from exploratory data analysis,
one could argue that good data science needs only one things: good data.
Crap in, crap out, as they say...
Now, how does one get data?
As a trained biologist, my first thought is structured experiments,
with repeated samples, controls groups, and as many data points as feasibly possible.
Unfortunately, this structured framework isn't always possible,
particularly when dealing with rpaidly evolving, as-of-yet not fully understood situations
like the current Covid-19 pandemic.
In these cases, where limitations are inherent to the problem, transparency becomes critical.
We must accept that the data are not, and cannot be, perfect,
recognise the limitations in the data,
and be open about any limitations when discussing interpretations of the data.

To that end, I have elected to use data collated by the team at
`Our World in Data <https://ourworldindata.org/>`_ (OWID)
when constructing my app. The data are freely avaialble, and can be found in their
`repo <https://github.com/owid/covid-19-data/tree/master/public/data>`_.
Their principle source of data is the
`European Center for Disease Prevention and Control <https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide>`_
(ECDC), who provide daily updates of worldwide statistics.
OWID thoroughly discusses all their sources, methods for data handling,
and the reasoning behind any decisions they make relating to data management.
Please, visit their `repo <https://github.com/owid/covid-19-data/tree/master/public/data>`_
for any questions you may have about the data.


Recent Changes
--------------

Please see the
`CHANGELOG <https://github.com/rbpatt2019/dash-covid19/blob/master/CHANGELOG.md>`_

Contributing
------------

If you would like to contribute to development, please see the `instructions <CONTRIBUTING.md>`


Next Steps
----------

- Add data summary page
- Refactor layout to move repetitive structures to helpers
- Continue to expand documentation
- Caching to improve performance

Thank Yous
----------

- `Dash <https://dash.plotly.com/>`_ for developing an incredible framework and excellent documentation.
- `Dash Bootstrap Components <https://dash-bootstrap-components.opensource.faculty.ai/>`_ for making it so much easier to layout the app.
- `OWID <https://ourworldindata.org/>`_ for providing an incredible resource amid a rapidly evolving situation.
