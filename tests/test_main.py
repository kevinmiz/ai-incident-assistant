from app.main import classify_incident, determine_severity


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
