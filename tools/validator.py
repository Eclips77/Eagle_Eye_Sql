from models.agent import AgentStatus

class Validator:

    @staticmethod
    def choose_status():
        print("Choose agent status:")
        for i, status in enumerate(AgentStatus, start=1):
            print(f"{i}. {status.name}")
        while True:
            choice = input("Enter choice number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(AgentStatus):
                return list(AgentStatus)[int(choice)-1]
            print("Invalid choice. Try again.")


  
