from Dal.agent_dal import AgentDAL
from models.agent import Agent, AgentStatus

def print_menu():
    print("\n==== Eagle Eye Agent Management ====")
    print("1. View all agents")
    print("2. Add a new agent")
    print("3. Find agent by ID")
    print("4. Exit")

def get_status_from_user():
    print("Choose status:")
    for i, status in enumerate(AgentStatus):
        print(f"{i + 1}. {status.value}")
    choice = int(input("Enter status number: ")) - 1
    return list(AgentStatus)[choice]

def main():
    dal = AgentDAL()   # Initialize the DAL
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            agents = dal.get_all_agents()
            for row in agents:
                print(row)

        elif choice == "2":
            code_name = input("Code name: ")
            real_name = input("Real name: ")
            location = input("Current location: ")
            status = get_status_from_user()
            missions = int(input("Missions completed: "))

            agent = Agent(code_name, real_name, location, status, missions)
            dal.add_agent_to_db(agent)

        elif choice == "3":
            id = int(input("Enter agent ID: "))
            agent = dal.get_agent_by_id(id)
            if agent:
                print(agent)
            else:
                print("Agent not found.")

        elif choice == "4":
            print("Exiting. Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
