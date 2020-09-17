from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from data_interface import Entry as db_Entry

class Entry(QtWidgets.QWidget):
    close_signal = QtCore.Signal()
    save_entry_signal = QtCore.Signal(db_Entry)

    def __init__(self, work_dates_df):
        
        # Sub init functions
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

        super().__init__()

        sp_retain = QtWidgets.QSizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        sp_retain.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)

        ### Define wideget elements

        # Headline
        self.headline_label = QtWidgets.QLabel("Eintrag bearbeiten")
        self.headline_label.setAlignment(QtCore.Qt.AlignLeft)
        font = QtGui.QFont('SansSerif',pointSize=20)
        font.setUnderline(True)
        self.headline_label.setFont(font)
        self.headline_label.setSizePolicy(sp_retain)

        # Work Date
        self.date_label = set_default_label_style(QtWidgets.QLabel("Datum:"))
        self.date_field = set_default_field_style(QtWidgets.QDateEdit())
        self.date_field.setDisplayFormat('dd.MM.yyyy')
        self.date_field.setDate(self.get_next_work_date(work_dates_df))
        self.date_field.setCalendarPopup(True)
        
        # Work start time
        self.start_time_label = set_default_label_style(QtWidgets.QLabel("Beginn:"))
        self.start_time_field = set_default_field_style(QtWidgets.QTimeEdit())
        # self.start_time_label.setMinimumSize()
        # Work end time
        self.end_time_label = set_default_label_style(QtWidgets.QLabel("Ende:"))
        self.end_time_field = set_default_field_style(QtWidgets.QTimeEdit())

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
        self.accept_button = QtWidgets.QPushButton()
        self.accept_button.setStyleSheet("""QPushButton {
                                    background-color: transparent;
                                    border-image: url(resources/button_icons/Accept.png);
                                    background: none;
                                    background-repeat:none;
                                    } """)
        self.accept_button.setFixedSize(75,75)

        self.delete_button = QtWidgets.QPushButton()
        self.delete_button.setStyleSheet("""QPushButton {
                                    background-color: transparent;
                                    border-image: url(resources/button_icons/Delete.png);
                                    background: none;
                                    background-repeat:none;
                                    } """)
        self.delete_button.setFixedSize(75,75)

        self.cancel_button = QtWidgets.QPushButton()
        self.cancel_button.setStyleSheet("""QPushButton {
                                    background-color: transparent;
                                    border-image: url(resources/button_icons/Cancel.png);
                                    background: none;
                                    background-repeat:none;
                                    } """)
        self.cancel_button.setFixedSize(75,75)
        
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

        self.add_to_grid(self.headline_label, horizontal_start=0, horizontal_length=3)

        self.add_to_grid(self.date_label, 'Label')
        self.add_to_grid(self.date_field, 'Field')

        self.add_to_grid(self.start_time_label, 'Label')
        self.add_to_grid(self.start_time_field, 'Field')

        self.add_to_grid(self.end_time_label, 'Label')
        self.add_to_grid(self.end_time_field, 'Field')
        
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
        self.button_line = QtWidgets.QFrame()
        self.button_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.button_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.widget_line = QtWidgets.QFrame()
        self.widget_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.widget_line.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Button Area
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.accept_button)
        # button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.cancel_button)

        widget_content = QtWidgets.QVBoxLayout()
        widget_content.addWidget(scroll_area)
        widget_content.addSpacing(30)
        widget_content.addWidget(self.button_line)
        widget_content.addLayout(button_layout)

        widget_layout = QtWidgets.QHBoxLayout()
        widget_layout.addWidget(self.widget_line)
        widget_layout.addLayout(widget_content)

        self.setLayout(widget_layout)

        self.fold_button.clicked.connect(self.dropdown_visibility)
        self.accept_button.clicked.connect(self.accept_process)
        self.cancel_button.clicked.connect(self.cancel_process)

        self.dropdown_visibility()

    def get_next_work_date(self, df):
        df = df.str.split('-', expand=True)
        df = df.sort_values(by=[0,1,2])
        year = int(df.iloc[-1][0])
        month = int(df.iloc[-1][1])
        day = int(df.iloc[-1][2])

        date = QtCore.QDate(year, month, day)
        week_day = date.dayOfWeek()

        if week_day in [2,3]:
            date = date.addDays(4-week_day)
        elif week_day == 1:
            date = date.addDays(1)
        elif week_day in [4,5,6,7]:
            date = date.addDays(9-week_day)
        
        return date


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

    def dropdown_visibility(self):
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

    def accept_process(self):
        print("Emit Signal from accept button")

        self.save_entry()
        self.close_signal.emit()

    def cancel_process(self):
        print("Emit signal from cancle button")
        self.close_signal.emit()

    def remove_widget(self):
        self.deleteLater()

    def save_entry(self):
        entry = db_Entry()
        
        entry.author = self.author_text.text()
        entry.work_date = (self.date_field.date().day(), self.date_field.date().month(), self.date_field.date().year())
        entry.start_time = (self.start_time_field.time().hour(), self.start_time_field.time().minute())
        entry.end_time = (self.end_time_field.time().hour(), self.end_time_field.time().minute())
        entry.hourly_wage = float(self.wage_textbox.text().replace(' €','').replace(',','.'))
        entry.is_vacation = self.vacation_checkbox.isChecked()
        entry.comment = self.comment_textbox.toPlainText()

        self.save_entry_signal.emit(entry)

        