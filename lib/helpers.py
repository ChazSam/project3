from models.member import Member
from models.trainer import Trainer

def exit_program():
    print("Goodbye")
    exit()


def list_trainers():
    trainers = Trainer.get_all()
    blank()
    print("Trainers: ")
    [print(f"{i}. {trainer.name} ") for i, trainer in enumerate(trainers, start=1)]        


def list_members():
    members = Member.get_all()
    blank()
    print("Members: ")
    [print(f"{i}. {member.name} ") for i, member in enumerate(members, start=1)]        


def create_trainer():
    name = input("Enter a trainer's full name: \n")
    days = input("Enter the days the trainer is working (enter MTWHFSU, no spaces): \n")
    try:
        trainer = Trainer.create(name, days.upper())
        print(f"{trainer.name} added to the database")
    except Exception as exc:
        print(f"Error: {exc}")


def create_member():
    name = input("Enter a Members's full name\n")
    try:
        age = int(input("Enter the members age (members must be 18+)\n"))
    except ValueError:
            print("Please enter a number.")
    goals = input("Enter the members goals\n")
    list_trainers()
    try:
        trainer = int(input("enter a number to assign a trainer: \n"))
    except ValueError:
        print("Please enter a number.")

    try:
        member = Member.create(name, age, goals, trainer)
        print(f"{member.name} added to the database")
    except Exception as exc:
        print(f"Error: {exc}")
        

def remove_trainer():
    trainers = Trainer.get_all()
    [print(f"{i}. {trainer.name} ") for i, trainer in enumerate(trainers, start=1) ]
    blank()

    try:
        choice = int(input("Enter trainers number you want to remove: "))

        if 1 <= choice <= len(trainers):
            selected_trainer = trainers[choice -1]
            reassign_Members(selected_trainer)
            selected_trainer.delete()
            print("Trainer deleted")
        else:
            print("Trainer not found")

    except ValueError:
        print("Please enter a number.")

def remove_member():
    members = Member.get_all()
    [ print(f"{i}. {member.name} ") for i, member in enumerate(members, start=1)]
    blank()

    try:
        choice = int(input("Enter member's number you want to remove: "))

        if 1 <= choice <= len(members):
            selected_member = members[choice-1]
            selected_member.delete()
            print(f"Member removed")
        else:
            print(f'Member not found')

    except ValueError:
        print("Please enter a number.")

def update_trainer():
    trainers = Trainer.get_all()
    [print(f"{i}. {trainer.name} ") for i, trainer in enumerate(trainers, start=1) ]
    blank()

    try:
        choice = int(input("Enter member number to update: \n"))

        if 1 <= choice <= len(trainers):
            selected_trainer = trainers[choice -1]

            try:
                name = input("Enter Trainer's Name: \n")
                selected_trainer.name = name
                work_days = input("Enter work_days: \n")
                selected_trainer.work_days = work_days.upper()
                selected_trainer.update()
                print(f"{selected_trainer.name} updated")

            except Exception as exc:
                print(f"Error updating member: ", exc)

        else:
            print(f"Member not found")

    except ValueError:
        print("Please enter a number\n")

def update_member():
    members = Member.get_all()
    [ print(f"{i}. {member.name} ") for i, member in enumerate(members, start=1)]
    blank()


    try:
        choice = int(input("Enter member's number you want to update: "))

        if 1 <= choice <= len(members):
            selected_member = members[choice-1]

            try:
                name = input("Enter Members Name: \n")
                selected_member.name = name
                try:
                    age = int(input("Enter Members Age: \n"))
                except ValueError:
                    print("Please enter a number.")
                selected_member.age = age
                goals = input("Enter the members goals\n")
                selected_member.goals = goals

                trainers = Trainer.get_all()
                [print(f"{i}. {trainer.name} ") for i, trainer in enumerate(trainers, start=1) ]
                blank()

                try:
                    choice = int(input("enter a number to assign a trainer: \n"))

                    if 1 <= choice <= len(trainers):
                        selected_trainer = trainers[choice -1]

                        try:
                            selected_member.trainer_id = selected_trainer.id
                            selected_member.update()
                            print(f"{selected_member.name} updated")

                        except ValueError:
                            print("Please enter a number.")                   

                except ValueError:
                    print("Please enter a valid number.")

            except Exception as exc:
                print(f"Error updating member: ", exc)

        else:
            print(f"Member not found")

    except ValueError:
        print("Please enter a number\n")
    
def list_members_and_trainers(): 
    members = Member.get_all()
    for i, member  in enumerate(members, start=1):
        trainer = Trainer.find_by_id(member.trainer_id)
        print(f"{i}. {member.name} - Trainer: {trainer.name}")


def reassign_Members(trainer):
    get_members = trainer.members()
    for member in get_members:
        print(f"{member.name} is assigned to {trainer.name}, Please reassign the member to another trainer.")
        trainer_list = Trainer.get_all()

        if trainer in trainer_list:
            trainer_list.remove(trainer)

        [print(f"{i}. {trainer.name}") for i, trainer in enumerate(trainer_list, start=1)]

        try:
            choice = int(input("Select which trainer to replace the previous \n"))

            if 1 <= choice <= len(trainer_list):
                selected_trainer = trainer_list[choice-1]
                member.trainer_id = selected_trainer.id
                member.update()
                print(f"Member: {member.name} trainer has been updated")

            else:
                print ("Trainer does not exist")
                remove_trainer()
                
        except ValueError:
            print("Please enter a number")


def trainer_info():
    trainers = Trainer.get_all()
    [print(f"{i}. {trainer.name} ") for i, trainer in enumerate(trainers, start=1)]
        
    try:
        choice = int(input("Select a trainer for all info: \n"))

        if 1 <= choice <= len(trainers):
            selected_trainer = trainers[choice-1]
            get_members = selected_trainer.members()

            print(f"Trainer: \n"
                f"{selected_trainer.name}  Work days - {selected_trainer.work_days} \n"
                "Assigned Members: ")
            [print(m.name) for m in get_members]
            blank()
        else:
            print("Please enter a valid number")

    except ValueError:
        print("Please enter a number.")

def member_info():
    members = Member.get_all()
    [ print(f"{i}. {member.name} ") for i, member in enumerate(members, start=1)]
        
    try:
        choice = int(input("Select a trainer for all info: \n"))

        if 1 <= choice <= len(members):
            selected_member = members[choice-1]
            get_trainer = Trainer.find_by_id(selected_member.trainer_id)

            print(f"{selected_member.name} Age: {selected_member.age} Goals: {selected_member.goals}\nTrainer: {get_trainer.name}")
            blank()
        else:
            print("Member not found")

    except ValueError:
        print("Please enter a number.")

def blank():
      print(" ")
