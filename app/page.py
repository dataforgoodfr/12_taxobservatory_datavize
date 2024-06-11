import inspect
from taipy.gui import Markdown
from app import config as cfg

class Page:
    def __init__(self, id:str):
        self.id= id
        
    def markdown(self) -> Markdown:
        # caller = inspect.currentframe().f_back
        # print("PAGED Called from module", caller.f_globals['__name__'])
        # print(f"{cfg.PAGES_PATH}/{self.id}/{self.id}.md")
        return Markdown(f"{cfg.PAGES_PATH}/{self.id}/{self.id}.md")