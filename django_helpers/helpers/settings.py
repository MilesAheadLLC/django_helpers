def set_default(value, default_value):
    """
     Sets default value for a settings configuration variable

     e.g. DEBUG = set_default(os.environ.get('DEBUG'), True))
    """
    if (not value):
        return default_value
    return value
