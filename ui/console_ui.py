from Dal.agent_dal import AgentDAL
from Dal.agent_manager import AgentManager
from models.agent import Agent, AgentStatus
from tools.validator import Validator


class ConsoleUI:
    """Console based menu UI."""

    def __init__(self):
        self.manager = AgentManager(AgentDAL())

    def run(self):
        while True:
            choice = self._menu()
            if choice == '1':
                self.add_agent()
            elif choice == '2':
                self.update_agent()
            elif choice == '3':
                self.delete_agent()
            elif choice == '4':
                self.find_agent()
            elif choice == '5':
                self.view_all_agents()
            elif choice == '0':
                print('Goodbye!')
                break
            else:
                print('Invalid choice.')

    def _menu(self):
        print('\n=== Agent Control Center ===')
        print('1. Add Agent')
        print('2. Update Agent')
        print('3. Delete Agent')
        print('4. Find Agent by ID')
        print('5. View All Agents')
        print('0. Exit')
        return input('Choose an option: ')

    def add_agent(self):
        code_name = input('Code Name: ')
        real_name = input('Real Name: ')
        location = input('Location: ')
        status = Validator.choose_status()
        missions = int(input('Missions Completed: ') or 0)
        self.manager.add_agent(code_name, real_name, location, status, missions)
        print('Agent added successfully.')

    def update_agent(self):
        agent_id = input('Agent ID to update: ')
        if not agent_id.isdigit():
            print('Invalid ID.')
            return
        code_name = input('Code Name: ')
        real_name = input('Real Name: ')
        location = input('Location: ')
        status = Validator.choose_status()
        missions = int(input('Missions Completed: ') or 0)
        agent = Agent(code_name, real_name, location, status, missions)
        self.manager.update_agent(int(agent_id), agent)
        print('Agent updated successfully.')

    def delete_agent(self):
        agent_id = input('Agent ID to delete: ')
        if not agent_id.isdigit():
            print('Invalid ID.')
            return
        self.manager.delete_agent(int(agent_id))
        print('Agent deleted successfully.')

    def find_agent(self):
        agent_id = input('Agent ID to find: ')
        if not agent_id.isdigit():
            print('Invalid ID.')
            return
        agent = self.manager.find_agent_by_id(int(agent_id))
        if agent:
            print(agent)
        else:
            print('Agent not found.')

    def view_all_agents(self):
        agents = self.manager.get_all_agents()
        for agent in agents:
            print(agent)
            print()
