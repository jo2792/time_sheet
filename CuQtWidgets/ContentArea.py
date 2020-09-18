from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

class EntryOverview(QtWidgets.QGraphicsView):
    def __init__(self, data):
        super().__init__()
        width = 1150
        height = 850
        self.setMinimumSize(width,height)
        self.setMaximumSize(width, height)

        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        

        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Maximum)

        scene = QtWidgets.QGraphicsScene(0,0,1130,680)
        
        self.setFrameStyle(QtWidgets.QFrame.NoFrame)

        scene.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(240,240,240), QtCore.Qt.BrushStyle.SolidPattern))
        
        strong_pen = QtGui.QPen("black")
        strong_pen.setWidthF(4)

        default_pen = QtGui.QPen("black")
        default_pen.setWidthF(2)

        padding_top = 10

        # Draw Head
        scene.addLine(828,25+padding_top,828,125+padding_top, default_pen)
        scene.addLine(555,75+padding_top,1101,75+padding_top, default_pen)

        self.month_title_text = scene.addText("August 2020")
        self.month_title_text.setPos(70,10+padding_top)
        self.month_title_text.setFont(QtGui.QFont('SansSerif', pointSize=50))

        sum_hours_text = scene.addText("∑ Arbeitsstunden")
        sum_hours_text.setPos(570,30+padding_top)
        sum_hours_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        sum_earnings_text = scene.addText("∑ Verdienst")
        sum_earnings_text.setPos(880,30+padding_top)
        sum_earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        self.sum_hours_value_text = scene.addText("16 Stunden")
        self.sum_hours_value_text.setPos(595,80+padding_top)
        self.sum_hours_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        self.sum_earnings_value_text = scene.addText("160 €")
        self.sum_earnings_value_text.setPos(932,80+padding_top)
        self.sum_earnings_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # Draw Body Headline
        scene.addLine(10,160+padding_top,1120,160+padding_top, strong_pen)
        scene.addLine(10,195+padding_top, 1120, 195+padding_top, strong_pen)
        scene.addLine(10,160+padding_top,10,195+padding_top, strong_pen)
        scene.addLine(1120,160+padding_top,1120,195+padding_top, strong_pen)
        scene.addLine(828,160+padding_top,828,195+padding_top, strong_pen)
        scene.addLine(535,160+padding_top,535,195+padding_top, strong_pen)

        date_text = scene.addText("Datum")
        date_text.setPos(self.center_text(date_text,10,535),160+padding_top)
        date_text.setFont(QtGui.QFont('SansSerif',pointSize=19))

        work_hours = scene.addText("Arbeitsstunden")
        work_hours.setPos(self.center_text(work_hours,535,828),160+padding_top)
        work_hours.setFont(QtGui.QFont('SansSerif', pointSize=19))

        earnings_text = scene.addText("Verdienst")
        earnings_text.setPos(self.center_text(earnings_text,828,1120),160+padding_top)
        earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=19))

        # Draw Body

        vertical_line_pos = 195+padding_top
        text_centering_margin = 3
        for index, row in data.df.iterrows():
            entry_date_text = scene.addText(self.format_date(row['Work Date']))
            entry_date_text.setPos(self.center_text(entry_date_text,10,535),vertical_line_pos+text_centering_margin)
            entry_date_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

            duration = self.get_duration(row['Start Time'], row['End Time'])
            entry_hours_text = scene.addText(self.format_duration(duration))
            entry_hours_text.setPos(self.center_text(entry_hours_text,535,828)-15,vertical_line_pos+text_centering_margin)
            entry_hours_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

            entry_earnings_text = scene.addText(self.format_earnings(duration,row['Hourly Wage']))
            entry_earnings_text.setPos(self.center_text(entry_earnings_text,828,1120),vertical_line_pos+text_centering_margin)
            entry_earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=23))
            
            vertical_line_pos += 45
            scene.addLine(10,vertical_line_pos,1120,vertical_line_pos, default_pen)

            

        scene.addLine(9,190+padding_top,9,vertical_line_pos, default_pen) #1 Line
        scene.addLine(535,190+padding_top,535,vertical_line_pos, default_pen) #2 Line
        scene.addLine(828,190+padding_top,828,vertical_line_pos, default_pen) #3 Line
        scene.addLine(1121,190+padding_top,1121,vertical_line_pos, default_pen) #4 Line


        # Draw Overtime
        # scene.addLine(210,500,828,500, default_pen)
        # scene.addLine(210,555,828,555, default_pen)
        # scene.addLine(210,610,828,610, default_pen)
        # scene.addLine(210,665,828,665, default_pen)

        # scene.addLine(210,500,210,665, default_pen)
        # scene.addLine(535,500,535,665, default_pen)
        # scene.addLine(828,500,828,665, default_pen)


        # overtime_text = scene.addText("Überstunden")
        # overtime_text.setPos(175,660)
        # overtime_text.setRotation(-90)
        # overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=19))

        # pre_overtime_text = scene.addText("Vormonat (Juli)")
        # pre_overtime_text.setPos(250,505)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_text = scene.addText("Neu")
        # pre_overtime_text.setPos(320,560)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_text = scene.addText("Gesamt")
        # pre_overtime_text.setPos(290,615)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_value_text = scene.addText("50 Stunden")
        # pre_overtime_value_text.setPos(600,505)
        # pre_overtime_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_text = scene.addText("6 Stunden")
        # pre_overtime_text.setPos(617,560)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_text = scene.addText("56 Stunden")
        # pre_overtime_text.setPos(600,615)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        padding_bottom = 40
        scene.setSceneRect(0,0,1130,vertical_line_pos+padding_bottom)

        self.setScene(scene)

    def format_date(self, date):
        date = QtCore.QDate.fromString(date, 'yyyy-MM-dd')

        return date.toString('ddd. dd.MM.yyyy')

    def get_duration(self, start_time, end_time):
        start_time = QtCore.QTime.fromString(start_time)
        end_time = QtCore.QTime.fromString(end_time)

        duration = start_time.secsTo(end_time)/3600

        return duration

    def format_duration(self, duration):
        if duration.is_integer():
            return "{:2.0f} Stunden".format(duration)
        else:
            return "{:2.1f} Stunden".format(duration)

    def format_earnings(self, duration, wage):
        return "{:3.2f} €".format(duration*wage)

    def center_text(self,text_obj, left_border, right_border):
        text_width = text_obj.boundingRect().width()
        range = right_border - left_border
        
        start_position = ((range - (2*text_width)) / 2 ) + left_border
        return start_position



class ContentArea(QtWidgets.QWidget):

    addClicked = QtCore.Signal(bool)
    button_state = 1
 
    def __init__(self, data):
        super().__init__()

        widget_layout = QtWidgets.QVBoxLayout()

        entry_overview_widget = EntryOverview(data)
        
        widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        widget_layout.addSpacing(30)
        widget_layout.addWidget(entry_overview_widget)
        widget_layout.addSpacing(200)

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
            self.addClicked.emit(True)

    def switch_button_state(self):
        self.button_state += 1
        self.button_state = self.button_state % 2

        print("Button State: " + str(self.button_state))      