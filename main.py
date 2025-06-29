import tkinter as tk
from Dal.agent_dal import AgentDAL
from Dal.agent_manager import AgentManager
from models.agent import Agent
from tools.validator import Validator

class AgentUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Agent Control Center")
        self.manager = AgentManager(AgentDAL())

        self.view_btn = tk.Button(root, text="View All Agents", command=self.view_all_agents)
        self.view_btn.pack()

        self.output = tk.Text(root, height=20, width=60)
        self.output.pack()

    def view_all_agents(self):
        agents = self.manager.get_all_agents()
        self.output.delete("1.0", tk.END)
        for agent in agents:
            self.output.insert(tk.END, str(agent) + "\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgentUI(root)
    root.mainloop()
