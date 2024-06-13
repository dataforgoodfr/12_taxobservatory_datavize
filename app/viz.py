import io
from typing import Any, Optional, Union

import pandas as pd
import plotly.graph_objects as go
from taipy.gui import State, download


class Viz:
    def __init__(
        self,
        id: str,
        state: State,
        data: Union[pd.DataFrame, Any] = None,
        fig: Optional[go.Figure] = None,
        title: Optional[str] = None,
        sub_title: Optional[str] = None,
    ):
        self.id = id
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

    def _to_state(self) -> dict[str, Any]:
        return {
            "data": self.data,
            "fig": self.fig,
            "title": self.title,
            "sub_title": self.sub_title,
            "on_action": self.on_action,
        }

    def to_state(self) -> dict[str, Any]:
        return self._to_state()

    @staticmethod
    def _to_empty() -> dict[str, None]:
        return {
            "data": None,
            "fig": None,
            "title": None,
            "sub_title": None,
            "on_action": None,
        }

    @staticmethod
    def init(viz_set: set[str]) -> dict[str, dict]:
        viz: dict[str, dict] = {}
        for viz_id in viz_set:
            viz[viz_id] = Viz._to_empty()
        return viz
