dash-covid19: A Dash App for Covid-19 Data
==========================================

[![Project Status: Concept -- Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)
[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Heroku Deploy Status](https://heroku-badge.herokuapp.com/?app=dash-covid19-pro)](https://dash-covid19-pro.herokuapp.com/)
[![Travis Build Status](https://travis-ci.org/rbpatt2019/dash-covid19.svg?branch=master)](https://travis-ci.org/rbpatt2019/dash-covid19)
[![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/rbpatt2019/dash-covid19)
[![Test Coverage](https://codecov.io/gh/rbpatt2019/dash-covid19/branch/master/graph/badge.svg)](https://codecov.io/gh/rbpatt2019/dash-covid19)
[![Updates](https://pyup.io/repos/github/rbpatt2019/dash-covid19/shield.svg)](https://pyup.io/repos/github/rbpatt2019/dash-covid19/)
[![Codestyle: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Introduction
------------

> **NOTE**: This project is still in early planning phases

[dash-covid19](https://github.com/rbpatt2019/dash-covid19/) is a
[Dash](https://dash.plotly.com/) app for viewing up-to-date information related
to the spread of Covid-19 using the data provided by a variety of sources collated by [Our World in Data](https://ourworldindata.org/).

Docs and Code
-------------

This app is hosted by Heroku and lives [here](https://dash-covid19-pro.herokuapp.com/)

The documentation is forthcoming, and will likely live as either it's own app, or a tab within this app.

The code lives in [the repo](https://github.com/rbpatt2019/dash-covid19/).

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
[Our World in Data](https://ourworldindata.org/) (OWID)
when constructing my app. The data are freely avaialble, and can be found in their
[repo](https://github.com/owid/covid-19-data/tree/master/public/data).
Their principle source of data is the
[European Center for Disease Prevention and Control](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)
(ECDC), who provide daily updates of worldwide statistics.
OWID thoroughly discusses all their sources, methods for data handling,
and the reasoning behind any decisions they make relating to data management.
Please, visit their [repo](https://github.com/owid/covid-19-data/tree/master/public/data)
for any questions you may have about the data.

Usage
-----

Having now fully integrated Travis, Code-cov, PyUp, and Percy, development is beginning on a UI.

Eventually, it will provde a graphic interface that allows the end-user to visualise and filter Covid-19 data.

Recent Changes
--------------

Please see the
[CHANGELOG](https://github.com/rbpatt2019/dash-covid19/blob/master/CHANGELOG.md)

Contributing
------------

If you would like to contribute to development, please see the [instructions](CONTRIBUTING.md)


Next Steps
----------

-   Develop a basic app framework.

Thank Yous
----------

-   [Dash](https://dash.plotly.com/) for developing an incredible
    framework and excellent documentation.
-   [OWID](https://ourworldindata.org/) for providing an incredible
	 resource amid a rapidly evolving situation.
