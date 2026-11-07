from pathlib import Path
from langchain.tools import tool

# Resolve requirements directory relative to this Python file
REQUIREMENTS_DIR = Path(__file__).resolve().parent / "requirements"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

@tool
def fetch_requirement(req_id: str) -> str:
    """
    Fetch the requirement details from a text file using its Req_id.

    Args:
        req_id: Unique requirement ID, e.g. REQ001.

    Returns:
        Complete requirement content if found.
    """

    # Prevent invalid filenames and directory traversal
    if not req_id or not req_id.strip():
        return "Error: Requirement ID cannot be empty."

    req_id = req_id.strip()

    if Path(req_id).name != req_id or req_id in {".", ".."}:
        return "Error: Invalid requirement ID."

    # Construct file path
    file_path = REQUIREMENTS_DIR / f"{req_id}.txt"

    # Check whether file exists
    if not file_path.is_file():
        return f"Requirement with ID '{req_id}' was not found."

    try:
        # Read requirement content
        content = file_path.read_text(encoding="utf-8")

        if not content.strip():
            return f"Requirement file '{req_id}' is empty."

        return content

    except OSError as e:
        return f"Error reading requirement file: {str(e)}"


@tool
def write_file(file_name: str, content: str) -> str:
    """
    Create a new file or overwrite an existing file with the provided content.

    Args:
        file_name: Name of the file to create, e.g. analysis.md.
        content: Content to write into the file.

    Returns:
        Success or error message.
    """

    if not file_name or not file_name.strip():
        return "Error: File name cannot be empty."

    file_name = file_name.strip()

    # Prevent directory traversal and restrict writing to output directory
    if Path(file_name).name != file_name or file_name in {".", ".."}:
        return "Error: Invalid file name. Only filenames are allowed."

    if not content or not content.strip():
        return "Error: File content cannot be empty."

    try:
        # Create output directory if it doesn't exist
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        file_path = OUTPUT_DIR / file_name

        # Create or overwrite the file
        file_path.write_text(content, encoding="utf-8")

        return (
            f"File successfully written: {file_path}\n"
            f"Characters written: {len(content)}"
        )

    except OSError as e:
        return f"Error writing file: {str(e)}"

@tool
def edit_file(
    file_name: str,
    old_string: str,
    new_string: str
) -> str:
    """
    Make an exact string replacement inside an existing file.

    Args:
        file_name: Name of the file to edit, e.g. analysis.md.
        old_string: Exact existing text to replace.
        new_string: New content that will replace the existing text.

    Returns:
        Success or error message.
    """

    if not file_name or not file_name.strip():
        return "Error: File name cannot be empty."

    file_name = file_name.strip()

    # Restrict operations to filenames inside OUTPUT_DIR
    if Path(file_name).name != file_name or file_name in {".", ".."}:
        return "Error: Invalid file name."

    if not old_string:
        return "Error: Old string cannot be empty."

    file_path = OUTPUT_DIR / file_name

    if not file_path.is_file():
        return f"Error: File '{file_name}' does not exist."

    try:
        # Read existing file content
        content = file_path.read_text(encoding="utf-8")

        # Ensure exact match exists
        occurrences = content.count(old_string)

        if occurrences == 0:
            return (
                f"Error: The specified text was not found "
                f"in '{file_name}'. No changes made."
            )

        if occurrences > 1:
            return (
                f"Error: Found {occurrences} occurrences of the "
                f"specified text. Please provide a more specific "
                f"string to avoid unintended replacements."
            )

        # Perform exact replacement
        updated_content = content.replace(
            old_string,
            new_string,
            1
        )

        # Write updated content back
        file_path.write_text(
            updated_content,
            encoding="utf-8"
        )

        return (
            f"Successfully updated '{file_name}'.\n"
            f"Replaced {len(old_string)} characters "
            f"with {len(new_string)} characters."
        )

    except OSError as e:
        return f"Error editing file: {str(e)}"