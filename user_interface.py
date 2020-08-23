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
        date_textbox = set_default_field_style(QtWidgets.QLineEdit())
        
        # Work start time
        start_time_label = set_default_label_style(QtWidgets.QLabel("Beginn:"))
        start_time_textbox = set_default_field_style(QtWidgets.QLineEdit())
        
        # Work end time
        end_time_label = set_default_label_style(QtWidgets.QLabel("Ende:"))
        end_time_textbox = set_default_field_style(QtWidgets.QLineEdit())

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
        self.wage_textbox = set_default_field_style(QtWidgets.QLineEdit("10,00 €"))
        
        # creation date
        self.creation_date_label = set_default_label_style(QtWidgets.QLabel("Erstelldatum:"))
        self.creation_date_text = set_default_field_style(QtWidgets.QLineEdit("18.08.2020"))
        self.creation_date_text.setReadOnly(True)

        # modification date
        self.modification_date_label = set_default_label_style(QtWidgets.QLabel("Änderungsdatum:"))
        self.modification_date_text = set_default_field_style(QtWidgets.QLineEdit("19.08.2020"))
        self.modification_date_text.setReadOnly(True)

        # author
        self.author_label = set_default_label_style(QtWidgets.QLabel("Autor:"))
        self.author_text = set_default_field_style(QtWidgets.QLineEdit("Jordan"))
        self.author_text.setReadOnly(True)

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
        label_h_begin = 0
        label_h_length = 2

        textbox_h_begin = 2
        textbox_h_length = 1

        self.vscroll_layout.addWidget(headline_label,0,0,1,3)
        self.vscroll_layout.addWidget(date_label,1,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(date_textbox,2,textbox_h_begin,1,textbox_h_length)
        self.vscroll_layout.addWidget(start_time_label,3,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(start_time_textbox,4,textbox_h_begin,1,textbox_h_length)
        self.vscroll_layout.addWidget(end_time_label,5,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(end_time_textbox,6,textbox_h_begin,1,textbox_h_length)
        
        self.vscroll_layout.addWidget(self.fold_button,7,0,1,1)
        self.vscroll_layout.addWidget(self.fold_line,7,1,1,2)
        
        self.vscroll_layout.addWidget(self.vacation_label,8,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(self.vacation_checkbox,8,2,1,1)
        self.vscroll_layout.addWidget(self.comment_label,9,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(self.comment_textbox,10,0,2,3)
        self.vscroll_layout.addWidget(self.wage_label,12,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(self.wage_textbox,13,textbox_h_begin,1,textbox_h_length)
        self.vscroll_layout.addWidget(self.creation_date_label,14,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(self.creation_date_text,15,textbox_h_begin,1,textbox_h_length)
        self.vscroll_layout.addWidget(self.modification_date_label,16,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(self.modification_date_text,17,textbox_h_begin,1,textbox_h_length)        
        self.vscroll_layout.addWidget(self.author_label,18,label_h_begin,1,label_h_length)
        self.vscroll_layout.addWidget(self.author_text,19,textbox_h_begin,1,textbox_h_length)  

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
        


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        edit_entry_widget = EditEntry()
        edit_entry_widget.setMinimumWidth(400)
        edit_entry_widget.setMaximumWidth(450)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QPushButton())#, stretch=8)
        layout.addWidget(edit_entry_widget)#, stretch=3)


        window_content = QtWidgets.QWidget()
        window_content.setLayout(layout)
        self.setCentralWidget(window_content)
        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
    
