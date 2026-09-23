agent_name = sys.argv[1] if len(sys.argv) > 1 else "Mango"

issue_type = sys.argv[2] if len(sys.argv) > 2 else "general request"

print(f"Welcome to helpdesk! My name is {agent_name}. How can I help you with your {issue_type} today?")