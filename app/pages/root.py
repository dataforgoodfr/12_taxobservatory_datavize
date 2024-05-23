from taipy.gui import Markdown


def to_text(val):
    return "{:,}".format(int(val)).replace(",", " ")


# Images path
data4good_logo_path = "./images/data4good-logo.svg"
taxplorer_logo_path = "./images/taxplorer-logo.svg"
website_logo_path = "./images/website-logo.svg"
twitter_logo_path = "./images/twitter-logo.svg"
linkedin_logo_path = "./images/linkedin-logo.svg"
eutax_logo_path = "./images/eutax-logo.svg"

# Generate page from Markdown file
root = Markdown("pages/root.md")
