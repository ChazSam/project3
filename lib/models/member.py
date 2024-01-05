from models.__init__ import CURSOR,CONN

class Member:

    all = {}

    # def __init__(self, name, age, goals, trainer_id, id = None):
    #     self.name = name
    #     self.age = age
    #     self.goals = goals
    #     self.trainer_id = trainer_id
    #     self.id = id

    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str) and len(name):
    #         self._name = name
    #     else:
    #         raise ValueError ("Please enter a valid name")
        
    # @property
    # def age(self):
    #     return self._age
    
    # @age.setter
    # def age(self, age):
    #     if isinstance(age, int) and age >= 18:
    #         self._age = age
    #     else:
    #         raise ValueError ("Please enter a number - Members must be at least 18 years old")
    
    # @property
    # def goals(self):
    #     return self._goals
    
    # @goals.setter
    # def goals(self, goals):
    #     if isinstance(goals, str) and len(goals):
    #         self._goals = goals
    #     else:
    #         raise ValueError ("Please enter a goal")
        
    # @property
    # def trainer_id(self):
    #     return self._trainer_id
    
    # @trainer_id.setter
    # def trainer_id(self, trainer_id):
    #     if type(trainer_id) is int:
    #         self._trainer_id = trainer_id
    #     else:
    #         raise ValueError("check trainer id")
        
    # @classmethod
    # def create_table(cls):
    #     sql = """CREATE TABLE IF NOT EXISTS members (
    #     id INTEGER PRIMARY KEY,
    #     name TEXT,
    #     age INTEGER,
    #     goals TEXT,
    #     trainer_id INTEGER,
    #     FOREIGN KEY (trainer_id) REFERENCES trainers(id))"""

    #     CURSOR.execute(sql)
    #     CONN.commit()


    # @classmethod
    # def drop_table(cls):
    #     sql = """DROP TABLE IF EXISTS members"""

    #     CURSOR.execute(sql)
    #     CONN.commit()


    # def save(self):
    #     sql = """INSERT INTO members (name, age, goals, trainer_id)
    #             VALUES (?, ?, ?, ?)"""

    #     CURSOR.execute(sql, (self.name, self.age, self.goals, self.trainer_id))
    #     CONN.commit()

    #     self.id = CURSOR.lastrowid
    #     type(self).all[self.id] = self
 
    # @classmethod
    # def create(cls, name, age, goals, trainer_id):
    #     member = cls(name, age, goals, trainer_id)
    #     member.save()
    #     return member

    
    # def get_all(self):
    #     pass

    # def create(self):
    #     pass

    # def delete(self):
    #     pass

    # def update_goals(self):
    #     pass

    def __init__(self, name, goals, id = None):
        self.name = name

        self.goals = goals
  
        self.id = id

    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str) and len(name):
    #         self._name = name
    #     else:
    #         raise ValueError ("Please enter a valid name")
        
    # @property
    # def goals(self):
    #     return self._goals
    
    # @goals.setter
    # def goals(self, goals):
    #     if isinstance(goals, str):
    #         self._goals = goals
    #     else:
    #         raise ValueError ("Please enter days with a single letter and commas (M,T,W,H,F,S)")
        

        
    # @property
    # def age(self):
    #     return self._age
    
    # @age.setter
    # def age(self, age):
    #     if isinstance(age, int) and age >= 18:
    #         self._age = age
    #     else:
    #         raise ValueError ("Please enter a number - Members must be at least 18 years old")
    
    # @property
    # def goals(self):
    #     return self._goals
    
    # @goals.setter
    # def goals(self, goals):
    #     if isinstance(goals, str) and len(goals):
    #         self._goals = goals
    #     else:
    #         raise ValueError ("Please enter a goal")
        
    # @property
    # def trainer_id(self):
    #     return self._trainer_id
    
    # @trainer_id.setter
    # def trainer_id(self, trainer_id):
    #     if type(trainer_id) is int:
    #         self._trainer_id = trainer_id
    #     else:
    #         raise ValueError("check trainer id")
        
#     @classmethod
#     def create_table(cls):
#         sql = """CREATE TABLE IF NOT EXISTS members (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
   
#         goals TEXT
# )"""

#         CURSOR.execute(sql)
#         CONN.commit()


#     @classmethod
#     def drop_table(cls):
#         sql = """DROP TABLE IF EXISTS members"""

#         CURSOR.execute(sql)
#         CONN.commit()


#     def save(self):
#         sql = """INSERT INTO members (name,  goals,)
#                 VALUES (?, ?)"""

#         CURSOR.execute(sql, (self.name, self.goals))
#         CONN.commit()

#         self.id = CURSOR.lastrowid
#         type(self).all[self.id] = self
 
#     @classmethod
#     def create(cls, name,  goals):
#         member = cls(name, goals)
#         member.save()
#         return member
        
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        name TEXT,
        goals TEXT)"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS members"""

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """INSERT INTO members (name, goals)
        VALUES (?,?)"""

        CURSOR.execute(sql, (self.name, self.goals))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, goals):
        member = cls(name, goals)
        member.save()
        return member

    def get_all(cls):
        sql = """SELECT * FROM members"""

        rows = CURSOR.execute(sql).fetchall()
        return  [cls.instance_from_db(row) for row in rows]

    def create(self):
        pass

    def delete(self):
        pass

    def update_goals(self):
        pass