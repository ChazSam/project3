from helpers import (
      exit_program,
      list_trainers,
      list_members,
      create_trainer,
      create_member,
      remove_trainer,
      remove_member,
      update_trainer,
      update_member,
      blank
)

def main():
      while True:
            option = input("Welcome to Trainer App. Please enter a number for:\n\n" 
            "1. Select Trainers \n"
            "2. Select Members\n"
            "0. Quit\n")

            if option == "0":
                  exit_program()
            elif option == "1":
                  trainer_option()
            elif option == "2":
                  member_options()
            else:
                  return "Please enter a valid number."
            

def trainer_option():
      list_trainers()
      blank()
      print(" ")
      option = input("Enter what you would like to do: \n"
                        "1. Add Trainer \n"
                        "2. Update Trainer \n"
                        "3. Remove Trainer \n"
                        "4. Assign Trainer to a Member without a Trainer \n"
                        "0. Back\n")

      if option == "0":
            main()
      elif option == "1":
            create_trainer()
      elif option == "2":
            x()
      elif option == "3":
            remove_trainer()
      elif option == "4":
            pass
      else:
            return("Please enter a valid number. \n")
            
def member_options():
      list_members()
      blank()
      option = input("Enter what you would like to do: \n"
                        "1. Add Member \n"
                        "2. Update Member \n"
                        "3. Remove Member \n"
                        "4. List Members with Trainers \n"
                        "0. Back \n")

      if option == "0":
            main()
      elif option == "1":
            create_member()
      elif option == "2":
            update_member()
      elif option == "3":
            remove_member()
      elif option == "4":
            pass
      else:
            return("Please enter a valid number. \n")
      
def x():
      pass

def y():
      pass



if __name__ == "__main__":                  
      main()


"""
Welcome to the trainer app

Press 1 for trainers status
press 2 for members status
Press Q to quit


1 - trainers

List trainers()
What would you like to do?
add trainer
update trainer
List trainer()
      update name
      update workday
            x has an training day with y, would you like to continue?
      update all
remove trainer
      x has an training day with y, would you like to continue?
assign member to trainer
back

2 - members
List Members()
What would you like to do?
add member
      add_member()
assign member to trainer
update member
delete member
      remove_member()
list members assigned to trainers
back
"""


# trainer options- 2 - done
# enter name
# enter work days
# assign member
# assign times with member

# edit trainer - 3
# Change name
# change work days
# see assigned members
# assign member
# assign times with member

# add member options - 6
# enter name
# enter age
# enter goals
# assign trainer
# assign times
      
#