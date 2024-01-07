from models.member import Member
from models.trainer import Trainer

def exit_program():
    print("Goodbye")
    exit()


def list_trainers():
    trainers = Trainer.get_all()
    return [print(trainer.name, trainer.work_days) for trainer in trainers]

def list_members():
    members = Member.get_all()
    return [print(member) for member in members]


def create_trainer():
    name = input("Enter a trainer's full name")
    days = input("Enter the days the trainer is working")
    try:
        trainer = Trainer.create(name, days)
        print(f"{trainer} added to the database")
    except Exception as exc:
        print(f"Error: {exc}")


def create_member():
    name = input("Enter a trainer's full name")
    age = input("Enter the members age")
    goals = input("Enter the members goals")
    trainer = input("Enter trainer's name or 'None' ")
    try:
        member = Member.create(name, age, goals, trainer)
        print(f"{member} added to the database")
    except Exception as exc:
        print(f"Error: {exc}")
        

def remove_trainer():
    pass


def remove_member():
    pass

