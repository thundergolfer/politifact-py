**politifact-py** is an API wrapper for the Politifact public REST API.

.. code-block:: python
  from politifact import Politifact

  p = Politifact()
  obama_related = p.statements().people('Barack Obama')

  for statement in obama_related:
    print(statement.ruling)

  # OUTPUT:
  # > True
  # > Pants On Fire!
  # > Mostly True
  # > ...

Get It Now
==========

.. code-block:: bash

    $ pip install politifact
