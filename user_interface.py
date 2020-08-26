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

class EntryOverview(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        width = 1150
        height = 700
        self.setMinimumSize(width,height)
        self.setMaximumSize(width, height)
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)

        scene = QtWidgets.QGraphicsScene(0,0,1130,680)
        self.setFrameStyle(QtWidgets.QFrame.NoFrame)

        scene.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(240,240,240), QtCore.Qt.BrushStyle.SolidPattern))
        # self.setAlignment(QtCore.Qt.AlignHCenter)
        
        strong_pen = QtGui.QPen("black")
        strong_pen.setWidthF(4)

        default_pen = QtGui.QPen("black")
        default_pen.setWidthF(2)

        scene.addLine(10,200,1120,200, strong_pen)
        scene.addLine(10,235 , 1120, 235, strong_pen)
        scene.addLine(10,200,10,235, strong_pen)
        scene.addLine(1120,200,1120,235, strong_pen)
        scene.addLine(828,200,828,235, strong_pen)
        scene.addLine(535,200,535,235, strong_pen)

        scene.addLine(9,235,9,415, default_pen)
        scene.addLine(535,230,535,415, default_pen)
        scene.addLine(828,230,828,415, default_pen)
        scene.addLine(1121,230,1121,415, default_pen)

        scene.addLine(10,280,1120,280, default_pen)
        scene.addLine(10,325,1120,325, default_pen)
        scene.addLine(10,370,1120,370, default_pen)
        scene.addLine(10,415,1120,415, default_pen)


        scene.addLine(828,65,828,165, default_pen)
        scene.addLine(555,115,1101,115, default_pen)
        
    

        date_text = scene.addText("Datum")
        date_text.setPos(230,200)
        date_text.setFont(QtGui.QFont('SansSerif',pointSize=19))
        # print(date_text.boundingRect().size())

        work_hours = scene.addText("Arbeitsstunden")
        work_hours.setPos(590,200)
        work_hours.setFont(QtGui.QFont('SansSerif', pointSize=19))

        earnings_text = scene.addText("Verdienst")
        earnings_text.setPos(915,200)
        earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=19))

        entry_date_text = scene.addText("Di. 04.08.2020")
        entry_date_text.setPos(170,238)
        entry_date_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        entry_hours_text = scene.addText("6 Stunden")
        entry_hours_text.setPos(610,238)
        entry_hours_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        entry_earnings_text = scene.addText("60 €")
        entry_earnings_text.setPos(950,238)
        entry_earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        entry2_date_text = scene.addText("Do. 06.08.2020")
        entry2_date_text.setPos(162,283)
        entry2_date_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        entry2_hours_text = scene.addText("10 Stunden")
        entry2_hours_text.setPos(595,283)
        entry2_hours_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        entry2_earnings_text = scene.addText("100 €")
        entry2_earnings_text.setPos(935,283)
        entry2_earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=23))


        month_title_text = scene.addText("August 2020")
        month_title_text.setPos(70,50)
        month_title_text.setFont(QtGui.QFont('SansSerif', pointSize=50))

        sum_hours_text = scene.addText("∑ Arbeitsstunden")
        sum_hours_text.setPos(570,70)
        sum_hours_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        sum_earnings_text = scene.addText("∑ Verdienst")
        sum_earnings_text.setPos(880,70)
        sum_earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        sum_hours_value_text = scene.addText("16 Stunden")
        sum_hours_value_text.setPos(595,120)
        sum_hours_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        sum_earnings_value_text = scene.addText("160 €")
        sum_earnings_value_text.setPos(932,120)
        sum_earnings_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))


        scene.addLine(210,500,828,500, default_pen)
        scene.addLine(210,555,828,555, default_pen)
        scene.addLine(210,610,828,610, default_pen)
        scene.addLine(210,665,828,665, default_pen)

        scene.addLine(210,500,210,665, default_pen)
        scene.addLine(535,500,535,665, default_pen)
        scene.addLine(828,500,828,665, default_pen)


        overtime_text = scene.addText("Überstunden")
        overtime_text.setPos(175,660)
        overtime_text.setRotation(-90)
        overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=19))

        pre_overtime_text = scene.addText("Vormonat (Juli)")
        pre_overtime_text.setPos(250,505)
        pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        pre_overtime_text = scene.addText("Neu")
        pre_overtime_text.setPos(320,560)
        pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        pre_overtime_text = scene.addText("Gesamt")
        pre_overtime_text.setPos(290,615)
        pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        pre_overtime_value_text = scene.addText("50 Stunden")
        pre_overtime_value_text.setPos(600,505)
        pre_overtime_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        pre_overtime_text = scene.addText("6 Stunden")
        pre_overtime_text.setPos(617,560)
        pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        pre_overtime_text = scene.addText("56 Stunden")
        pre_overtime_text.setPos(600,615)
        pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        self.setScene(scene)


class ContentArea(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        widget_layout = QtWidgets.QVBoxLayout()

        entry_overview_widget = EntryOverview()
        
        widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        widget_layout.addWidget(entry_overview_widget)
        widget_layout.addSpacing(800)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addSpacing(200)
        button_layout.setSpacing(30)

        add_button = QtWidgets.QPushButton("Add")
        add_button.setFont(QtGui.QFont('SansSerif', pointSize=16))
        add_button.setFixedHeight(40)
        add_button.setFixedWidth(100)
        button_layout.addWidget(add_button)

        overtime_button = QtWidgets.QPushButton("OT")
        overtime_button.setFont(QtGui.QFont('SansSerif', pointSize=16))
        overtime_button.setFixedHeight(40)
        overtime_button.setFixedWidth(100)
        button_layout.addWidget(overtime_button)

        close_month_button = QtWidgets.QPushButton("Abschließen")
        close_month_button.setFont(QtGui.QFont('SansSerif', pointSize=16))
        close_month_button.setFixedHeight(40)
        close_month_button.setFixedWidth(100)
        button_layout.addWidget(close_month_button)

        export_button = QtWidgets.QPushButton("Export")
        export_button.setFont(QtGui.QFont('SansSerif', pointSize=16))
        export_button.setFixedHeight(40)
        export_button.setFixedWidth(100)
        button_layout.addWidget(export_button)

        options_button = QtWidgets.QPushButton("Optiones")
        options_button.setFont(QtGui.QFont('SansSerif', pointSize=16))
        options_button.setFixedHeight(40)
        options_button.setFixedWidth(100)
        button_layout.addWidget(options_button)

        button_layout.addSpacing(200)

        widget_layout.addLayout(button_layout)

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

        content_area = ContentArea()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(month_overview_widget)
        layout.addWidget(content_area)
        layout.addWidget(edit_entry_widget)#, stretch=3)


        window_content = QtWidgets.QWidget()
        window_content.setLayout(layout)
        self.setCentralWidget(window_content)
        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec_())
    
