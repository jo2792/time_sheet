from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

class MonthOverview(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        months = ["Januar 2020","Februar 2020","März 2020","April 2020",
                    "Mai 2020","Juni 2020","Juli 2020","August 2020",
                    "September 2020","Oktober 2020","November 2020",
                    "Dezember 2020"]

        widget_content = QtWidgets.QVBoxLayout()

        entry_dict = {}

        for month in months:
            dict_name = month.replace(' ','_').lower()
            entry_dict[dict_name] = {}
            entry_dict[dict_name]['display'] = month[:3] + '\n' + month[-2:]
            entry_dict[dict_name]['object'] = QtWidgets.QPushButton(entry_dict[dict_name]['display'])

            entry_dict[dict_name]['object'].setFont(QtGui.QFont('SansSerif', pointSize=22))
            entry_dict[dict_name]['object'].setStyleSheet("QPushButton {background: rgb(212, 212, 212)}")
            entry_dict[dict_name]['object'].setMinimumWidth(130)
            entry_dict[dict_name]['object'].setMaximumWidth(150)
            entry_dict[dict_name]['object'].setMinimumHeight(200)
            entry_dict[dict_name]['object'].setMaximumHeight(200)

            widget_content.addWidget(entry_dict[dict_name]['object'])

        widget_content.setAlignment(QtCore.Qt.AlignHCenter)
        widget_content.setSpacing(20)

        # Scroll Area
        scroll_area_content = QtWidgets.QWidget()
        scroll_area_content.setLayout(widget_content)
        scroll_area = QtWidgets.QScrollArea()

        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_area_content)
        scroll_area.setStyleSheet("QScrollArea { background-color: white; border: none; }")
        scroll_area.verticalScrollBar().setValue(scroll_area.verticalScrollBar().maximum())


        self.widget_line = QtWidgets.QFrame()
        self.widget_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.widget_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        widget_layout = QtWidgets.QHBoxLayout()

        widget_layout.addWidget(scroll_area)
        widget_layout.addWidget(self.widget_line)

        self.setLayout(widget_layout)
