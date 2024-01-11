from helpers import (
      exit_program,
      list_trainers,
      list_members,
      create_trainer,
      create_member,
      remove_trainer,
      remove_member,
      update_trainers,
      update_members
)

def main():
      while True:
            option = input("Welcome to Trainer App. Please enter a number for:\n" 
            "1. List all trainers \n"
            "2. Add a trainer\n"
            "3. Edit a trainer\n"
            "4. Remove a trainer\n"
            
            "\n"
            "5. See all members\n"
            "6. Add a member\n"
            "7. Edit a member\n"
            "8. Remove a member\n"
            "\n"
            "0. Exit Program\n")

            if option == "0":
                  exit_program()
            if option == "1":
                  list_trainers()
            if option == "2":
                  create_trainer()
            if option == "3":
                  exit_program()
            if option == "4":
                  remove_trainer()
            if option == "5":
                  list_members()
            if option == "6":
                  create_member()
            if option == "7":
                  exit_program()
            if option == "8":
                  remove_member()
            else:
                  return "Please enter a valid number."
            
if __name__ == "__main__":                  
      main()

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