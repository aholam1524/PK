import re


def titlecase(text):
    return re.sub(r"\S+", lambda match: match.group().capitalize(), text)
