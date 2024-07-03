# from promptflow import tool
# from promptflow.connections import CustomConnection

# promptflow/src/promptflow-tools/promptflow/tools/aoai_gpt4v.py
from typing import List, Dict

# Following imports and functions are defined in the lastest promptflow source repo. But, it's not available in the promptflow-tools==1.4.0.
# It must be checked with dependencies and/or versions of tools packages on Azure AI Studio.
# from promptflow.tools.common import handle_openai_error, build_messages, \
#     preprocess_template_string, find_referenced_image_set, convert_to_chat_list, init_azure_openai_client, \
#     post_process_chat_api_response, list_deployment_connections, build_deployment_dict
from promptflow.tools.common import render_jinja_template, handle_openai_error, parse_chat, \
    preprocess_template_string, find_referenced_image_set, convert_to_chat_list, init_azure_openai_client, \
    post_process_chat_api_response, list_deployment_connections, build_deployment_dict

from promptflow._internal import ToolProvider, tool
from promptflow.connections import AzureOpenAIConnection
from promptflow.contracts.types import PromptTemplate

# List of GPT models and versions support image capabilities
GPT4V_VERSION="vision-preview"
GPT4T_VERSION="turbo-2024-04-09"
GPT4o_VERSION="2024-05-13"

def list_deployment_names(
    subscription_id=None,
    resource_group_name=None,
    workspace_name=None,
    connection=""
) -> List[Dict[str, str]]:
    res = []
    deployment_collection = list_deployment_connections(subscription_id, resource_group_name, workspace_name,
                                                        connection)
    if not deployment_collection:
        return res

    for item in deployment_collection:
        deployment = build_deployment_dict(item)
        if deployment.version in [GPT4V_VERSION, GPT4T_VERSION, GPT4o_VERSION]:
            cur_item = {
                "value": deployment.name,
                "display_value": deployment.name,
            }
            res.append(cur_item)

    return res


class AzureOpenAIMM(ToolProvider):
    def __init__(self, connection: AzureOpenAIConnection):
        super().__init__()
        self._client = init_azure_openai_client(connection)

    @tool(streaming_option_parameter="stream")
    @handle_openai_error()
    def chat(
        self,
        prompt: PromptTemplate,
        deployment_name: str,
        temperature: float = 1.0,
        top_p: float = 1.0,
        # stream is a hidden to the end user, it is only supposed to be set by the executor.
        stream: bool = False,
        stop: list = None,
        max_tokens: int = None,
        presence_penalty: float = 0,
        frequency_penalty: float = 0,
        seed: int = None,
        # detail: str = 'auto',
        **kwargs,
    ) -> str:
        prompt = preprocess_template_string(prompt)
        referenced_images = find_referenced_image_set(kwargs)

        # convert list type into ChatInputList type
        converted_kwargs = convert_to_chat_list(kwargs)
        # Code fragments from promptflow-tools > 1.4.0
        # messages = build_messages(prompt=prompt, images=list(referenced_images), detail=detail, **converted_kwargs)
        # code fragments from promptflow-tools==1.4.0
        chat_str = render_jinja_template(prompt, trim_blocks=True, keep_trailing_newline=True, **converted_kwargs)
        messages = parse_chat(chat_str, list(referenced_images))
        headers = {
            "Content-Type": "application/json",
            "ms-azure-ai-promptflow-called-from": "aoai-gpt4v-tool"
        }

        params = {
            "messages": messages,
            "temperature": temperature,
            "top_p": top_p,
            "n": 1,
            "stream": stream,
            "presence_penalty": presence_penalty,
            "frequency_penalty": frequency_penalty,
            "extra_headers": headers,
            "model": deployment_name,
        }

        if stop:
            params["stop"] = stop
        if max_tokens is not None:
            params["max_tokens"] = max_tokens
        if seed is not None:
            params["seed"] = seed

        # completion = self._client.chat.completions.create(**params)
        # return post_process_chat_api_response(completion, stream)
        completion = self._client.chat.completions.create(**params)
        return post_process_chat_api_response(completion, stream, None)


# @tool
# def chat(connection, input_text):
#     return "Hello " + input_text

# @tool
# def custom_aoai_gpt4mm(connection: CustomConnection, input_text: str) -> str:
#     # Replace with your tool code.
#     # Usually connection contains configs to connect to an API.
#     # Use CustomConnection is a dict. You can use it like: connection.api_key, connection.api_base
#     # Not all tools need a connection. You can remove it if you don't need it.
#     return "Hello " + input_text

