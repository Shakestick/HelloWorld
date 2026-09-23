
import sys
from abc import ABC, abstractmethod

class agent_name(ABC):
    def __init__(self, name="Mango", issue_type="general request"):
        self.name = name
        self.issue_type = issue_type

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_issue_type(self):
        pass

    @abstractmethod
    def welcome_message(self):
        pass


class HelpdeskAgent(agent_name):
    def get_name(self):
        return self.name

    def get_issue_type(self):
        return self.issue_type

    def welcome_message(self):
        return (
            f"Welcome to helpdesk! My name is {self.name}. "
            f"How can I help you with your {self.issue_type} today?"
        )


agent = HelpdeskAgent(
    sys.argv[1] if len(sys.argv) > 1 else "Mango",
    sys.argv[2] if len(sys.argv) > 2 else "general request",
)

print(agent.welcome_message())