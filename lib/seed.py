from models.__init__ import CONN, CURSOR
from models.member import Member
from models.trainer import Trainer

def seed_database():
    Trainer.drop_table()
    Member.drop_table()
    Trainer.create_table()
    Member.create_table()

    jeff = Trainer.create("Jeff Flexman", "MWF")
    lisa = Trainer.create("Lisa Misa", "TH")

    Member.create("Steve Limparm", 21, "I want to have strong legs.", jeff.id)
    Member.create("Jessie Flexie", 89, "I want to do one armed push ups.", lisa.id)
    Member.create("Joey Jojo", 23, "I want to be taller", None)


seed_database()
print("Seeded database")