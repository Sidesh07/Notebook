groupchat = GroupChat(
    agents=(IO_Agent, friendly_agent, suspicious_agent, proxy_agent),
    messages=[],
    allowed_or_disallowed_speaker_transitions=allowed_transitions,
    speaker_transitions_type="allowed",
    max_round=10,
)

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    llm_config=manager_config,
)

chat_result = proxy_agent.initiate_chat(manager, message=task)