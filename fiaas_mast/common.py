import collections
import uuid


def dict_merge(dct, merge_dct):
    """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.
    :param dct: dict onto which the merge is executed
    :param merge_dct: dct merged into dct
    :return: None
    """
    for k, v in merge_dct.items():
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.Mapping)):
            dict_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]


def generate_random_uuid_string():
    id = uuid.uuid4()
    return str(id)


def make_safe_name(name):
    safe_name = name.replace('_', '-')
    return safe_name


class ClientError(Exception):
    def __init__(self, description, *args, **kwargs):
        self.code = 422
        self.name = "Unprocessable Entity"
        self.description = description
