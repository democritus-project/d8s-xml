import functools

# TODO: get the decorators below working properly...


def xml_read_first_arg_string(func):
    """Return an XML element for first argument (if it is a string)."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from .xml_data import xml_read

        first_arg = args[0]
        other_args = args[1:]

        if isinstance(first_arg, str):
            first_arg_xml_element = xml_read(first_arg)
            return func(first_arg_xml_element, *other_args, **kwargs)
        else:
            return func(*args, **kwargs)

    return wrapper


def stringify_first_arg_xml_element(func):
    """If the first arg is an XML element, send its string representation into the function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from .xml_data import xml_as_string, _is_xml_element

        first_arg = args[0]
        other_args = args[1:]

        if _is_xml_element(first_arg):
            first_arg_string = xml_as_string(first_arg)
            return func(first_arg_string, *other_args, **kwargs)
        else:
            return func(*args, **kwargs)

    return wrapper
