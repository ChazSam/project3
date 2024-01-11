from models.member import Member
from models.trainer import Trainer

def exit_program():
    print("Goodbye")
    exit()


def list_trainers():
    trainers = Trainer.get_all()
    print("Trainers: ")
    for i, trainer  in enumerate(trainers, start=1) :
        print(f"{i}. {trainer.name} ")

def list_members():
    members = Member.get_all()
    print("Members: ")
    for i, member  in enumerate(members, start=1) :
        print(f"{i}. {member.name} ")

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
    age = int(input("Enter the members age\n"))
    goals = input("Enter the members goals\n")
    list_trainers()
    trainer = int(input("enter a number to assign a trainer: \n"))
    try:
        member = Member.create(name, age, goals, trainer)
        print(f"{member.name} added to the database")
    except Exception as exc:
        print(f"Error: {exc}")
        

def remove_trainer():
    name = input("Enter trainers name you want to remove: ")
    #id_ = Trainer.find_by_name(name)
    breakpoint()
    if trainer := Trainer.find_by_name(name):
        trainer.delete()
        print(f"Trainer {name} deleted")
    else:
        print(f'Trainer {name} not found')


def remove_member():
    name = input("Enter member's name you want to remove: ")
    # breakpoint()
    if member := Member.find_by_name(name):
        member.delete()
        print(f"Member {name} removed")
    else:
        print(f'Member {name} not found')


def update_trainers():
    pass

def update_members():
    pass
