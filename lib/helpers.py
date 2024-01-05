from models.member import Member
from models.trainer import Trainer

def exit_program():
    print("Goodbye")
    exit()


def list_trainers():
    trainers = Trainer.get_all()
    return [print(trainer) for trainer in trainers]
    # for trainer in trainers:
    #     print(trainer)


def list_members():
    members = Member.get_all()
    #return [print(member) for member in members]
        