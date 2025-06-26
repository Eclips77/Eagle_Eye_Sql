from Dal.agent_dal import AgentDAL
from models.agent import Agent, AgentStatus

class AgentManager:
    def __init__(self, dal):
        self.dal = dal

    def view_all_agents(self):
        rows = self.dal.get_all_agents()
        agents = [Agent.from_tuple(row) for row in rows]
        for agent in agents:
            print(agent)

    def add_agent(self, code_name, real_name, location, status, missions):
        agent = Agent(code_name, real_name, location, status, missions)
        self.dal.add_agent_to_db(agent)

    def find_agent_by_id(self, id):
        row = self.dal.get_agent_by_id(id)
        if row:
            print(Agent.from_tuple(row))
        else:
            print("Agent not found.")

    def update_agent(self, id, updated_agent):
        self.dal.update_agent_by_id(id, updated_agent)

    def delete_agent(self, id):
        self.dal.delete_agent_by_id(id)

