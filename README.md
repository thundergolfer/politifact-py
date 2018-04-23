

# Politifact-Py [![Documentation Status](https://readthedocs.org/projects/politifact-py/badge/?version=latest)](http://politifact-py.readthedocs.io/en/latest/?badge=latest)

#####  **NOTE:** *This API Wrapper was hastily created to facilitate another high-priority project. It is still under active development and may be pretty ugly and wonky.*

----

<p align="center">
  <img src="./repo-image.png"/>
</p>

Python REST API wrapper for the Pulitzer Prize winning [Politifact](http://www.politifact.com/) organisation's [public API](http://static.politifact.com/api/doc.html).

-----

## Usage

```python
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
```


## Installation

`pip install politifact`

## Development

#### Dependencies

The project uses [pipenv](https://github.com/pypa/pipenv) for package and virtual environment management. Install it with `pip install pipenv`

1. Get all dependencies with `pipenv install --dev`

#### Testing

`python -m pytest tests/`

#### Releasing

> Make sure you have `twine` installed. `pip install twine`

1. `python setup.py sdist`
2. Create a [Github Release for the project](https://github.com/thundergolfer/politifact-py/releases)
3. `twine upload dist/*`

### License

Released under the MIT license. See [LICENSE](LICENSE) for further details.
