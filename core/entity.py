from __future__ import annotations

from pandas import DataFrame


class PlotObject:
    """
            data_frame_targets,
                x: str,
                y: str,
                name_report:str,
                kind_plot: str = 'line',
                image_type='svg'
    """

    def __init__(
        self,
        data_frame_targets: DataFrame,
        x: str,
        y: str,
        name_report: str,
        kind_plot: str = 'line',
        image_type='svg',
    ):

        self.dataFrameTarget = data_frame_targets
        self.x = x
        self.y = y
        self.kindPlot = kind_plot
        self.name_report = name_report
        self.image_type = image_type
        self.target = f'plot_image_render/{self.name_report}.{self.image_type}'
