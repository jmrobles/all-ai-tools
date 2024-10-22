from fastapi.testclient import TestClient
from app.main import app 
from app.schemas.tool import ToolCreate
from app.core.config import settings


client = TestClient(app)

def test_index_documents_happy_path():
    # Test data
    tools = [
        ToolCreate(
            name="npcsh",
            description="A library for interacting with AI agents, supporting voice chat and image processing.",
            url="https://github.com/cagostino/npcsh",
            categories=["voice", "image"],
            dt=1728745861101,
            hash="ed75f282213f6fdd0c4383c6429cb261",
            scrapped="Welcome to npcsh, the shell for interacting with NPCs (LLM-powered AI agents) and for coordinating actions and information between the NPCs. npcsh is meant to be a drop-in replacement shell for any kind of bash/zsh/powershell and allows the user to directly operate their machine through the use of the LLM-powered shell. npcsh introduces a new paradigm of programming for LLMs: npcsh allows users to set up NPC profiles (a la npc_profile.npc) where a user sets the primary directive of the NPC, the tools they want the NPC to use, and other properties of the NPC. NPCs can interact with each other and their primary directives and properties make these relationships explicit through jinja references.",
            use_cases=[
                "Creating and managing LLM-powered NPCs for interactive applications.",
                "Developing a new programming paradigm for LLMs that allows for user-defined NPC profiles.",
                "Coordinating actions and information between multiple NPCs in a collaborative environment.",
                "Providing a user-friendly shell interface for operating machines through LLMs.",
                "Facilitating the customization of NPC behaviors and interactions based on user-defined directives.",
                "Enabling the integration of various tools and functionalities within NPC profiles."
            ],
            latest_scrap=1729438970525,
            validated=True
        )
    ]

    # Get a valid token (you'll need to implement this based on your authentication system)
    valid_token = get_valid_token()

    # Make the request
    response = client.post("/api/index", json=[tool.model_dump() for tool in tools], headers={"Authorization": f"Bearer {valid_token}"})

    # Assert the response
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "success"
    assert response_data["message"] == "1 tools indexed successfully"
    assert len(response_data["tools"]) == 1

    # Assert the indexed tool data
    indexed_tool = response_data["tools"][0]
    assert indexed_tool["name"] == "npcsh"
    assert indexed_tool["description"] == "A library for interacting with AI agents, supporting voice chat and image processing."
    assert indexed_tool["url"] == "https://github.com/cagostino/npcsh"
    assert indexed_tool["categories"] == ["voice", "image"]
    assert indexed_tool["dt"] == 1728745861101
    assert indexed_tool["hash"] == "ed75f282213f6fdd0c4383c6429cb261"
    assert "scrapped" in indexed_tool
    assert len(indexed_tool["use_cases"]) == 6
    assert indexed_tool["latest_scrap"] == 1729438970525
    assert indexed_tool["validated"] == True

def get_valid_token():
    return settings.API_TOKEN

