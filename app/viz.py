from taipy.gui import State, download
import pandas as pd
import io 

class Viz:
    def __init__(self, id:str, state: State, data: pd.DataFrame=None, fig = None, title:str=None, sub_title:str=None):
        self.id= id
        self.state = state
        self.data = data
        self.fig = fig
        self.title = id if title is None else title
        # Used for responsive to preserve layout
        # "sub_title": "------------ --------- ---------"
        self.sub_title = "------------ --------- ---------" if sub_title is None else sub_title   

    def on_action(self):       
        self._on_download() 
                
    def _on_download(self):
        buffer = io.StringIO()
        data = self.data
        if type(data) == pd.DataFrame:
            data.to_csv(buffer)
        else:
            buffer.write(self.sub_title + "\n" + str(data))
        download(self.state, content=bytes(buffer.getvalue(), "UTF-8"), name="data.csv")


    def _to_state(self) -> dict[str]:
        return {
            "data": None if self is None else self.data,
            "fig": None if self is None else self.fig,
            "title": None if self is None else self.title,
            "sub_title": None if self is None else self.sub_title,
            "on_action": None if self is None else self.on_action
        }
        
    def to_state(self) -> dict[str]:
        return self._to_state()
    
    def TO_EMPTY() -> dict[str,]:
        return Viz._to_state(None) 
