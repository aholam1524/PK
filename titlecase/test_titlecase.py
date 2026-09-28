from titlecase import titlecase


def test_normal_sentence():
    assert titlecase("hello WORLD") == "Hello World"


def test_already_titlecased_string():
    assert titlecase("Hello World") == "Hello World"


def test_all_caps_string():
    assert titlecase("HELLO WORLD") == "Hello World"


def test_empty_string():
    assert titlecase("") == ""
