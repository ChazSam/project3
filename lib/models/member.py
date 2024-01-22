from models.__init__ import CURSOR, CONN
from models.trainer import Trainer

class Member:

    all = {}

    def __init__(self, name, age, goals, trainer_id, id = None):
        self.name = name
        self.age = age
        self.goals = goals
        self.trainer_id = trainer_id
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
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age >= 18:
            self._age = age
        else:
            raise ValueError ("Members must be at least 18 years old")
    
    @property
    def goals(self):
        return self._goals
    
    @goals.setter
    def goals(self, goals):
        if isinstance(goals, str) and len(goals):
            self._goals = goals
        else:
            raise ValueError ("Please enter a goal")
        
    @property
    def trainer_id(self):
        return self._trainer_id
    
    @trainer_id.setter
    def trainer_id(self, trainer_id):
        trainer_list = Trainer.get_all()
        if isinstance(trainer_id, int) and 1 <= trainer_id <= len(trainer_list):
            self._trainer_id = trainer_id
        else:
            raise ValueError("Member must be assigned a trainer.")
    
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        goals TEXT,
        trainer_id INTEGER,
        FOREIGN KEY (trainer_id) REFERENCES trainers(id))"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS members"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM members"""

        rows = CURSOR.execute(sql).fetchall()
        return  [cls.instance_from_db(row) for row in rows]

    def save(self):
        sql = """INSERT INTO members (name, age, goals, trainer_id) VALUES (?, ?, ?, ?)"""

        CURSOR.execute(sql, (self.name, self.age, self.goals, self.trainer_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
 
    @classmethod
    def create(cls, name, age, goals, trainer_id):
        member = cls(name, age, goals, trainer_id)
        member.save()
        return member
    
    def update(self):
        sql = """ UPDATE members
        SET name = ?, age = ?, goals = ?, trainer_id = ?
        WHERE id = ? """

        CURSOR.execute(sql, (self.name, self.age, self.goals, self.trainer_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM members WHERE id = ?"""

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        member = cls.all.get(row[0])
        if member:
            member.name = row[1]
            member.age = row[2]
            member.goals = row[3]
            member.trainer_id = row[4]
        else:
            member = cls(row[1], row[2], row[3], row[4])
            member.id = row[0]
            cls.all[member.id] = member
        return member

    @classmethod
    def find_by_id(cls, id):
        sql="""SELECT * FROM members WHERE id = ? """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql= """SELECT * FROM members WHERE name is ?"""

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None


