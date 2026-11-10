import os
from pathlib import Path
from dotenv import load_dotenv

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend

from langgraph.checkpoint.memory import MemorySaver
from deepagents.backends.utils import create_file_data
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR

REQUIREMENTS_DIR = ROOT_DIR / "requirements"
OUTPUT_DIR = ROOT_DIR / "output"
SKILLS_DIR = ROOT_DIR / "skills"
MEMORY_FILE = ROOT_DIR / "Agents.md"

# Ensure required directories exist
if not REQUIREMENTS_DIR.is_dir():
    raise FileNotFoundError(
        f"Requirements directory not found: {REQUIREMENTS_DIR}"
    )

if not MEMORY_FILE.is_file():
    raise FileNotFoundError(
        f"Memory instructions not found: {MEMORY_FILE}"
    )

SKILL_FILE = (
    SKILLS_DIR
    / "requirement-analyst-skill"
    / "SKILL.md"
)

if not SKILL_FILE.is_file():
    raise FileNotFoundError(
        f"Requirement analysis skill not found: {SKILL_FILE}"
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

Your responsibility is to analyze requirements accurately and
produce complete, structured, evidence-based analysis reports.

## Instructions and Skills

1. Read and follow the persistent instructions in Agents.md.
   These define your general operating rules.

2. Discover and evaluate the available skills exposed through
   the DeepAgents skill system for every new task.

3. Compare each available skill's name and description with
   the current task. When a skill is relevant, load its complete
   SKILL.md instructions before performing the task.

4. Apply all relevant skill instructions throughout execution.
   Do not skip a relevant skill merely because the task appears
   straightforward or the general instructions seem sufficient.

5. If multiple skills are relevant, use all applicable skills
   and reconcile any conflicting instructions with Agents.md
   and the user's explicit requirements.

6. Do not claim that a skill was used unless its instructions
   were actually made available to you.

## Filesystem and Execution

- Use the filesystem tools to inspect, read, write, and edit files.
- Read the requirement document before analyzing it.
- Follow the applicable analysis workflow and report template.
- Separate confirmed facts, ambiguities, clarification questions,
  assumptions, and recommendations.
- Never present an assumption as a confirmed requirement.
- Do not invent stakeholder decisions or requirements.
- Save the final report to the exact output path requested.
- Read back and validate the completed report before finishing.
- Correct any issues discovered during validation.

The task is complete only after the report has been saved and
its contents have been verified against the applicable instructions.
"""



agent = create_deep_agent(
    model=llm,
    system_prompt=system_prompt,
    backend=FilesystemBackend(root_dir=ROOT_DIR, virtual_mode=True),
    memory=["Agents.md"],
    skills=["/skills/"],
    checkpointer=MemorySaver()
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

requirement_file = REQUIREMENTS_DIR / f"{req_id}.txt"

if not requirement_file.is_file():
    raise FileNotFoundError(
        f"Requirement document not found: {requirement_file}"
    )

requirement_path = f"requirements/{req_id}.txt"
output_path = "output/analysis_draft.md"

# Define the user request
content = f"""
Review the requirement document associated with Req_id: {req_id}.

Requirement document: {requirement_path}
Required output file: {output_path}

Discover and activate all relevant available skills before
performing the analysis. Follow Agents.md and the instructions
of every relevant skill.

Read the complete requirement document, analyze it, and save
the report to exactly {output_path}.

Verify the saved report against the applicable instructions.
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
    },
    config={"configurable": {"thread_id": "demo-1"}}
)

for m in response["messages"]:
    m.pretty_print()

# DISPLAY FINAL RESPONSE
# print("\nFinal Response:\n")
# print(response["messages"][-1].content)

# # DISPLAY GENERATED FILES
# print("\nResponse Files:\n")
# print(response.get("files", {}))

# # VERIFY DRAFT CREATION
# if DRAFT_PATH.is_file():

#     print("\nAnalysis draft successfully generated:")
#     print(DRAFT_PATH)

# else:

#     print("\nWARNING: Analysis draft was not found.")
#     print(f"Expected location: {DRAFT_PATH}")