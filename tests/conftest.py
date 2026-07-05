"""Test configuration for Employee Onboarding Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "employee-onboarding-agent", "category": "Human Resources"}
