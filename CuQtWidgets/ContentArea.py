from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

class EntryOverview(QtWidgets.QGraphicsView):
    editClicked = QtCore.Signal(list)

    def __init__(self, data):
        super().__init__()
        width = 1150
        height = 850
        self.setMinimumSize(width,height)
        self.setMaximumSize(width, height)

        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        

        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Maximum)

        self.scene = QtWidgets.QGraphicsScene(0,0,1130,680)
        
        self.setFrameStyle(QtWidgets.QFrame.NoFrame)

        self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(240,240,240), QtCore.Qt.BrushStyle.SolidPattern))
        
        strong_pen = QtGui.QPen("black")
        strong_pen.setWidthF(4)

        self.default_pen = QtGui.QPen("black")
        self.default_pen.setWidthF(2)

        self.padding_top = 10

        # Draw Body Headline
        self.scene.addLine(10,160+self.padding_top,1120,160+self.padding_top, strong_pen)
        self.scene.addLine(10,195+self.padding_top, 1120, 195+self.padding_top, strong_pen)
        self.scene.addLine(10,160+self.padding_top,10,195+self.padding_top, strong_pen)
        self.scene.addLine(1120,160+self.padding_top,1120,195+self.padding_top, strong_pen)
        self.scene.addLine(828,160+self.padding_top,828,195+self.padding_top, strong_pen)
        self.scene.addLine(535,160+self.padding_top,535,195+self.padding_top, strong_pen)

        date_text = self.scene.addText("Datum")
        date_text.setPos(self.center_text(date_text,10,535),160+self.padding_top)
        date_text.setFont(QtGui.QFont('SansSerif',pointSize=19))

        work_hours = self.scene.addText("Arbeitsstunden")
        work_hours.setPos(self.center_text(work_hours,535,828),160+self.padding_top)
        work_hours.setFont(QtGui.QFont('SansSerif', pointSize=19))

        earnings_text = self.scene.addText("Verdienst")
        earnings_text.setPos(self.center_text(earnings_text,828,1120),160+self.padding_top)
        earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=19))

        

        # Draw Head
        self.scene.addLine(828,25+self.padding_top,828,125+self.padding_top, self.default_pen)
        self.scene.addLine(555,75+self.padding_top,1101,75+self.padding_top, self.default_pen)

        self.month_title_text = self.scene.addText("August 2020")
        self.month_title_text.setPos(70,10+self.padding_top)
        self.month_title_text.setFont(QtGui.QFont('SansSerif', pointSize=50))

        sum_hours_text = self.scene.addText("∑ Arbeitsstunden")
        sum_hours_text.setPos(570,30+self.padding_top)
        sum_hours_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        sum_earnings_text = self.scene.addText("∑ Verdienst")
        sum_earnings_text.setPos(880,30+self.padding_top)
        sum_earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        self.draw_from_data(data)

        # Draw Overtime
        # self.scene.addLine(210,500,828,500, self.default_pen)
        # self.scene.addLine(210,555,828,555, self.default_pen)
        # self.scene.addLine(210,610,828,610, self.default_pen)
        # self.scene.addLine(210,665,828,665, self.default_pen)

        # self.scene.addLine(210,500,210,665, self.default_pen)
        # self.scene.addLine(535,500,535,665, self.default_pen)
        # self.scene.addLine(828,500,828,665, self.default_pen)


        # overtime_text = self.scene.addText("Überstunden")
        # overtime_text.setPos(175,660)
        # overtime_text.setRotation(-90)
        # overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=19))

        # pre_overtime_text = self.scene.addText("Vormonat (Juli)")
        # pre_overtime_text.setPos(250,505)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_text = self.scene.addText("Neu")
        # pre_overtime_text.setPos(320,560)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_text = self.scene.addText("Gesamt")
        # pre_overtime_text.setPos(290,615)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_value_text = self.scene.addText("50 Stunden")
        # pre_overtime_value_text.setPos(600,505)
        # pre_overtime_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_text = self.scene.addText("6 Stunden")
        # pre_overtime_text.setPos(617,560)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        # pre_overtime_text = self.scene.addText("56 Stunden")
        # pre_overtime_text.setPos(600,615)
        # pre_overtime_text.setFont(QtGui.QFont('SansSerif', pointSize=23))

        
        self.setScene(self.scene)

    def draw_from_data(self, data):
        # Draw Body

        self.vertical_line_pos = 195+self.padding_top
        text_centering_margin = 3
        sum_duration = 0
        sum_earnings = 0

        self.l = []
        self.removable_objects = []
        for index, row in data.df.iterrows():
            entry_date_text = self.scene.addText(self.format_date(row['Work Date']))
            entry_date_text.setPos(self.center_text(entry_date_text,10,535),self.vertical_line_pos+text_centering_margin)
            entry_date_text.setFont(QtGui.QFont('SansSerif', pointSize=23))
            self.removable_objects.append(entry_date_text)

            duration = self.get_duration(row['Start Time'], row['End Time'])
            entry_hours_text = self.scene.addText(self.format_duration(duration))
            entry_hours_text.setPos(self.center_text(entry_hours_text,535,828)-15,self.vertical_line_pos+text_centering_margin)
            entry_hours_text.setFont(QtGui.QFont('SansSerif', pointSize=23))
            self.removable_objects.append(entry_hours_text)
            sum_duration += duration

            earning = duration*row['Hourly Wage']
            entry_earnings_text = self.scene.addText(self.format_earnings(earning))
            entry_earnings_text.setPos(self.center_text(entry_earnings_text,828,1120),self.vertical_line_pos+text_centering_margin)
            entry_earnings_text.setFont(QtGui.QFont('SansSerif', pointSize=23))
            self.removable_objects.append(entry_earnings_text)
            sum_earnings += earning
            
            click_area = self.scene.addRect(10,self.vertical_line_pos,1110,45)
            self.removable_objects.append(click_area)

            self.l.append({'Object': click_area, 'Row_Nr': index, 'Data': row})

            self.vertical_line_pos += 45
            line = self.scene.addLine(10,self.vertical_line_pos,1120,self.vertical_line_pos, self.default_pen)
            self.removable_objects.append(line)

        line_1 = self.scene.addLine(9,190+self.padding_top,9,self.vertical_line_pos, self.default_pen) #1 Line
        line_2 = self.scene.addLine(535,190+self.padding_top,535,self.vertical_line_pos, self.default_pen) #2 Line
        line_3 = self.scene.addLine(828,190+self.padding_top,828,self.vertical_line_pos, self.default_pen) #3 Line
        line_4 = self.scene.addLine(1121,190+self.padding_top,1121,self.vertical_line_pos, self.default_pen) #4 Line

        self.removable_objects.append(line_1)
        self.removable_objects.append(line_2)
        self.removable_objects.append(line_3)
        self.removable_objects.append(line_4)

        # Head Values
        self.sum_hours_value_text = self.scene.addText(self.format_duration(sum_duration))
        self.sum_hours_value_text.setPos(self.center_text(self.sum_hours_value_text,555,828)-30,80+self.padding_top)
        self.sum_hours_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))
        self.removable_objects.append(self.sum_hours_value_text)

        self.sum_earnings_value_text = self.scene.addText(self.format_earnings(sum_earnings))
        self.sum_earnings_value_text.setPos(self.center_text(self.sum_earnings_value_text,828,1101),80+self.padding_top)
        self.sum_earnings_value_text.setFont(QtGui.QFont('SansSerif', pointSize=23))
        self.removable_objects.append(self.sum_earnings_value_text)

        padding_bottom = 40
        self.scene.setSceneRect(0,0,1130,self.vertical_line_pos+padding_bottom)

    def update(self,data):
        #remove old data
        for item in self.removable_objects: 
            self.scene.removeItem(item)

        #print new data
        self.draw_from_data(data)

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
            return "{:2.0f} Stunden".format(duration).replace('.',',')
        else:
            return "{:2.1f} Stunden".format(duration).replace('.',',')

    def format_earnings(self, earning):
        return "{:4.2f} €".format(earning).replace('.',',')

    def center_text(self,text_obj, left_border, right_border):
        text_width = text_obj.boundingRect().width()
        range = right_border - left_border
        
        start_position = ((range - (2*text_width)) / 2 ) + left_border
        return start_position

    def mousePressEvent(self, event):
        """ 
        Functionality of mouse click on row elements
        """

        position = event.pos()
    
        # print(f"Positions: {position.x()}, {position.y()}")

        obj = self.itemAt(event.pos())
        row_obj = self.l[[item['Object'] for item in self.l].index(obj)]
        row_number = row_obj['Row_Nr']

        # print(obj)
        # print(row_number)  
       
        self.editClicked.emit([row_obj['Data'], row_number])

class ContentArea(QtWidgets.QWidget):

    addClicked = QtCore.Signal()
    button_state = 1
 
    def __init__(self, data):
        super().__init__()

        widget_layout = QtWidgets.QVBoxLayout()

        self.entry_overview_widget = EntryOverview(data)
        
        widget_layout.setAlignment(QtCore.Qt.AlignHCenter)

        widget_layout.addSpacing(30)
        widget_layout.addWidget(self.entry_overview_widget)
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
            self.addClicked.emit()

    def switch_button_state(self):
        self.button_state += 1
        self.button_state = self.button_state % 2

        print("Button State: " + str(self.button_state))      