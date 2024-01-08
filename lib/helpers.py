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
    name = input("Enter a trainer's full name: \n")
    days = input("Enter the days the trainer is working: \n")
    try:
        trainer = Trainer.create(name, days)
        print(f"{trainer.name} added to the database")
    except Exception as exc:
        print(f"Error: {exc}")


def create_member():
    name = input("Enter a trainer's full name\n")
    age = input("Enter the members age\n")
    goals = input("Enter the members goals\n")
    trainer = input("Enter trainer's name or 'None' \n")
    try:
        member = Member.create(name, age, goals, trainer)
        print(f"{member} added to the database")
    except Exception as exc:
        print(f"Error: {exc}")
        

def remove_trainer():
    name = input("Enter trainers name you want to remove: ")
    if trainer := Trainer.find_by_name(name):
        trainer.delete(name)
        print(f"Trainer {name} deleted")
    else:
        print(f'Trainer {name} not found')


def remove_member():
    name = input("Enter member's name you want to remove: ")
    if trainer := Member.find_by_name(name):
        trainer.delete(name)
        print(f"Member {name} removed")
    else:
        print(f'Member {name} not found')

def update_trainers():
    pass

def update_members():
    pass
