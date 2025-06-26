from manager.agent_manager import AgentManager  # או הנתיב שלך

manager = AgentManager()

def menu():
    print("\nAgent Control Center")
    print("1. View all agents")
    print("2. Add new agent")
    print("3. Find agent by ID")
    print("4. Update agent")
    print("5. Delete agent")
    print("0. Exit")

def view_agents():
    manager.view_all_agents()

def add_agent():
    code_name = input("Code name: ")
    real_name = input("Real name: ")
    location = input("Location: ")
    status = input("Status (e.g., Active): ")
    missions = int(input("Missions completed: "))
    manager.add_agent(code_name, real_name, location, status, missions)

def find_agent():
    id = input("Agent ID to search: ")
    manager.find_agent_by_id(id)

def update_agent():
    id = input("Agent ID to update: ")
    code_name = input("New code name: ")
    real_name = input("New real name: ")
    location = input("New location: ")
    status = input("New status: ")
    missions = int(input("New mission count: "))
    updated = Agent(code_name, real_name, location, status, missions)
    manager.update_agent(id, updated)

def delete_agent():
    id = input("Agent ID to delete: ")
    manager.delete_agent(id)

def main():
    while True:
        menu()
        choice = input("Choose an option: ")
        match choice:
            case "1":
                view_agents()
            case "2":
                add_agent()
            case "3":
                find_agent()
            case "4":
                update_agent()
            case "5":
                delete_agent()
            case "0":
                print("Exiting... Bye.")
                break
            case _:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
