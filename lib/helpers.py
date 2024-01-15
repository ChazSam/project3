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
    list_trainers()
    blank()
    id_ = int(input("Enter trainers number you want to remove: "))
    #id_ = Trainer.find_by_name(name)
    #breakpoint()
    if trainer := Trainer.find_by_id(id_):
        trainer.delete()
        print(f"Trainer deleted")
    else:
        print(f'Trainer not found')


def remove_member():
    list_members()
    blank()
    id_ = int(input("Enter member's number you want to remove: "))
    # breakpoint()
    if member := Member.find_by_id(id_):
        member.delete()
        print(f"Member removed")
    else:
        print(f'Member not found')

def update_trainer():
    list_trainers()
    blank()
    id_ = input("Enter member number to update: \n")
    if trainer := Trainer.find_by_id(id_):
        try:
            name = input("Enter Trainer's Name: \n")
            trainer.name = name
            work_days = input("Enter work_days: \n")
            trainer.work_days = work_days
            trainer.update()
            print(f"{trainer.name} updated")
        except Exception as exc:
            print(f"Error updating member: ", exc)
    else:
        print(f"Member not found")

def update_member():
    list_members()
    blank()
    id_ = input("Enter member number to update: \n")
    if member := Member.find_by_id(id_):
        try:
            name = input("Enter Members Name: \n")
            member.name = name
            age = int(input("Enter Members Age: \n"))
            member.age = age
            goals = input("Enter the members goals\n")
            member.goals = goals
            list_trainers()
            trainer = int(input("enter a number to assign a trainer: \n"))
            member.trainer_id = trainer
            member.update()
            print(f"{member.name} updated")
        except Exception as exc:
            print(f"Error updating member: ", exc)
    else:
        print(f"Member not found")


def blank():
      print(" ")