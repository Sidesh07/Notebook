import autogen
from autogen.agentchat import UserProxyAgent
from autogen.agentchat.assistant_agent import AssistantAgent
from autogen.agentchat.groupchat import GroupChat

# Define the llm_config and manager_config dictionaries properly
llm_config = {
    "timeout": 600,
    "cache_seed": 45,  # change the seed for different trials
    "config_list": autogen.config_list_from_json(
        r"Notebooks\Mitigating Prompt hacking with JSON Mode in Autogen\OAI_CONFIG_LIST.json",
        filter_dict={"model": ["gpt-4-0125-preview"]},  # This Config is set to JSON mode
    ),
    "temperature": 0,
}

manager_config = {
    "timeout": 600,
    "cache_seed": 44,  # change the seed for different trials
    "config_list": autogen.config_list_from_json(
        r"Notebooks\Mitigating Prompt hacking with JSON Mode in Autogen\OAI_CONFIG_LIST.json",
        filter_dict={"model": ["gpt-4-turbo-preview"]},  # This Config is set to Text mode
    ),
    "temperature": 0,
}

print(autogen.__version__)
