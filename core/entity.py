from __future__ import annotations


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
        data_frame_targets: list,
        name_report: str,
        kind_plot: str = 'line',
        image_type='svg',
    ):

        self.dataFrameTarget = data_frame_targets

        self.kindPlot = kind_plot
        self.name_report = name_report
        self.image_type = image_type
        self.target = f'static/{self.name_report}.{self.image_type}'
