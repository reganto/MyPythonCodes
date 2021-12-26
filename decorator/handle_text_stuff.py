def handle_text_stuff(convert_type, text):
    def make_upper(t):
        return t.upper()

    def make_title(t):
        return t.title()

    def make_lower(t):
        return t.lower()

    if convert_type == "upper":
        return make_upper(text)
    elif convert_type == "title":
        return make_upper(text)
    else:
        return make_lower(text)
