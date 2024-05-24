from taipy.gui import Markdown, navigate


def to_text(val):
    return "{:,}".format(int(val)).replace(",", " ")


# Path to images
data4good_logo_path = "./images/data4good-logo.svg"
eutax_logo_path = "./images/eutax-logo.svg"


def goto_d4g_website(state):
    navigate(state, "https://dataforgood.fr/", tab="_blank")


# Generate page from Markdown file
root = Markdown("pages/root.md")
