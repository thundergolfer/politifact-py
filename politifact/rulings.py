
class Ruling():
    def __init__(self, name, slug, graphic):
        self.name = name
        self.slug = slug
        self.graphic = graphic


PANTS_ON_FIRE = Ruling(
    'Pants on Fire!',
    'pants-fire',
    'http://static.politifact.com.s3.amazonaws.com/rulings/tom-pantsonfire.gif'
)
TRUE = Ruling(
    'True',
    'true',
    'http://static.politifact.com.s3.amazonaws.com/rulings/tom-pantsonfire.gif'
)
HALF_TRUE = Ruling(
    'Half-True',
    'half-true',
    'http://static.politifact.com.s3.amazonaws.com/rulings/tom-halftrue.png'
)

FULL_FLOP = Ruling(
    'Full Flop',
    'full-flop',
    'http://static.politifact.com.s3.amazonaws.com/rulings/fom-fullFlop.png'
)

MOSTLY_FALSE = Ruling(
    'Mostly False',
    'barely-true',
    'http://static.politifact.com.s3.amazonaws.com/rulings/tom-mostlyfalse.png'
)

HALF_FLIP = Ruling(
    'Half Flip',
    'half-flip',
    'http://static.politifact.com.s3.amazonaws.com/rulings/fom-halfFlip.png'
)

NO_FLIP = Ruling(
    'No Flip',
    'no-flip',
    'http://static.politifact.com.s3.amazonaws.com/rulings/fom-noflip.png'
)

FALSE = Ruling(
    'False',
    'false',
    'http://static.politifact.com.s3.amazonaws.com/rulings/tom-false.png'
)

MOSTLY_TRUE = Ruling(
    'Mostly True',
    'mostly-true',
    'http://static.politifact.com.s3.amazonaws.com/rulings/tom-mostlytrue.png'
)

rulings = [
    PANTS_ON_FIRE,
    TRUE,
    HALF_TRUE,
    MOSTLY_TRUE,
    FALSE,
    NO_FLIP,
    HALF_FLIP,
    FULL_FLOP
]


def map_ruling_slug_to_ruling(slug):
    for r in rulings:
        if r.slug == slug:
            return r
    return None
