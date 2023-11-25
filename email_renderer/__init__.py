import jinja2


def compile_mail(name: str, vals: dict) -> str:
    """
    Compiles jinja template and adds values to the template from the input dictionary
    :param name: template name
    :param vals: dictionary of values, do not want to handle types in python I HATE TYPINGS AND ANNOTATIONS
    :return: compiled HTML template
    """

    template = ""
    with open(f"static/mails/{name}", "r") as f:
        template = f.read()
    env = jinja2.Environment()
    template = env.from_string(template)
    return template.render(vals)
