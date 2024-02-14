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
      trainer_info,
      member_info,
      blank
)

def main():
      while True:
            option = input("Welcome to Trainer Assignment App. Please enter a number for:\n\n" 
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
            #list_trainers()
            blank()
            option = input("Enter what you would like to do: \n"
                              "1. Add a Trainer \n"
                              "2. Update a Trainer info \n"
                              "3. Remove a Trainer \n"
                              "4. Display a Trainer's info with Members assigned to the Trainer \n"
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
                  trainer_info()
            else:
                  print("Please enter a valid number. \n")
            
            
def member_options():
      while True:
            #list_members()
            blank()
            option = input("Enter what you would like to do: \n"
                              "1. Add a Member \n"
                              "2. Update a Member \n"
                              "3. Remove a Member \n"
                              "4. List all Members with Trainers \n"
                              "5. List all infomation for a Member \n"
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
                  member_info()
            else:
                  print("Please enter a valid number. \n")
            

if __name__ == "__main__":                  
      main()
