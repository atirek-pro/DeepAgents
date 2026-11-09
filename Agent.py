import os
from pathlib import Path
from dotenv import load_dotenv

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR
REQUIREMENTS_DIR = ROOT_DIR / "requirements"
OUTPUT_DIR = ROOT_DIR / "output"

# Ensure required directories exist
if not REQUIREMENTS_DIR.is_dir():
    raise FileNotFoundError(
        f"Requirements directory not found: {REQUIREMENTS_DIR}"
    )

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DRAFT_PATH = OUTPUT_DIR / "analysis_draft.md"


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

Use the filesystem tools to retrieve requirement documents,
read and edit files, and generate analysis reports.

Follow the defined analysis workflow and adhere strictly to the
provided instructions.

Your task is complete only when the analysis has been successfully
generated and saved to the required output file.
"""


agent = create_deep_agent(
    model=llm,
    system_prompt=system_prompt,
    backend=FilesystemBackend(root_dir=ROOT_DIR, virtual_mode=True),
    memory=["./Agents.md"]
)

# Generate agent graph
graph = agent.get_graph()

# Save graph as PNG
png_data = graph.draw_mermaid_png()
output_path = Path(__file__).resolve().parent / "agent_with_FileSystemBackend.png"
output_path.write_bytes(png_data)
print(f"Agent graph saved at: {output_path}")

# Get requirement ID from user
req_id = input("Enter Requirement ID: ").strip()

if not req_id:
    raise ValueError("Requirement ID cannot be empty.")

# Prevent directory traversal
if Path(req_id).name != req_id or req_id in {".", ".."}:
    raise ValueError("Invalid requirement ID.")

requirement_path = f"requirements/{req_id}.txt"

# Define the user request
content = f"""
Review the requirement document associated with Req_id: {req_id}.

Requirement document:
{requirement_path}

Follow the complete procedure and review guidance defined in your
persistent memory (Agents.md).

Execution instructions:

1. Read the requirement document:
   {requirement_path}

2. Analyze the requirement according to the defined analysis workflow.

3. Write the analysis to create the analysis draft.

4. The output filename MUST be exactly:
   output/analysis_draft.md

5. If revisions are required, then edit the file
   to update the existing draft.

6. Ensure the complete analysis is saved successfully before
   considering the task complete.

Do not create alternative report filenames.
"""

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ]
    }
)

# DISPLAY FINAL RESPONSE
print("\nFinal Response:\n")
print(response["messages"][-1].content)

# DISPLAY GENERATED FILES
print("\nResponse Files:\n")
print(response.get("files", {}))

# VERIFY DRAFT CREATION
if DRAFT_PATH.is_file():

    print("\nAnalysis draft successfully generated:")
    print(DRAFT_PATH)

else:

    print("\nWARNING: Analysis draft was not found.")
    print(f"Expected location: {DRAFT_PATH}")