from enum import Enum

class AgentStatus(Enum):
    ACTIVE = "Active"
    INJURED = "Injured"
    MISSING = "Missing"
    RETIRED = "Retired"

class Agent:
    def __init__(self, code_name, real_name, cur_location, status: AgentStatus, mission_completed_n):
        if not isinstance(status, AgentStatus):
            raise ValueError(f"Invalid status: {status}")
        self.code_name = code_name
        self.real_name = real_name
        self.cur_location = cur_location
        self.status = status
        self.mission_completed = mission_completed_n

    def __str__(self):
        return (f"Agent {self.code_name} ({self.real_name})\n"
                f"Location: {self.cur_location}\n"
                f"Status: {self.status.value}\n"
                f"Missions Completed: {self.mission_completed}")

# agent = Agent("Shadow", "Yaakov B.A", "Tel Aviv", AgentStatus.ACTIVE, 7)
# print(agent)
