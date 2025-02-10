from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("API_KEY")

client=MiraClient(config={"API_KEY":api_key})
flow=Flow(source="flow.yaml")
try:
    client.flow.deploy(flow)
except FlowError as e:
    print(f"Error occured:{str(e)}")