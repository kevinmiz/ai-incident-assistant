from datetime import datetime, timezone
from elasticsearch import Elasticsearch


def save_incident(incident, category, severity, errors):
    client = Elasticsearch("http://localhost:9200")

    document = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "incident": incident,
        "category": category,
        "severity": severity,
        "errors": errors
    }

    response = client.index(
        index="incidents",
        document=document
    )

    return response["result"]
