from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("API_KEY")

client=MiraClient(config={"API_KEY":api_key})

flow=Flow(source="flow.yaml")

input_dict={"algorithm":"Check whether a number is prime", "language":"Java"}

response=client.flow.test(flow,input_dict)

print(response)
