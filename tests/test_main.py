from app.main import classify_incident, determine_severity
from app.runbook import get_runbook


def test_classify_payment_incident():
    result = classify_incident("Payment API timeout")
    assert result == "Payment Service"


def test_classify_database_incident():
    result = classify_incident("Database query failed")
    assert result == "Database"


def test_determine_severity_sev2():
    result = determine_severity("Payment API timeout")
    assert result == "SEV-2"


def test_determine_severity_sev3():
    result = determine_severity("Application response is slow")
    assert result == "SEV-3"


def test_database_runbook():
    runbook = get_runbook("Database")

    assert "Check database service availability" in runbook
    assert "Escalate to DBA if the issue persists" in runbook


def test_network_runbook():
    runbook = get_runbook("Network")

    assert "Check network connectivity" in runbook
    assert "Escalate to Network team if the issue persists" in runbook
