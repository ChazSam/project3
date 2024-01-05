from helpers import (
      exit_program,
      list_trainers
)

def main():
      while True:
            option = input("Welcome to Trainer App. Please enter a number for:\n" 
            "1. List all trainers \n"
            "2. Add a trainer\n"
            "3. Select a trainer\n"
            "4. Remove a trainer\n"

            "5. See all members\n"
            "6. Add a member\n"
            "7. Select a member\n"
            "8. Remove a member\n"

            "0. Exit Program\n")
            if option == "1":
                  list_trainers()
                  
            else:
                  exit_program()
                  
main()
# trainer options- 2
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