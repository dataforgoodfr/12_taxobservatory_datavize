from taipy.gui import State, download
import pandas as pd
import io
import plotly.graph_objects as go

class Viz:
    def __init__(self, id:str, state: State, data: pd.DataFrame=None, fig:go.Figure = None, title:str=None, sub_title:str=None):
        self.id= id
        self.state = state
        self.data = data
        self.fig = fig
        self.title = id if title is None else title
        # Workaround used for responsive to preserve layout
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
    
    def _to_empty() -> dict[str,]:
        return Viz._to_state(None) 
    
    def init(viz_set:set[str]) -> dict[str,dict]:
        viz:dict[str,dict] = {}
        for viz_id in viz_set:
            viz[viz_id] = Viz._to_empty()
        return viz