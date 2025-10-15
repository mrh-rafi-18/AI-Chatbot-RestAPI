from app.services.product_service import get_tools
from langchain_groq import ChatGroq

tools= get_tools()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5,
    max_tokens=1024
)

def fetch_the_information_from_api(query: str):


    model_with_tools = llm.bind_tools(tools)

    messages=[
                {
                    "role": "system",
                    "content": """You are a Helpful AI agent provided with tools to fetch information 
                                from a products API. Watch user query carefully and find the proper arguments and
                                call the correct tool to get the information. use the keywords in the user query to
                                find the correct tool to call. If the user query contains multiple conditions,
                                """
                },
                {
                    "role": "user",
                    "content": query
                }
        ]
    response = model_with_tools.invoke(messages)

    try:
        tool_name = response.tool_calls[0]["name"]
        tool_args = response.tool_calls[0].get("args", {})

        tool_to_call = next((t for t in tools if t.name == tool_name), None)
    
        result = tool_to_call.invoke(tool_args)
        
        return result
    except Exception as e:
        result = {"Fetching information from api failed": str(e)}
        return result


def json_to_human_readable_text(json_data: dict) -> str:
        json_data = str(json_data)
        messages=[
                        {
                            "role": "system",
                            "content": """You are a Helpful AI assistant that converts JSON data
                                        into a human-readable text format providing exact information
                                        without missing any details. Now convert the following user provided JSON data to text:
                                            
                                        """
                        },
                        {
                            "role": "user",
                            "content": json_data
                        }
                    ]
    
        response = llm.invoke(messages)
        return response.content



def generate_chatbot_response(user_message: str) -> str:
    api_data=fetch_the_information_from_api(user_message)
    context= json_to_human_readable_text(api_data)
    messages=[
                {
                    "role": "system",
                    "content": f"""You are a helpful AI assistant. Answer user questions accurately and concisely using the provided context.
                                If the context doesn’t include the answer, reply politely with:

                                “No, we don’t have any information like that.”

                                Do not mention or refer to the context itself — the user doesn’t know it exists.
                                Avoid hallucination and focus only on relevant, useful details.

                                keep short, precise and relevant answers.
                                
                                
                                context: {context}
                                """
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]    


    response = llm.invoke(messages)
    return response.content

