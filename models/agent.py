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

    @classmethod
    def from_tuple(cls, row):
        if len(row) != 6:
            raise ValueError("Row must have exactly 6 elements")
        return cls(
            code_name=row[1],
            real_name=row[2],
            cur_location=row[3],
            status=AgentStatus(row[4]),
            mission_completed_n=row[5]
        )

    def __str__(self):
        return (f"Code Name: {self.code_name}\n"
            f"Real Name: {self.real_name}\n"
            f"Location: {self.cur_location}\n"
            f"Status: {self.status.value}\n"
            f"Missions Completed: {self.mission_completed}\n"
            "-----------------------------")


