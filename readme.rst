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

* logging
* argparse
* threading
* multiprocessing / message passing
* asyncio


Async strategies:

* callbacks
* deferred
* await


Threading topics:

* Main thread, child threads & joining
* Shared memory
* GIL
* Locks & Semaphores
