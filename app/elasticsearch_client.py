import os
from datetime import datetime, timezone

from elasticsearch import Elasticsearch


def save_incident(incident, category, severity, errors):
    elasticsearch_url = os.getenv(
        "ELASTICSEARCH_URL",
        "http://localhost:9200"
    )


    client = Elasticsearch(elasticsearch_url)

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
