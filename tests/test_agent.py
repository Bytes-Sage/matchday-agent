import pytest
from agent.agent import agent, get_runner

# Simple check to ensure agent is instantiated (or fallback handled)
def test_agent_initialization():
    assert get_runner() is not None
