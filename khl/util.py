"""common hax"""


def unpack_id(obj) -> str:
    """extract obj's id if not str"""
    return obj if isinstance(obj, str) or isinstance(obj, int) else obj.id
