""" Module to build the grafic interface to interact with the user """
__authors__ = "Jordan Alwon"
__copyright__ = "Copyright 2020"

import sys
from PySide2 import QtWidgets, QtCore, QtGui

class EditEntry(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        sp_retain = QtWidgets.QSizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        sp_retain.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)

        def set_default_label_style(widget):
            widget.setSizePolicy(sp_retain)
            widget.setAlignment(QtCore.Qt.AlignLeft)
            widget.setFont(QtGui.QFont('SansSerif',pointSize=16))

            return widget

        def set_default_field_style(widget):
            widget.setSizePolicy(sp_retain)
            widget.setAlignment(QtCore.Qt.AlignCenter)
            widget.setFont(QtGui.QFont('SansSerif',pointSize=16))

            return widget

        ### Define wideget elements

        # Headline
        headline_label = QtWidgets.QLabel("Eintrag bearbeiten")
        headline_label.setAlignment(QtCore.Qt.AlignLeft)
        font = QtGui.QFont('SansSerif',pointSize=20)
        font.setUnderline(True)
        headline_label.setFont(font)
        headline_label.setSizePolicy(sp_retain)

        # Work Date
        date_label = set_default_label_style(QtWidgets.QLabel("Datum:"))
        date_field = set_default_field_style(QtWidgets.QDateEdit())
        date_field.setDisplayFormat('dd.MM.yyyy ')
        date_field.setDate(QtCore.QDate.currentDate())
        date_field.setCalendarPopup(True)
        
        # Work start time
        start_time_label = set_default_label_style(QtWidgets.QLabel("Beginn:"))
        start_time_field = set_default_field_style(QtWidgets.QTimeEdit())
        # start_time_label.setMinimumSize()
        # Work end time
        end_time_label = set_default_label_style(QtWidgets.QLabel("Ende:"))
        end_time_field = set_default_field_style(QtWidgets.QTimeEdit())

        # Spoiler Button and Line
        self.fold_button = QtWidgets.QToolButton()
        self.fold_button.setStyleSheet("QToolButton { border: none; }")
        self.fold_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.fold_button.setArrowType(QtCore.Qt.DownArrow)
        # self.fold_button.setText("Erweitert")
        self.fold_button.setCheckable(True)
        self.fold_button.setChecked(False)

        self.fold_line = QtWidgets.QFrame()
        self.fold_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.fold_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Vacation
        self.vacation_label = set_default_label_style(QtWidgets.QLabel("Urlaub:"))
        self.vacation_checkbox = QtWidgets.QCheckBox()
        self.vacation_checkbox.setSizePolicy(sp_retain)
        
        # Comment box
        self.comment_label = set_default_label_style(QtWidgets.QLabel("Kommentar:"))
        self.comment_textbox = QtWidgets.QTextEdit()
        self.comment_textbox.setAlignment(QtCore.Qt.AlignLeft)
        self.comment_textbox.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.comment_textbox.setSizePolicy(sp_retain)

        # Wage
        self.wage_label = set_default_label_style(QtWidgets.QLabel("Stundenlohn:"))
        self.wage_textbox = set_default_field_style(QtWidgets.QLineEdit("10,00"))
        self.wage_textbox.setInputMask('09,99 €')
        
        # creation date
        self.creation_date_label = set_default_label_style(QtWidgets.QLabel("Erstelldatum:"))
        self.creation_date_text = set_default_field_style(QtWidgets.QLineEdit("18.08.2020"))
        self.creation_date_text.setReadOnly(True)
        self.creation_date_text.setStyleSheet("QLineEdit {background: rgb(220, 220, 220) }")

        # modification date
        self.modification_date_label = set_default_label_style(QtWidgets.QLabel("Änderungsdatum:"))
        self.modification_date_text = set_default_field_style(QtWidgets.QLineEdit("19.08.2020"))
        self.modification_date_text.setReadOnly(True)
        self.modification_date_text.setStyleSheet("QLineEdit {background: rgb(220, 220, 220) }")

        # author
        self.author_label = set_default_label_style(QtWidgets.QLabel("Autor:"))
        self.author_text = set_default_field_style(QtWidgets.QLineEdit("Jordan"))
        self.author_text.setReadOnly(True)
        self.author_text.setStyleSheet("QLineEdit {background: rgb(220, 220, 220) }")

        # Buttons
        accept_button = QtWidgets.QPushButton("Ok")
        accept_button.setFont(QtGui.QFont('SansSerif',pointSize=16))
        accept_button.setFixedHeight(40)

        delete_button = QtWidgets.QPushButton("Del")
        delete_button.setFont(QtGui.QFont('SansSerif',pointSize=16))
        delete_button.setFixedHeight(40)

        deny_button = QtWidgets.QPushButton("Nop")
        deny_button.setFont(QtGui.QFont('SansSerif',pointSize=16))
        deny_button.setFixedHeight(40)
        
        # Layout managment
        # Scroll Area
        self.vscroll_layout = QtWidgets.QGridLayout()

        scroll_area_content = QtWidgets.QWidget()
        scroll_area_content.setLayout(self.vscroll_layout)
        scroll_area = QtWidgets.QScrollArea()

        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_area_content)
        scroll_area.setStyleSheet("QScrollArea { background-color: white; border: none; }")

        # Add widgets to Grid
        self.grid_v_pos = 0

        self.add_to_grid(headline_label, horizontal_start=0, horizontal_length=3)

        self.add_to_grid(date_label, 'Label')
        self.add_to_grid(date_field, 'Field')

        self.add_to_grid(start_time_label, 'Label')
        self.add_to_grid(start_time_field, 'Field')

        self.add_to_grid(end_time_label, 'Label')
        self.add_to_grid(end_time_field, 'Field')
        
        self.add_to_grid(self.fold_button, horizontal_start=0, horizontal_length=1)
        self.add_to_grid(self.fold_line, vertical_start=self.grid_v_pos-1, horizontal_start=1, horizontal_length=2)
        
        self.add_to_grid(self.vacation_label, 'Label')
        self.add_to_grid(self.vacation_checkbox, vertical_start=self.grid_v_pos-1, horizontal_start=2, horizontal_length=1)

        self.add_to_grid(self.comment_label, 'Label')
        self.add_to_grid(self.comment_textbox, vertical_length=2, horizontal_start=0, horizontal_length=3)
        
        self.add_to_grid(self.wage_label, 'Label')
        self.add_to_grid(self.wage_textbox, 'Field')

        self.add_to_grid(self.creation_date_label, 'Label')
        self.add_to_grid(self.creation_date_text, 'Field')

        self.add_to_grid(self.modification_date_label, 'Label')
        self.add_to_grid(self.modification_date_text, 'Field')

        self.add_to_grid(self.author_label, 'Label')
        self.add_to_grid(self.author_text, 'Field')

        # Seperation line
        button_line = QtWidgets.QFrame()
        button_line.setFrameShape(QtWidgets.QFrame.HLine)
        button_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        widget_line = QtWidgets.QFrame()
        widget_line.setFrameShape(QtWidgets.QFrame.VLine)
        widget_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Button Area
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(accept_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(deny_button)

        widget_content = QtWidgets.QVBoxLayout()
        widget_content.addWidget(scroll_area)
        widget_content.addSpacing(30)
        widget_content.addWidget(button_line)
        widget_content.addLayout(button_layout)

        widget_layout = QtWidgets.QHBoxLayout()
        widget_layout.addWidget(widget_line)
        widget_layout.addLayout(widget_content)

        self.setLayout(widget_layout)

        self.fold_button.clicked.connect(self.change_visibility)

        self.change_visibility()

    def add_to_grid(self, widget, configuration=None, vertical_start=None,
                    horizontal_start=None, vertical_length=None, horizontal_length=None):
        if configuration == "Label":
            horizontal_start = 0
            horizontal_length = 2
            vertical_start = self.grid_v_pos
            vertical_length = 1
        elif configuration == "Field":
            horizontal_start = 2
            horizontal_length = 1
            vertical_start = self.grid_v_pos
            vertical_length = 1

        if not vertical_start:
            vertical_start = self.grid_v_pos

        if not vertical_length:
            vertical_length = 1
        
        self.vscroll_layout.addWidget(widget, vertical_start, horizontal_start, vertical_length, horizontal_length)

        self.grid_v_pos += vertical_length + vertical_start - self.grid_v_pos

    def change_visibility(self):
        changing_widgets = [self.vacation_label, self.vacation_checkbox,
                            self.comment_label,  self.comment_textbox,
                            self.wage_label, self.wage_textbox,
                            self.creation_date_label, self.creation_date_text,
                            self.modification_date_label, self.modification_date_text,
                            self.author_label, self.author_text]

        if self.fold_button.arrowType() == QtCore.Qt.RightArrow:
            print("Debug: Open advanced entry settings.")
            self.fold_button.setArrowType(QtCore.Qt.DownArrow)
            for widget in changing_widgets: widget.show()

        elif self.fold_button.arrowType() == QtCore.Qt.DownArrow:
            print("Debug: Close advanced entry settings.")
            self.fold_button.setArrowType(QtCore.Qt.RightArrow)
            for widget in changing_widgets: widget.hide()

class MonthOverview(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        months = ["Januar 2020","Februar 2020","März 2020","April 2020",
                    "Mai 2020","Juni 2020","Juli 2020","August 2020",
                    "September 2020","Oktober 2020","November 2020",
                    "Dezember 2020"]

        widget_content = QtWidgets.QVBoxLayout()

        size_policy = QtWidgets.QSizePolicy()
        # size_policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Minimum)

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


        widget_line = QtWidgets.QFrame()
        widget_line.setFrameShape(QtWidgets.QFrame.VLine)
        widget_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        widget_layout = QtWidgets.QHBoxLayout()

        widget_layout.addWidget(scroll_area)
        widget_layout.addWidget(widget_line)

        self.setLayout(widget_layout)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        edit_entry_widget = EditEntry()
        edit_entry_widget.setMinimumWidth(400)
        edit_entry_widget.setMaximumWidth(450)

        month_overview_widget = MonthOverview()
        month_overview_widget.setMinimumWidth(150)
        month_overview_widget.setMaximumWidth(250)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(month_overview_widget)
        layout.addWidget(QtWidgets.QPushButton())#, stretch=8)
        layout.addWidget(edit_entry_widget)#, stretch=3)


        window_content = QtWidgets.QWidget()
        window_content.setLayout(layout)
        self.setCentralWidget(window_content)
        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec_())
    
