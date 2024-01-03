from models.__init__ import CONN, CURSOR
from models.member import Member
from models.trainer import Trainer

def seed_database():
    Trainer.drop_table()
    Member.drop_table()
    Trainer.create_table()
    Member.create_table()


seed_database()
print("Seeded database")