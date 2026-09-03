# AI Incident Assistant

AI Incident Assistant is a simple Python-based incident triage tool that helps analyze application incidents using rule-based classification, log parsing, and Gemini AI.

The project is designed as a lightweight simulation of an IT Operations / Application Support incident investigation workflow.

## Features

- Incident category classification
- Incident severity determination
- Application log parsing
- Automatic error log detection
- AI-assisted incident analysis using Gemini
- Docker container support
- Unit testing with pytest
- CI testing using GitHub Actions
- Incident storage in Elasticsearch
- Incident exploration using Kibana
- Environment-based Elasticsearch configuration
- Docker network support for application-to-Elasticsearch communication

## Incident Analysis Flow

1. User describes an incident
2. Application determines incident category
3. Application determines severity
4. User selects a sample log file
5. Application extracts ERROR logs
6. Incident metadata and parsed errors are stored in Elasticsearch
7. Incident details and log evidence are sent to Gemini
8. Gemini generates:
   - Incident summary
   - Impact analysis
   - Possible root cause
   - Investigation steps
   - Recommended actions
   - Escalation recommendation

## Project Structure

```text
ai-incident-assistant/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── log_parser.py
│   ├── ai_analyzer.py
│   ├── elasticsearch_client.py
│   └── check_gemini.py
├── sample_logs/
├── tests/
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Technologies

- Python 3.14
- Google Gemini API
- Elasticsearch
- Kibana
- Docker
- Docker Compose
- pytest
- Git
- GitHub
- GitHub Actions

## Running Locally

Create and activate a Python virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key
```

Run the application:

```bash
python -m app.main
```

## Running with Docker

Build the Docker image:

```bash
docker build -t ai-incident-assistant .
```

Run the container:

```bash
docker run --rm -it --env-file .env ai-incident-assistant
```

The `.env` file is provided only at runtime and is not stored inside the Docker image.

## Running Tests

Run unit tests locally:

```bash
python -m pytest -v
```

Tests are also executed automatically by GitHub Actions when changes are submitted through a pull request.

## Example Incident

```text
Payment API timeout causing transactions to fail
```

Example classification:

```text
Category : Payment Service
Severity : SEV-2
```

The application then analyzes the selected error logs and sends the available incident evidence to Gemini for further investigation recommendations.

## Security

Sensitive configuration such as the Gemini API key is stored in `.env`.

The `.env` file is excluded from:

- Git using `.gitignore`
- Docker build context using `.dockerignore`

API credentials should never be committed to the repository or stored directly inside the Docker image.

## Project Goal

This project is a lightweight incident analysis simulation designed to demonstrate:

- incident triage
- log investigation
- AI-assisted analysis
- observability
- containerization
- automated testing
- environment-based configuration

The application assists an operator during incident investigation. It does not automatically perform production remediation actions.

## Observability with Elasticsearch and Kibana

The application stores incident metadata and parsed error logs in Elasticsearch for centralized incident tracking and analysis.

Kibana is used to explore indexed incident data through the `incidents` index.

### Observability Flow

```text
Incident Input
      ↓
Rule-based Classification
      ↓
Severity Determination
      ↓
Log Parsing
      ↓
Elasticsearch
      ↓
Kibana
      ↓
Gemini AI Analysis
```

Elasticsearch and Kibana are provided using Docker Compose.

```bash
docker compose up -d
```

Available services:

Elasticsearch: `http://localhost:9200`
Kibana: `http://localhost:5601`

For local Python execution, the application uses:

```text
http://localhost:9200
```

For Docker network communication, the Elasticsearch URL can be configured using:
```text
ELASTICSEARCH_URL=http://elasticsearch:9200
```

If ELASTICSEARCH_URL is not configured, the application defaults to:
```text
http://localhost:9200
```

Example Docker execution:

```bash
docker run --rm -it \
  --network ai-incident-assistant_default \
  --env-file .env \
  -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
  ai-incident-assistant
```

Elasticsearch security is disabled in the Docker Compose configuration for local development and demonstration purposes only.
