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
      list_members_and_trainers,
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
                  print("Please enter a valid number.") 
            

def trainer_option():
      while True:
            list_trainers()
            blank()
            option = input("Enter what you would like to do: \n"
                              "1. Add Trainer \n"
                              "2. Update Trainer \n"
                              "3. Remove Trainer \n"
                              "4. Select trainer info and members assigned \n"
                              "0. Back\n")

            if option == "0":
                  main()
            elif option == "1":
                  create_trainer()
            elif option == "2":
                  update_trainer()
            elif option == "3":
                  remove_trainer()
            elif option == "4":
                  pass
            else:
                  print("Please enter a valid number. \n")
            
def member_options():
      while True:
            list_members()
            blank()
            option = input("Enter what you would like to do: \n"
                              "1. Add Member \n"
                              "2. Update Member \n"
                              "3. Remove Member \n"
                              "4. List Members with Trainers \n"
                              "5. get all info for selected member including trainer name \n"
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
                  list_members_and_trainers()
            elif option == "5":
                  pass
            else:
                  print("Please enter a valid number. \n")
            

if __name__ == "__main__":                  
      main()
