from models.__init__ import CONN, CURSOR
from models.member import Member
from models.trainer import Trainer

def seed_database():
    Trainer.drop_table()
    Trainer.create_table()
    Member.drop_table()
    Member.create_table()

    jeff = Trainer.create("Jeff Flexman", "M")
    jeffe = Trainer.create("Jeffe Flexman", "M")

    steve = Member.create("Steve Limparm", "I want to have strong legs.")
    # Member.create("Jessie Flexie", 89, "I want to do one armed push ups.", jeff.id)


seed_database()
print("Seeded database")