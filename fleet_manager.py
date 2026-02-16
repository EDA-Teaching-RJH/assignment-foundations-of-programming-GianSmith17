running = True

def init_database():
    # Code to initialize the database connection and create necessary tables
    names = ["Jean-Luc Picard", "William Riker", "Data", "Worf", "Deanna Troi"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["E001", "E002", "E003", "E004", "E005"]
    return names, ranks, divs, ids
    
def display_menu(): #Queries users full name, Prints the options and current student logged in and returns the user's choice.
    

    print("\n--- MENU ---")
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Update Rank")
    print("5. Display Roaster")
    print("6. Search Crew")
    print("7. Filter by Division")
    print("8. Calculate Payroll")
    print("9. Count Officers")
    print("10. Exit")

    choice = input("Select option: ")
    return choice

def add_member(names, ranks, divs, ids):     #Adds a new crew member to the system, ensuring unique ID and valid rank.
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_div = input("Division: ")
    new_id = input("ID: ")
    if new_id in ids:
        print("ID already exists. Please choose a unique ID.")
        return
    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    if new_rank not in valid_ranks:
        print("Invalid rank. Please enter a valid rank.")
        return
    
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    
    print("Crew member added.")

def remove_member(names, ranks, divs, ids): #Removes a crew member from the system based on their unique ID, ensuring the ID exists before attempting removal.
    rem_id = input("ID to remove: ")
    if rem_id in ids:
        idx = ids.index(rem_id)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Crew member removed.")
    else:
        print("Crew member not found.")

def update_rank(names, ranks, ids): #Updates the rank of a crew member based on their unique ID, ensuring the ID exists and the new rank is valid before updating.
    update_id = input("ID to update: ")
    if update_id in ids:
        idx = ids.index(update_id)
        new_rank = input("New Rank: ")
        valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
        if new_rank not in valid_ranks:
            print("Invalid rank. Please enter a valid rank.")
            return
        ranks[idx] = new_rank
        print("Rank updated.")
    else:
        print("Crew member not found.")

def display_roaster(names, ranks, divs, ids): #Displays the current crew roster in a formatted manner, showing each member's name, rank, division, and ID.
    print("Current Crew List:")
    for i in range(len(names)):
        print(f"{ids[i]}: {names[i]} - {ranks[i]} ({divs[i]})")
    
def search_crew(names, ranks, divs, ids):   #Searches for a crew member by name, displaying their details if found, and handling cases where the crew member does not exist in the system.
    search_name = input("Name to search: ")
    found = False
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"Found: {ids[i]}: {names[i]} - {ranks[i]} ({divs[i]})")
            found = True
            break
    if not found:
        print("Crew member not found.")

def filter_by_division(names, divs, ids):  #Filters the crew roster by division, allowing the user to select a division and displaying all crew members that belong to that division, while handling cases where no members are found in the selected division.
    filter_div = input("Choose division to filter by, Command, Operations, Sciences: ")
    print(f"Crew members in {filter_div} division:") 
    for i in range(len(names)):
        if divs[i].lower() == filter_div.lower():
            print(f"{names[i]}, div: {divs[i]}")
        
def calculate_payroll(ranks):  #Calculates the total payroll based on the ranks of the crew members, using a predefined salary structure for each rank, and handles cases where a rank may not be recognized in the salary structure.
    rank_salaries = {
        "Captain": 10000,
        "Commander": 8000,
        "Lt. Commander": 6000,
        "Lieutenant": 4000,
        "Ensign": 3000
    }
    total_payroll = sum(rank_salaries.get(rank, 0) for rank in ranks)
    print(f"Total Payroll: ${total_payroll}")
    return total_payroll 

def count_officers(ranks):  #Counts the number of officers in the crew based on their ranks, defining officers as those with ranks of "Captain", "Commander", or "Lt. Commander", and returns the count of officers in the system.
    officer_count = sum(1 for rank in ranks if rank in ["Captain", "Commander", "Lt. Commander"])
    print(f"Number of Officers: {officer_count}")
    return officer_count
    

def main(running = True):  #Initializes the system, prompts the user for their full name, and enters a loop that displays the menu and processes user choices until the user decides to exit the system.
    names, ranks, divs, ids = init_database()
    full_name = input("Enter your full name: ")
    print(f"Welcome, {full_name}!")
    while running == True:
        choice = display_menu()
        
        if choice == "1":
            display_roaster(names, ranks, divs, ids)
        elif choice == "2":
            add_member(names, ranks, divs, ids)
        elif choice == "3":
            remove_member(names, ranks, divs, ids)
        elif choice == "4":
            update_rank(names, ranks, ids)
        elif choice == "5":
            display_roaster(names, ranks, divs, ids)
        elif choice == "6":
            search_crew(names, ranks, divs, ids)
        elif choice == "7":
            filter_by_division(names, divs, ids)
        elif choice == "8":
            calculate_payroll(ranks)
        elif choice == "9":
            count_officers(ranks)
        elif choice == "10":
            print("Exiting system. Goodbye!")
            running = False
        else:
            print("Invalid option. Please select a valid option.")
           
        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice.lower() != 'y':
            print("Exiting system. Goodbye!")
            running = False
main() #Starts the main function to run the fleet management system.