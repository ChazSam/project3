from models.__init__ import CURSOR,CONN

class Member:
    
    def __init__(self, name, age, goals, id=None):
        self.name = name
        self.age = age
        self.goals = goals
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
            raise ValueError ("Please enter a number - Members must be at least 18 years old")
    
    @property
    def goals(self):
        return self._goals
    
    @goals.setter
    def goals(self,goals):
        if isinstance(goals, str) and len(goals):
            self._goals = goals
        else:
            raise ValueError ("Please enter a goal")
        
    @classmethod
    def create_table(cls):
        sql ="""CREATE TABLE IF NOT EXISTS members(
        id INTERGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        goals TEXT,
        FOREIGN KEY (trainer_id) REFERENCES trainers(id))"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS members"""

        CURSOR.execute(sql)
        CONN.commit()

    def get_all(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def update_goals(self):
        pass