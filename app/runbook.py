def get_runbook(category):
    runbooks = {
        "Payment Service": [
            "Check payment service availability",
            "Review payment API error logs",
            "Check connectivity to payment dependencies",
            "Verify recent deployment or configuration changes",
            "Escalate to Payment/Application team if the issue persists"
        ],
        "Database": [
            "Check database service availability",
            "Review slow-running queries",
            "Check active database connections",
            "Check CPU, memory, and disk utilization",
            "Review blocking or locked sessions",
            "Escalate to DBA if the issue persists"
        ],
        "Network": [
            "Check network connectivity",
            "Verify DNS resolution",
            "Check application port connectivity",
            "Review firewall or routing changes",
            "Escalate to Network team if the issue persists"
        ],
        "Infrastructure": [
            "Check server availability",
            "Check CPU and memory utilization",
            "Check disk usage",
            "Review system and application logs",
            "Escalate to Infrastructure team if the issue persists"
        ],
        "Application": [
            "Check application service status",
            "Review application error logs",
            "Verify recent deployment or configuration changes",
            "Check dependent services",
            "Escalate to Application team if the issue persists"
        ]
    }

    return runbooks.get(
        category,
        ["Review incident logs and escalate to the appropriate support team"]
    )
