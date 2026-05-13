from ai import chat
from langchain_core.messages import HumanMessage , SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

def connect_with_ai(system_prompt: str , user_prompt: str , response_class):
    parser = JsonOutputParser(pydantic_object=response_class)
    prompt_template = PromptTemplate(
    template="{user_prompt}\n\n{format_instructions}",
    input_variables=["user_prompt"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    messages = [
    SystemMessage(content=f'''{system_prompt}
    - Output must have schema of the response Schema : {response_class.model_json_schema()}'''),
     HumanMessage(content=prompt_template.format(user_prompt= user_prompt))
    ]
    response = chat.invoke(messages)
    return parser.parse(response.content)
