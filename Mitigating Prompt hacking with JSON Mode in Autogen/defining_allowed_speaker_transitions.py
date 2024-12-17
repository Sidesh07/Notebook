allowed_transitions = {
    proxy_agent: [IO_Agent],
    IO_Agent: [friendly_agent, suspicious_agent],
    suspicious_agent: [proxy_agent],
    friendly_agent: [proxy_agent],
}