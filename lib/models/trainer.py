from models.__init__ import CURSOR, CONN

class Trainer:

    all = {}

    def __init__(self, name, work_days, id = None):
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
        sql = """CREATE TABLE IF NOT EXISTS trainers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        work_days TEXT)"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS trainers"""
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM trainers"""

        rows = CURSOR.execute(sql).fetchall()
        return  [cls.instance_from_db(row) for row in rows]

    def save(self):
        sql ="""INSERT INTO trainers (name, work_days) VALUES (?,?)"""

        CURSOR.execute(sql, (self.name, self.work_days))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, work_days):
        trainer = cls(name, work_days)
        trainer.save()
        return trainer
    
    def update(self):
        sql = """UPDATE trainers
        SET name = ?, work_days = ?
        WHERE id = ?"""

        CURSOR.execute(sql, (self.name, self.work_days, self.id))
        CONN.commit()

    def delete(self):

        sql = """ DELETE FROM trainers WHERE id = ? """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        trainer = cls.all.get(row[0])
        if trainer:
            trainer.name = row[1]
            trainer.work_days = row[2]
        else:
            trainer = cls(row[1], row[2])
            trainer.id = row[0]
            cls.all[trainer.id] = trainer
        return trainer

    @classmethod 
    def find_by_id(cls, id):
        sql="""SELECT * FROM trainers WHERE id = ? """

        row = CURSOR.execute(sql, (id,)).fetchone
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql= """SELECT * FROM trainers WHERE name is ?"""

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None