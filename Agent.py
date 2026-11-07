import os
from pathlib import Path
from dotenv import load_dotenv

from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import fetch_requirement, edit_file, write_file

load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

system_prompt = """
You are an AI-powered Requirement Analysis Agent.

Your responsibility is to analyze requirements accurately and produce
complete, structured, and high-quality requirement analysis reports.

Use the instructions provided in your persistent memory (Agents.md)
as the primary source of your operational guidelines.

Follow the defined analysis workflow, use the available tools when
required, and adhere strictly to the rubric evaluation process.

Do not fabricate requirement details or make unsupported assumptions.

Your task is complete only when the analysis has been successfully
generated and saved to the required output file.
"""


agent = create_deep_agent(
    model=llm,
    tools=[
        fetch_requirement,
        edit_file,
        write_file
    ],
    system_prompt=system_prompt,
    memory=["./Agents.md"]
)

# Generate agent graph
graph = agent.get_graph()

# Save graph as PNG
# png_data = graph.draw_mermaid_png()
# output_path = Path(__file__).resolve().parent / "agent.png"
# output_path.write_bytes(png_data)
# print(f"Agent graph saved at: {output_path}")

# Get requirement ID from user
req_id = input("Enter Requirement ID: ").strip()

if not req_id:
    raise ValueError("Requirement ID cannot be empty.")

# Define the user request
content = f"""
Review the requirement document associated with Req_id: {req_id}.

Follow the complete procedure and review guidance defined
in your system instructions.

Execute the review sequentially and save the final report.
"""

response = agent.invoke(
    {
        "messages":[
            {
                "role": "user",
                "content": content
            }
        ]
    }
)

print("Final Response: ", "\n")
print(response["messages"][-1].content)
print("\n")
print("Response Files")
print(response["files"])