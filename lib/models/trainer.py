from models.__init__ import CURSOR,CONN

class Trainer:
    
    def __init__(self, name, work_days, id=None):
        self.name = name
        self.work_days = work_days
        self.id = id
   
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError ("Please enter a valid name")
        
    @property
    def work_days(self):
        return self._work_days
    
    @work_days.setter
    def work_days(self, work_days):
        if isinstance(work_days, str):
            self._work_days = work_days
        else:
            raise ValueError ("Please enter days with a single letter and commas (M,T,W,H,F,S)")
    
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS trainers(
        id INTERGER PRIMARY KEY,
        name TEXT,
        work_days TEXT)"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS trainers"""
        
        CURSOR.execute(sql)
        CONN.commit()

    def get_all(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def change_work_days(self):
        pass

    def assign_member(self):
        pass

    def remove_member(self):
        pass