# pythonPlayground

This is where I hope to store some python scripts I'm working on. Unfortunately, because this is public, I can't do any REAL work in it because API keys. Boo. 


---- adding in some more content to test confluence stuff ----


Pyrseas
=======

.. image:: https://circleci.com/gh/DevotedHealth/Pyrseas/tree/master.svg?style=svg
    :target: https://circleci.com/gh/DevotedHealth/Pyrseas/tree/master
    
Pyrseas provides utilities to describe a PostgreSQL database schema as
YAML, to verify the schema against the same or a different database
and to generate SQL that will modify the schema to match the YAML
description.

Features
--------

- Outputs a YAML description of a Postgres database's tables
  and other objects (metadata), suitable for storing in a version
  control repository

- Generates SQL statements to modify a database so that it will match
  an input YAML/JSON specification

- Generates an augmented YAML description of a Postgres database
  from its catalogs and an augmentation specification.

Requirements
------------

- PostgreSQL 9.3 or higher

- Python 2.7 or higher

License
-------

Pyrseas is free (libre) software and is distributed under the BSD
license.  Please see the LICENSE file for details.
