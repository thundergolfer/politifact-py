def parse_name_str(name):
    tokens = name.lower().split()
    if len(tokens) is not 2:
        raise ValueError(
            'A person\'s name must be of the form \'<firstname> <lastname>\'. Got: {}'.format(name)
        )
    return tokens


def slugify(*tokens):
    return '-'.join(tokens)
