""" Module to build the grafic interface to interact with the user """
__authors__ = "Jordan Alwon"
__copyright__ = "Copyright 2020"

import sys
from PySide2 import QtWidgets, QtCore, QtGui
from CuQtWidgets.EditEntry import EditEntry
        
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

class EntryOverview(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        width = 1150
        height = 700
        # self.setMinimumSize(width,height)
        # self.setMaximumSize(width, height)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)

        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Minimum)

        scene = QtWidgets.QGraphicsScene(0,0,1130,680)
        self.setFrameStyle(QtWidgets.QFrame.NoFrame)

        scene.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(240,240,240), QtCore.Qt.BrushStyle.SolidPattern))
        
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

    addClicked = QtCore.Signal()
    button_state = 1

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

        add_button = QtWidgets.QPushButton()
        add_button.setStyleSheet("""QPushButton {
                                    background-color: transparent;
                                    border-image: url(resources/button_icons/Add.png);
                                    background: none;
                                    background-repeat:none;
                                    } """)
        add_button.setFixedSize(75,75)
        button_layout.addWidget(add_button)

        overtime_button = QtWidgets.QPushButton()
        overtime_button.setStyleSheet("""QPushButton {
                                    background-color: transparent;
                                    border-image: url(resources/button_icons/Overtime.png);
                                    background: none;
                                    background-repeat:none;
                                    } """)
        overtime_button.setFixedSize(75,75)
        button_layout.addWidget(overtime_button)

        close_month_button = QtWidgets.QPushButton()
        close_month_button.setStyleSheet("""QPushButton {
                                    background-color: transparent;
                                    border-image: url(resources/button_icons/Lock.png);
                                    background: none;
                                    background-repeat:none;
                                    } """)
        close_month_button.setFixedSize(75,75)
        button_layout.addWidget(close_month_button)

        export_button = QtWidgets.QPushButton()
        export_button.setStyleSheet("""QPushButton {
                                    background-color: transparent;
                                    border-image: url(resources/button_icons/Export.png);
                                    background: none;
                                    background-repeat:none;
                                    } """)
        export_button.setFixedSize(75,75)
        button_layout.addWidget(export_button)

        options_button = QtWidgets.QPushButton()
        options_button.setStyleSheet("""QPushButton {
                                    background-color: transparent;
                                    border-image: url(resources/button_icons/Options.png);
                                    background: none;
                                    background-repeat:none;
                                    } """)
        options_button.setFixedSize(75,75)
        # options_button.clicked.connect(self.Testfunc)


        button_layout.addWidget(options_button)

        button_layout.addSpacing(200)

        widget_layout.addLayout(button_layout)

        self.setLayout(widget_layout)

        add_button.clicked.connect(self.add_test)

    def add_test(self):
        if self.button_state:
            self.addClicked.emit()

    def switch_button_state(self):
        self.button_state += 1
        self.button_state = self.button_state % 2

        print("Button State: " + str(self.button_state))      

class MainWindow(QtWidgets.QMainWindow):
    entry_widget_is_shown = False
    edit_entry_widget = None

    def __init__(self):
        super().__init__()

        self.month_overview_widget = MonthOverview()

        screen_size= self.screen().size().height()
        self.content_area = ContentArea()
        self.content_area.setMaximumHeight(999)

        self.content_area.addClicked.connect(self.change_entry_widget_visibility)
        

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.month_overview_widget)
        self.layout.addWidget(self.content_area, stretch= 8)

        self.month_overview_widget.setMaximumWidth(230)
        self.month_overview_widget.setMinimumWidth(230)

        window_content = QtWidgets.QWidget()
        window_content.setLayout(self.layout)
        self.setCentralWidget(window_content)

    def change_entry_widget_visibility(self):
        self.content_area.switch_button_state()
        if self.entry_widget_is_shown:
            self.entry_widget_is_shown= False
            self.layout.removeWidget(self.edit_entry_widget)
            self.edit_entry_widget.remove_widget()
        else:
            self.entry_widget_is_shown = True
            self.edit_entry_widget = EditEntry()
            self.layout.addWidget(self.edit_entry_widget, stretch= 3)
            self.edit_entry_widget.accept_signal.connect(self.change_entry_widget_visibility)            
        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec_())
    
