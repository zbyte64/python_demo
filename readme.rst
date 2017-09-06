Day 1
=====

Python Idioms: http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html

Hitch hikers guide to python: http://docs.python-guide.org/en/latest/


Anaconda: https://www.continuum.io/anaconda-overview


Python Builtins to Know:

* help
* dir
* print
* list
* dict


Day 2
=====

Evolution of dictionaries: https://dl.dropboxusercontent.com/u/3967849/sfmu2/_build/html/main.html

Finite State Machines

Python builtins to Know:

* tuple
* hash
* iter
* is vs ==
* yield
* control structures (try except, if else, while, for in)


Day 3
=====


Design Principles: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PatternConcept.html#design-principles

Jupyter Notebooks: http://jupyter.org/
https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

Pythonic things to Know:

* collections
* requests
* BeautifulSoup4 (select, text)
* json
* pickle
* codecs
* class, __init__, self, super
* property, classmethod, staticmethod
* nltk




Day 4
=====

Pythonic things to Know:

* __call__
* lambda
* type
* isinstance
* pandas
* twisted


Pandas:

* Series & DataFrames https://pandas.pydata.org/pandas-docs/stable/dsintro.html
* Load Data: https://pandas.pydata.org/pandas-docs/stable/io.html
* Overview: https://pandas.pydata.org/pandas-docs/stable/10min.html
* Cookbook: https://github.com/jvns/pandas-cookbook

Pandas UCMR example


Side-effects: https://www.quora.com/What-is-a-side-effect-in-programming

Design Patterns:

* factory: https://en.wikipedia.org/wiki/Factory_method_pattern#Python
* adaptors: https://en.wikipedia.org/wiki/Adapter_pattern#Python


Why Twisted: http://www.aosabook.org/en/twisted.html

* blocking I/O vs async ( Reactor )
* loose coupling all the way down ( Transports, Protocols)

Twisted uses factories to allow protocols to bind to either server or client:
https://twistedmatrix.com/documents/8.1.0/api/twisted.internet.protocol.Factory.html


Class Assignment: Find Data, Scrape It, Put it in a Pandas Dataframe
OR adapt game to twisted (Telnet Server)


Day 5
=====

Pythonic things to Know:

* threading
* multiprocessing / message passing
* asyncio


Async strategies:

* callbacks
* deferred
* await
* gevent monkey patch

Asyncio primer: https://pymotw.com/3/asyncio/coroutines.html
Aiohttp: http://aiohttp.readthedocs.io/en/stable/


Threading topics:

* Main thread, child threads & joining
* Shared memory
* GIL
* Locks & Semaphores

Example: semaphore downloader; will download many urls, but only one request at a time per domain.


Day 6
=====

* OSI Model
* 12 factor applications - https://12factor.net/
* environment variables
* logging - http://docs.python-guide.org/en/latest/writing/logging/
* twisted clients: IRC, sendmail, broadcast
* twistedweb
* argparse
* scikit-learn

Examples:

* telnet_game.py
* ircLogBot.py


Day 7
=====

* gensim - https://radimrehurek.com/gensim/
* django - https://tutorial.djangogirls.org/
* extending django manually - https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/
* django packages - https://djangopackages.org/
* example install: comments


Day 8
=====

* python visualization libraries - seaborn, bokeh, holoviews, altair
* seaborn - https://seaborn.pydata.org/introduction.html - matplotlib ++
* bokeh - https://bokeh.pydata.org/en/latest/ - d3.js
* holoviews - http://holoviews.org/ - bokeh simplified
* altair - https://github.com/altair-viz/altair - declarative graphs

* Django API docs - https://docs.djangoproject.com/en/1.11/topics/
* Builtin template tags - https://docs.djangoproject.com/en/1.11/ref/templates/builtins/
* Model Fields - https://docs.djangoproject.com/en/1.11/ref/models/fields/
* Django Middleware - https://docs.djangoproject.com/en/1.11/topics/http/middleware/
* Sessions - https://docs.djangoproject.com/en/1.11/topics/http/sessions/
* Forms - https://docs.djangoproject.com/en/1.11/topics/forms/


Day 9
=====

Django Admin

* https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
* list_display
* ModelAdmin options
* Template override: "admin/<appname>/<modelname>/<view>.html" - https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#templates-which-may-be-overridden-per-app-or-model
* Admin actions
* Admin Themes
* Autocomplete widgets - https://django-select2.readthedocs.io/en/latest/index.html
* Image Cropping - https://github.com/jonasundderwolf/django-image-cropping
* Hierarchies - http://django-treebeard.readthedocs.io/en/latest/
