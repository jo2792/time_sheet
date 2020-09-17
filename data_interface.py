""" Module to build the interface with data storage """
__authors__ = "Jordan Alwon"
__copyright__ = "Copyright 2020"

import os
import pandas as pd
import datetime

class Database():
    """ Class for a Database Obejct

    Parameters:
    -----------

    Attributes:
    -----------

    """

    def __init__(self, user_name):

        # Derive file name from user name
        self.file_name = user_name + ".csv"

        if self._is_file():
            self._read()

        else:
            self._create()
        
    def _is_file(self):
        return os.path.isfile(self.file_name)

    def _create(self):
        self.df = pd.DataFrame()

    def _read(self):
        self.df = pd.read_csv(self.file_name, index_col=0)

    def save(self):
        self.df.to_csv(self.file_name)

    def add_entry(self, entry):
        if not isinstance(entry, Entry):
            raise TypeError

        row = entry.to_dict()
        self.df = self.df.append(row, ignore_index=True)  

        self.save()          

    def remove_entry(self):
        pass

    def replace_entry(self, entry_index, entry):
        if entry_index >= len(self.df):
            raise ValueError
        
        if not isinstance(entry, Entry):
            raise TypeError
        
        self.df.iloc[entry_index] = entry.to_dict()           

class Entry():

    def __init__(self, db_entry= None):
        
        if db_entry: #dict convert Contructor
            self.__creation_date = datetime.datetime.fromisoformat(db_entry['Creation Date'])
            self.__modification_date = datetime.datetime.fromisoformat(db_entry['Modification Date'])
            self.__author = db_entry['Author']
    
            self.__work_date = datetime.date.fromisoformat(db_entry['Work Date'])
            self.__start_time = datetime.time.fromisoformat(db_entry['Start Time'])
            self.__end_time = datetime.time.fromisoformat(db_entry['End Time'])
    
            self.__hourly_wage = db_entry['Hourly Wage']
            self.__is_vacation = bool(db_entry['Is Vacation'])
    
            self.__comment = db_entry['Comment']

        else: #default Constructor
            date = datetime.datetime.now()
            self.__creation_date = date
            self.__modification_date = date
            self.__author = "John Doe"
            
            self.__work_date = datetime.date(1900,1,1)
            
            self.__start_time = datetime.time(0,0)
            self.__end_time = datetime.time(0,0)

            self.__hourly_wage = 0.00
            self.__is_vacation = False

            self.__comment = " "

    @property
    def creation_date(self):
        return self.__creation_date

    @creation_date.setter
    def creation_date(self, _):
        print("The creation date can't be changed!")

    @property
    def modification_date(self):
        return self.__modification_date

    @modification_date.setter
    def modification_date(self, _):
        print("The modification_date is set automatically!")

    def __update_modification_date(self):
        self.__modification_date = datetime.datetime.now()

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author_name):
        if isinstance(author_name, str):
            self.__author = author_name
            self.__update_modification_date()
        else:
            print("Autor type must be string!")

    @property
    def work_date(self):
        return self.__work_date

    @work_date.setter
    def work_date(self, date):
        day, month, year = date
        self.__work_date = datetime.date(year, month, day)
        self.__update_modification_date()

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, time):
        hour, minute = time
        self.__start_time = datetime.time(hour, minute)
        self.__update_modification_date()

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, time):
        hour, minute = time
        self.__end_time = datetime.time(hour, minute)
        self.__update_modification_date()

    @property
    def hourly_wage(self):
        return self.__hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, wage):
        if isinstance(wage, float) or isinstance(wage, int):
            self.__hourly_wage = wage
            self.__update_modification_date()
        else:
            print("The wage type must be a number")

    @property
    def is_vacation(self):
        return self.__is_vacation

    @is_vacation.setter
    def is_vacation(self, boo):
        if isinstance(boo, bool):
            self.__is_vacation = boo
            self.__update_modification_date()
        else:
            print("The type must be a boolean")
    
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment_text):
        if isinstance(comment_text, str):
            self.__comment = comment_text
            self.__update_modification_date()
        else:
            print("Comment type must be string!")

    def to_dict(self):
        
        return { "Creation Date": self.creation_date.isoformat(),
                    "Modification Date": self.modification_date.isoformat(),
                    "Author": self.author,
                    "Work Date": self.work_date.isoformat(),
                    "Start Time": self.start_time.isoformat(),
                    "End Time": self.end_time.isoformat(),
                    "Hourly Wage": self.hourly_wage,
                    "Is Vacation": self.is_vacation,
                    "Comment": self.comment}