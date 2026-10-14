
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing import List, Optional

# -------------------- Setup --------------------
load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq",
)


# -------------------- Schema --------------------
class Movie(BaseModel):
    title: str = Field(description="Movie title")
    release_year: Optional[int] = Field(default=None)
    genre: List[str] = Field(default_factory=list)
    director: Optional[str] = Field(default=None)
    cast: List[str] = Field(default_factory=list)
    rating: Optional[float] = Field(default=None)
    summary: str = Field(description="Short movie summary")


parser = PydanticOutputParser(pydantic_object=Movie)


# -------------------- Prompt --------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a movie information extraction assistant.

Extract movie information from the user's paragraph.
Do not invent facts or guess unknown details.

If a field cannot be determined:
- Use null for optional fields.
- Use an empty list for list fields.
- Use a short explanation if the summary cannot be determined.

Return valid JSON matching the required schema.

{format_instructions}
"""
    ),
    ("human", "{paragraph}")
])


# -------------------- Extraction Function --------------------
def extract_movie(paragraph: str) -> Movie:
    final_prompt = prompt.invoke({
        "paragraph": paragraph,
        "format_instructions": parser.get_format_instructions(),
    })

    response = model.invoke(final_prompt)

    return parser.parse(response.content)
