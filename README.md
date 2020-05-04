dash-covid19: A Dash App for WHO Data
=====================================

[![Project Status: Concept -- Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)
[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://docs.python.org/3/contents.html)
[![Travis Build Status](https://travis-ci.org/rbpatt2019/dash-covid19.svg?branch=master)](https://travis-ci.org/rbpatt2019/dash-covid19)
[![Test Coverage](https://codecov.io/gh/rbpatt2019/dash-covid19/branch/master/graph/badge.svg)](https://codecov.io/gh/rbpatt2019/dash-covid19)
[![Updates](https://pyup.io/repos/github/rbpatt2019/dash-covid19/shield.svg)](https://pyup.io/repos/github/rbpatt2019/dash-covid19/)
[![Codestyle: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Introduction
------------

View the World Health Organization\'s Covid-19 situation report data.

> **NOTE**: This project is still in early planning phases

[dash-covid19](https://github.com/rbpatt2019/dash-covid19/) is a
[Dash](https://dash.plotly.com/) app for viewing the information related
to the spread of Covid-19 using the data provided in the World Health
Organization\'s ([WHO](https://www.who.int/)) daily [situation
reports](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/).

The data is curated and provided by [Namara](https://app.namara.io/),
and manually downloaded by myself. As this project develops, automatic
queries using Namara\'s API will likely be incorporated.

Docs and Code
-------------

The documentation is forthcoming, and will likely live as either it's own app, or a tab within this app.

The code lives at <https://github.com/rbpatt2019/dash-covid19/> .

Installation
------------

> **NOTE**: This project has not yet been formally released/deployed.

As this is a Dash app, no formally installation is necessary! Simply visit [the app](https://dash-covid19-pro.herokuapp.com/)

If you would like to contribute to development, please see the [instructions](CONTRIBUTING.md)

Usage
-----

The app will provide an iteractive iterface to filter data by country
and date.

Recent Changes
--------------

Please see the
[CHANGELOG](https://github.com/rbpatt2019/dash-covid19/blob/master/CHANGELOG.rst)

Next Steps
----------

-   Develop a basic app framework.

Thank Yous
----------

-   [Dash](https://dash.plotly.com/) for developing an incredible
    framework and excellent documentation.
-   [WHO](https://www.who.int/) for providing accurate information
    during these unusual times.
-   [Namara](https://app.namara.io/) for curating the data in an
    easy-to-parse format.
