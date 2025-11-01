from google import genai
import os
from dotenv import load_dotenv
from google.genai import types

from functions.call_function import call_function

load_dotenv()

function_schemas = [
    {
        "name":"get_files_info",
        "description":"Lists files in the specified directory along with their sizes, constrained to the working directory.",
        "parameter_type":types.Type.OBJECT,
        "properties": {
            "directory":{
                "type" : types.Type.STRING,
                "description" : "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            },
        },
    },
    {
        "name":"get_file_content",
        "description":"Get the content of the file limited to the first 10000 characters, constrained to the working directory.",
        "parameter_type":types.Type.OBJECT,
        "properties": {
            "file_path":{
                "type" : types.Type.STRING,
                "description" : "The file that needs to be read, relative to the working directory.",
            },
        },
    },
    {
        "name":"write_file",
        "description":"Write content to a file path, constrained to the working directory.",
        "parameter_type":types.Type.OBJECT,
        "properties": {
            "file_path":{
                "type" : types.Type.STRING,
                "description" : "The file that needs to be created or edited, overwrites existing content in the file, relative to the working directory.",
            },
            "content":{
                "type" : types.Type.STRING,
                "description" : "The content that needs to be written in the file",
            },
        },
    },
    {
        "name":"run_python_file",
        "description":"Execute a python file, constrained to the working directory, and can only run a python file.",
        "parameter_type":types.Type.OBJECT,
        "properties": {
            "file_path":{
                "type" : types.Type.STRING,
                "description" : "The file that needs to executed, relative to the working directory.",
            },
        },
    },
]

def call_llm(user_prompt="",debug_mode = False):
    system_prompt = system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("MODEL")
    client = genai.Client(api_key=api_key)

    function_declarations= []
    for schema in function_schemas:
        function_declarations.append(define_functions(schema["name"],schema["description"], parameter_type=schema["parameter_type"], properties_dict=schema["properties"]))

    available_functions = types.Tool(
            function_declarations=function_declarations
            )


    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]
    
    result = client.models.generate_content(model=model,contents=messages, config=types.GenerateContentConfig(system_instruction = system_prompt, tools = [available_functions]))
    function_calls = result.function_calls
    if function_calls:
        for function_call in function_calls:
            function_result = call_function(function_call, debug_mode)
            # print(f"Calling function: {function_call.name}({function_call.args})")
            if function_result.parts[0] and function_result.parts[0].function_response.response:
                if debug_mode:
                    print(f"-> {function_result.parts[0].function_response.response}")
            else:
                raise Exception("Invalid function call")

    if (debug_mode):
        prompt_tokens = result.usage_metadata.prompt_token_count
        cand_tokens = result.usage_metadata.candidates_token_count
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {cand_tokens}")


def define_functions(name, description,parameter_type, properties_dict):
    properties = {}
    for property in properties_dict.items():
        properties[property[0]] = types.Schema(
            type=property[1]["type"],
            description=property[1]["description"]
        )
    return types.FunctionDeclaration(
            name=name,
            description=description,
            parameters = types.Schema(
                    type = parameter_type,
                    properties=properties,
                ),
            )
