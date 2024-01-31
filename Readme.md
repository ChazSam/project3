Trainer CLI	
    
This application is a Python Command Line Interface (CLI) that allows a user to add trainers, members, update information about each, remove them, and show information about a specific trainer or member. The user would see the following options: selecting a trainer and viewing all members assigned to them, listing all members and their respective trainers, and displaying complete information about each member, including their name, age, goals, and assigned trainer. One trainer can have multiple members, but each member can only have one trainer at a time. All of the data will be stored in a single database using SQL.
Starting in the backend, the models folder holds three files; an init, a member, and a trainer python file. These files use SQL to create a database that does the following for trainers and members: Create table, drop table, get all, save update delete, instance from db, find by id, and find by name. The trainer’s database also has a method called members that goes into the member’s database and returns information about members assigned to a certain trainer.
For trainers and members, each attribute is assigned a setter and getter to limit what information a user can input whether they need to input an integer or that they have to enter a certain age for a member. 
The Setters for trainers attributes are: 
name-a string with at least one letter
workdays-they enter from a list either MTWHFSU to represent the day of the week they are working. 
The Setters for members attributes are:
name - a string with at least one letter
age - an integer where the member has to be 18 or older
goals - a string with at least one letter
trainer_id - an integer that is at least 1 and cannot be more than the length of the list. 
In the front end, there are three files, the cli, helpers, and seed. Running seed.py will create an initial database to work with that can be used when you first run the program or if you want to return default values in the database. Next is the cli, which first, imports the functions from the helpers file, then creates the command lines that will be used in this application. With each option, there is a function within the helper's file that does different actions. 
exit_program() - end the program.
list_trainers()- takes all the trainers within the trainer's database and numbers their names in order.
list_members() - takes all the members within the member's database and numbers their names in order.
create_trainer() - takes inputs of the trainer's name and work days and adds them to the database
create_member() - takes inputs of a member's name, age, and goals for their workout out and the user assigns a trainer to them; then, adds them to the members database.
remove_trainer() - lists all of the trainers and asks the user which one to remove. If a trainer is assigned a member, the CLI will ask them to reassign the member to a different trainer before deleting them. 
remove_member() - lists all the members and asks which one to remove from the list. 
update_trainer() - asks the user to re-enter the choices from create_trainer and changes them in the database.
update_member() - asks the user to renter the choices from create member and changes them in the database.
list_members_and_trainers() - prints each member's name and the trainer's name assigned to them.
reassign_members() - takes a member, lists all other trainers than the one assigned to them, and prompts the user to choose a different trainer for them. 
trainer_info() - gets all of the trainers from the trainers' table, lists each trainer, and prints their name, work days, and members assigned to them. 
member_info() - gets all of the members from the members' table, lists each one, and prints the name, age, goals, and trainer's name of that member.
blank() - formats a blank line to format the CLI.
