"""Employee Onboarding Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_provision_new_hire():
    """Test Provision accounts, access, and equipment for a new hire."""
    tools = AgentTools()
    result = await tools.provision_new_hire(employee_id="test", role="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_create_onboarding_plan():
    """Test Create a personalized onboarding plan based on role and department."""
    tools = AgentTools()
    result = await tools.create_onboarding_plan(employee_id="test", role="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_progress():
    """Test Track onboarding milestone completion for an employee."""
    tools = AgentTools()
    result = await tools.track_progress(employee_id="test", include_overdue=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_verify_compliance():
    """Test Verify completion of required employment documents and training."""
    tools = AgentTools()
    result = await tools.verify_compliance(employee_id="test", requirements="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.employee_onboarding_agent_agent import EmployeeOnboardingAgentAgent
    agent = EmployeeOnboardingAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
