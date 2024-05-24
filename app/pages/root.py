from taipy.gui import Markdown, navigate


def to_text(val):
    return "{:,}".format(int(val)).replace(",", " ")


def goto_d4g_website(state):
    navigate(state, "https://dataforgood.fr/", tab="_blank")


# Generate page from Markdown file
root = Markdown("pages/root.md")
