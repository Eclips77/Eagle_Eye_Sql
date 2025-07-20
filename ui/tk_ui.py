import tkinter as tk

from Dal.agent_dal import AgentDAL
from Dal.agent_manager import AgentManager
from models.agent import Agent, AgentStatus


class TkUI:
    """Tkinter based user interface."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Agent Control Center")
        self.manager = AgentManager(AgentDAL())
        self._build_widgets()

    def _build_widgets(self):
        root = self.root
        tk.Label(root, text="Code Name").grid(row=0, column=0, sticky="e")
        self.code_entry = tk.Entry(root)
        self.code_entry.grid(row=0, column=1)

        tk.Label(root, text="Real Name").grid(row=1, column=0, sticky="e")
        self.real_entry = tk.Entry(root)
        self.real_entry.grid(row=1, column=1)

        tk.Label(root, text="Location").grid(row=2, column=0, sticky="e")
        self.location_entry = tk.Entry(root)
        self.location_entry.grid(row=2, column=1)

        tk.Label(root, text="Status").grid(row=3, column=0, sticky="e")
        self.status_var = tk.StringVar(value=AgentStatus.ACTIVE.value)
        status_options = [status.value for status in AgentStatus]
        self.status_menu = tk.OptionMenu(root, self.status_var, *status_options)
        self.status_menu.grid(row=3, column=1)

        tk.Label(root, text="Missions Completed").grid(row=4, column=0, sticky="e")
        self.mission_entry = tk.Entry(root)
        self.mission_entry.grid(row=4, column=1)

        tk.Label(root, text="Agent ID").grid(row=5, column=0, sticky="e")
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=5, column=1)

        self.add_btn = tk.Button(root, text="Add Agent", command=self.add_agent)
        self.add_btn.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.update_btn = tk.Button(root, text="Update Agent", command=self.update_agent)
        self.update_btn.grid(row=7, column=0, columnspan=2, sticky="ew")

        self.delete_btn = tk.Button(root, text="Delete Agent", command=self.delete_agent)
        self.delete_btn.grid(row=8, column=0, columnspan=2, sticky="ew")

        self.find_btn = tk.Button(root, text="Find Agent", command=self.find_agent)
        self.find_btn.grid(row=9, column=0, columnspan=2, sticky="ew")

        self.view_btn = tk.Button(root, text="View All Agents", command=self.view_all_agents)
        self.view_btn.grid(row=10, column=0, columnspan=2, sticky="ew")

        self.output = tk.Text(root, height=15, width=60)
        self.output.grid(row=11, column=0, columnspan=2, pady=10)

    def clear_inputs(self):
        self.code_entry.delete(0, tk.END)
        self.real_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.mission_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)

    def add_agent(self):
        try:
            status = AgentStatus(self.status_var.get())
            missions = int(self.mission_entry.get() or 0)
            self.manager.add_agent(
                self.code_entry.get(),
                self.real_entry.get(),
                self.location_entry.get(),
                status,
                missions,
            )
            self.output.insert(tk.END, "Agent added successfully.\n")
            self.clear_inputs()
        except ValueError as ex:
            self.output.insert(tk.END, f"Error adding agent: {ex}\n")

    def update_agent(self):
        agent_id = self.id_entry.get()
        if not agent_id.isdigit():
            self.output.insert(tk.END, "Invalid ID for update.\n")
            return

        try:
            status = AgentStatus(self.status_var.get())
            missions = int(self.mission_entry.get() or 0)
            agent = Agent(
                self.code_entry.get(),
                self.real_entry.get(),
                self.location_entry.get(),
                status,
                missions,
            )
            self.manager.update_agent(int(agent_id), agent)
            self.output.insert(tk.END, f"Agent {agent_id} updated.\n")
            self.clear_inputs()
        except ValueError as ex:
            self.output.insert(tk.END, f"Error updating agent: {ex}\n")

    def delete_agent(self):
        agent_id = self.id_entry.get()
        if not agent_id.isdigit():
            self.output.insert(tk.END, "Invalid ID for deletion.\n")
            return
        self.manager.delete_agent(int(agent_id))
        self.output.insert(tk.END, f"Agent {agent_id} deleted.\n")
        self.clear_inputs()

    def find_agent(self):
        agent_id = self.id_entry.get()
        if not agent_id.isdigit():
            self.output.insert(tk.END, "Invalid ID.\n")
            return
        agent = self.manager.find_agent_by_id(int(agent_id))
        self.output.delete("1.0", tk.END)
        if agent:
            self.output.insert(tk.END, str(agent) + "\n")
        else:
            self.output.insert(tk.END, "Agent not found.\n")

    def view_all_agents(self):
        agents = self.manager.get_all_agents()
        self.output.delete("1.0", tk.END)
        for agent in agents:
            self.output.insert(tk.END, str(agent) + "\n\n")

    def run(self):
        self.root.mainloop()
