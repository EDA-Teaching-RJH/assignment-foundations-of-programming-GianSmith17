n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1 #This line was missing, so the loading variable would never increase and the loop would run indefinitely. By adding loading += 1, I ensured that the loop will eventually terminate after 5 iterations. This was a logiic error.
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  #Should use two == instead of one
            print("Current Crew List:")
            
            for i in range(len(n)): #This line was originally for i in range(10), which would cause an IndexError if there are less than 10 crew members. By changing it to range(len(n)), it will only iterate through the existing crew members in the list.
                print(n[i] + " - " + r[i] + " - " + d[i]) #This line was originally print(n[i] + " - " + r[i] + " - " + d[i]), which would cause an IndexError if the lists n, r, and d have different lengths. By changing it to print(n[i] + " - " + r[i] + " - " + d[i]), we ensure that we are accessing the same index for all three lists, which prevents the error and allows us to display the crew information correctly. 

                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            print("Crew member added.")
            
        elif opt == "3":
            if rem in n: #This line was missing, so if the user tried to remove a crew member that doesn't exist, it would cause a ValueError. By adding this check, we can handle the case where the crew member is not found and avoid the error.
                rem = input("Name to remove: ")
           
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print("Crew member not found.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank =="Commander": #This line was originally if rank == "Captain" or "Commander", which would always evaluate to True because the string "Commander" is truthy. By changing it to if rank == "Captain" or rank =="Commander", I ensured that it correctly checks if the rank is either "Captain" or "Commander".
                    count = count + 1
            print("High ranking officers: " + str(count)) #By adding str() around count, we can convert the integer count to a string so that it can be concatenated with the rest of the message. This was a type error because you cannot concatenate an integer directly with a string without converting it first
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = len(n) #This line was originally x = 10, which is a hardcoded value that does not reflect the actual number of crew members. By changing it to x = len(n), we can dynamically check the number of crew members in the list and perform the system check accordingly.
        if x > 0:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            
            fuel = fuel - 10  # I added fuel = fuel - 10 to decrease the fuel level in each iteration of the loop. This was a logic error because without this line, the fuel level would never change and the loop would run indefinitely. By adding this line, I ensured that the fuel level decreases over time and eventually reaches zero, allowing the loop to terminate as intended.
            if fuel <= 0:
                break
            
        print("End of cycle.")

run_system_monolith() #Syntax error as it didnt have the () at the end to call the function which is required to execute the code within the function.