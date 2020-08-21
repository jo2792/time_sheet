""" Module to build the grafic interface to interact with the user """
__authors__ = "Jordan Alwon"
__copyright__ = "Copyright 2020"

import sys
from PySide2 import QtWidgets, QtCore, QtGui

class EditEntry(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(350)

        sp_retain = QtWidgets.QSizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)

        # Define wideget elements
        headline_label = QtWidgets.QLabel("Eintrag bearbeiten")
        headline_label.setAlignment(QtCore.Qt.AlignLeft)
        headline_label.setFont(QtGui.QFont('SansSerif',pointSize=20))
        headline_label.setSizePolicy(sp_retain)
        # headline_label.setStyleSheet("QWidget { font: 25px}")

        # Work Date
        date_label = QtWidgets.QLabel("Datum:")
        date_label.setAlignment(QtCore.Qt.AlignLeft)
        date_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        date_label.setSizePolicy(sp_retain)

        date_textbox = QtWidgets.QLineEdit()
        # date_textbox.setMaximumWidth()
        date_textbox.setAlignment(QtCore.Qt.AlignCenter)
        date_textbox.setFont(QtGui.QFont('SansSerif',pointSize=16))
        date_textbox.setContentsMargins(QtCore.QMargins(150,0,10,0))
        date_textbox.setSizePolicy(sp_retain)
        

        # Work start time
        start_time_label = QtWidgets.QLabel("Beginn:")
        start_time_label.setAlignment(QtCore.Qt.AlignLeft)
        start_time_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        start_time_label.setSizePolicy(sp_retain)

        start_time_textbox = QtWidgets.QLineEdit()
        start_time_textbox.setAlignment(QtCore.Qt.AlignCenter)
        start_time_textbox.setFont(QtGui.QFont('SansSerif',pointSize=16))
        start_time_textbox.setContentsMargins(QtCore.QMargins(150,0,10,0))
        start_time_textbox.setSizePolicy(sp_retain)

        # Work end time
        end_time_label = QtWidgets.QLabel("Ende:")
        end_time_label.setAlignment(QtCore.Qt.AlignLeft)
        end_time_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        end_time_label.setSizePolicy(sp_retain)

        end_time_textbox = QtWidgets.QLineEdit()
        end_time_textbox.setAlignment(QtCore.Qt.AlignCenter)
        end_time_textbox.setFont(QtGui.QFont('SansSerif',pointSize=16))
        end_time_textbox.setContentsMargins(QtCore.QMargins(150,0,10,0))
        end_time_textbox.setSizePolicy(sp_retain)

        

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

        #Scroll Area
        self.vscroll_layout = QtWidgets.QGridLayout()

        # self.vscroll_layout.setAlignment(QtCore.Qt.AlignRight)

              
        scroll_area_content = QtWidgets.QWidget()
        scroll_area_content.setLayout(self.vscroll_layout)
        scroll_area = QtWidgets.QScrollArea()

        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_area_content)
        scroll_area.setStyleSheet("QScrollArea { background-color: white; border: none; }")

        self.vscroll_layout.addWidget(headline_label,0,0,1,7)
        self.vscroll_layout.addWidget(date_label,1,0,1,5)
        self.vscroll_layout.addWidget(date_textbox,2,2,1,3)
        self.vscroll_layout.addWidget(start_time_label,3,0,1,5)
        self.vscroll_layout.addWidget(start_time_textbox,4,2,1,3)
        self.vscroll_layout.addWidget(end_time_label,5,0,1,5)
        self.vscroll_layout.addWidget(end_time_textbox,6,2,1,3)
        
        # self.vscroll_layout.setSpacing(0)
        # self.vscroll_layout.setMargin(0)
        # self.vscroll_layout.setContentsMargins(0,0,0,0)

       

        # Spoiler
        self.fold_button = QtWidgets.QToolButton()
        self.fold_button.setStyleSheet("QToolButton { border: none; }")
        self.fold_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.fold_button.setArrowType(QtCore.Qt.RightArrow)
        self.fold_button.setText("Erweitert")
        self.fold_button.setCheckable(True)
        self.fold_button.setChecked(False)

        self.fold_line = QtWidgets.QFrame()
        self.fold_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.fold_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Vacation
          
        self.vacation_label = QtWidgets.QLabel("Urlaub:")
        self.vacation_label.setAlignment(QtCore.Qt.AlignLeft)
        self.vacation_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.vacation_label.setSizePolicy(sp_retain)

        self.vacation_checkbox = QtWidgets.QCheckBox()
        self.vacation_checkbox.setSizePolicy(sp_retain)
        
        # Comment
        self.comment_label = QtWidgets.QLabel("Kommentar:")
        self.comment_label.setAlignment(QtCore.Qt.AlignLeft)
        self.comment_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.comment_label.setSizePolicy(sp_retain)

        self.comment_textbox = QtWidgets.QTextEdit()
        self.comment_textbox.setAlignment(QtCore.Qt.AlignLeft)
        self.comment_textbox.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.comment_textbox.setSizePolicy(sp_retain)

        # wage
        self.wage_label = QtWidgets.QLabel("Stundenlohn:")
        self.wage_label.setAlignment(QtCore.Qt.AlignLeft)
        self.wage_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.wage_label.setSizePolicy(sp_retain)

        self.wage_textbox = QtWidgets.QLineEdit("10,00 €")
        self.wage_textbox.setAlignment(QtCore.Qt.AlignCenter)
        self.wage_textbox.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.wage_textbox.setSizePolicy(sp_retain)
        
        # creation date
        self.creation_date_label = QtWidgets.QLabel("Erstelldatum:")
        self.creation_date_label.setAlignment(QtCore.Qt.AlignLeft)
        self.creation_date_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.creation_date_label.setSizePolicy(sp_retain)

        self.creation_date_text = QtWidgets.QLineEdit("18.08.2020")
        self.creation_date_text.setAlignment(QtCore.Qt.AlignCenter)
        self.creation_date_text.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.creation_date_text.setReadOnly(True)
        self.creation_date_text.setSizePolicy(sp_retain)

        # modification date
        self.modification_date_label = QtWidgets.QLabel("Änderungsdatum:")
        self.modification_date_label.setAlignment(QtCore.Qt.AlignLeft)
        self.modification_date_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.modification_date_label.setSizePolicy(sp_retain)

        self.modification_date_text = QtWidgets.QLineEdit("19.08.2020")
        self.modification_date_text.setAlignment(QtCore.Qt.AlignCenter)
        self.modification_date_text.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.modification_date_text.setReadOnly(True)
        self.modification_date_text.setSizePolicy(sp_retain)

        # author
        self.author_label = QtWidgets.QLabel("Autor:")
        self.author_label.setAlignment(QtCore.Qt.AlignLeft)
        self.author_label.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.author_label.setSizePolicy(sp_retain)

        self.author_text = QtWidgets.QLineEdit("Jordan")
        self.author_text.setAlignment(QtCore.Qt.AlignCenter)
        self.author_text.setFont(QtGui.QFont('SansSerif',pointSize=16))
        self.author_text.setReadOnly(True)
        self.author_text.setSizePolicy(sp_retain)
        
        self.vscroll_layout.addWidget(self.fold_button,7,0,1,1)
        self.vscroll_layout.addWidget(self.fold_line,7,1,1,4)
        
        self.vscroll_layout.addWidget(self.vacation_label,8,0,1,3)
        self.vscroll_layout.addWidget(self.vacation_checkbox,8,4,1,1)
        self.vscroll_layout.addWidget(self.comment_label,9,0,1,5)
        self.vscroll_layout.addWidget(self.comment_textbox,10,0,2,5)
        self.vscroll_layout.addWidget(self.wage_label,12,0,1,5)
        self.vscroll_layout.addWidget(self.wage_textbox,13,2,1,3)
        self.vscroll_layout.addWidget(self.creation_date_label,14,0,1,5)
        self.vscroll_layout.addWidget(self.creation_date_text,15,2,1,3)
        self.vscroll_layout.addWidget(self.modification_date_label,16,0,1,5)
        self.vscroll_layout.addWidget(self.modification_date_text,17,2,1,3)        
        self.vscroll_layout.addWidget(self.author_label,18,0,1,5)
        self.vscroll_layout.addWidget(self.author_text,19,2,1,3)  

        # self.bottom_space = QtWidgets.QSpacerItem(0,1)
        # self.vscroll_layout.addItem(self.bottom_space)
        
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

        self.space = QtWidgets.QSpacerItem(0,0)

        widget_content = QtWidgets.QVBoxLayout()
        widget_content.addWidget(scroll_area)
        # widget_content.addSpacerItem(self.space)
        widget_content.addWidget(button_line)
        widget_content.addLayout(button_layout)

        widget_layout = QtWidgets.QHBoxLayout()
        widget_layout.addWidget(widget_line)
        widget_layout.addLayout(widget_content)

        self.setLayout(widget_layout)

        self.fold_button.clicked.connect(self.hide)


    def hide(self):
        print("Test")

        if self.fold_button.arrowType() == QtCore.Qt.RightArrow:
            self.fold_button.setArrowType(QtCore.Qt.DownArrow)

            print("Test2")
    
            self.vacation_label.show()
            self.vacation_checkbox.show()
            self.comment_label.show()
            self.comment_textbox.show()
            self.wage_label.show()
            self.wage_textbox.show()
            self.creation_date_label.show()
            self.creation_date_text.show()
            self.modification_date_label.show()
            self.modification_date_text.show()
            self.author_label.show()
            self.author_text.show()

        elif self.fold_button.arrowType() == QtCore.Qt.DownArrow:
            # self.space.changeSize(10,700)
            self.fold_button.setArrowType(QtCore.Qt.RightArrow)
            print("Test3")
            self.vacation_label.hide()
            self.vacation_checkbox.hide()
            self.comment_label.hide()
            self.comment_textbox.hide()
            self.wage_label.hide()
            self.wage_textbox.hide()
            self.creation_date_label.hide()
            self.creation_date_text.hide()
            self.modification_date_label.hide()
            self.modification_date_text.hide()
            self.author_label.hide()
            self.author_text.hide()
        



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        edit_entry_widget = EditEntry()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(QtWidgets.QPushButton(), stretch=3)
        layout.addWidget(edit_entry_widget, stretch=1)


        window_content = QtWidgets.QWidget()
        window_content.setLayout(layout)
        self.setCentralWidget(window_content)
        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
    
