============
Fruit Basket
============
.. image:: https://github.com/cmeza99/fruit-basket/workflows/Tests/badge.svg?branch=master
     :target: https://github.com/cmeza99/fruit-basket/actions?workflow=Tests
     :alt: CI Status

Generates a report on fruit basket inventory.

Installation
============
.. code-block:: console

   pip install git+https://github.com/cmeza99/fruit-basket.git

Usage
=====

CLI
---
.. code-block:: console

   usage: fruit_basket [-h] [-v] FILE

   Fruit Basket CLI Help

   positional arguments:
    FILE           Fruit basket inventory file(csv).

   optional arguments:
    -h, --help     show this help message and exit
    -v, --version  show program's version number and exit

Module
------
.. code-block:: console

   python3 -m fruit_basket [-h] [-v] FILE

To Do:
======

* Tests Fixtures
   * Setup / Tear Down
   * Parametrizing
* Test Exceptions
* Test CLI
* Documentation Generation to Github Pages

License
=======
Copyright 2020 Carlos Meza

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
