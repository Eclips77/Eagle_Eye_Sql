from mysql.connector import connect, Error
from Module.agent import Agent, AgentStatus


class AgentDAL:
    def __init__(self):
        self.connection = self.get_connection()

    def get_connection(self):
        try:
            return connect(
                host="localhost",
                user="root",
                password="",
                database="eagleeyedb"
            )
        except Error as e:
            print(f"Connection failed: {e}")
            return None

    def get_all_agents(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM agents")
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as ex:
            print(f"error in get agents {ex}")

    def add_agent_to_db(self, agent):
        try:
            cursor = self.connection.cursor()
            sql = """
            INSERT INTO agents (codeName, realName, location, status, missionCompleted)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                agent.code_name,
                agent.real_name,
                agent.cur_location,
                agent.status.value,
                agent.mission_completed
            )
            cursor.execute(sql, values)
            self.connection.commit()
            print("Agent added to DB successfully.")
        except Exception as ex:
            print(f"Error adding agent: {ex}")
        finally:
            cursor.close()

    def get_agent_by_id(self, id):
        if self.connection is None:
            print("No database connection.")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM agents WHERE id = %s", (id,))
            row = cursor.fetchone()
            cursor.close()

            if row:
                agent = Agent(
                    code_name=row[1],
                    real_name=row[2],
                    cur_location=row[3],
                    status=AgentStatus(row[4]),
                    mission_completed_n=row[5]
                )
                return agent
            else:
                print(f"No agent found with ID {id}")
                return None

        except Error as e:
            print(f"Error retrieving agent with id {id}: {e}")
            return None


dal = AgentDAL()
agent1 = dal.get_agent_by_id(20)
print(agent1)
