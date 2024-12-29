import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read the YAML file as a string
with open("browserstack_template.yml", "r") as file:
    content = file.read()

# Replace placeholders with environment variables
content = content.replace("${BROWSERSTACK_USERNAME}", os.getenv("BROWSERSTACK_USERNAME", ""))
content = content.replace("${BROWSERSTACK_ACCESS_KEY}", os.getenv("BROWSERSTACK_ACCESS_KEY", ""))

# Write the updated YAML back to a file or use it directly
with open("browserstack.yml", "w") as file:
    file.write(content)

print("Updated browserstack.yml written to browserstack_resolved.yml")