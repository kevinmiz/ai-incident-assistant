from log_parser import read_log_file, find_errors
from ai_analyzer import build_incident_prompt, analyze_with_ai



def classify_incident(incident):
    incident = incident.lower()

    if "payment" in incident:
        return "Payment Service"

    if "database" in incident or "sql" in incident:
        return "Database"

    if "network" in incident or "connection" in incident:
        return "Network"

    if "server" in incident or "cpu" in incident:
        return "Infrastructure"

    return "Application"


def determine_severity(incident):
    incident = incident.lower()

    if "all users" in incident or "production down" in incident:
        return "SEV-1"

    if "timeout" in incident or "failed" in incident:
        return "SEV-2"

    if "slow" in incident or "degraded" in incident:
        return "SEV-3"

    return "SEV-4"


def main():
    incident = input("Describe the incident: ")

    category = classify_incident(incident)
    severity = determine_severity(incident)

    print("\n=== INCIDENT ANALYSIS ===")
    print(f"Incident : {incident}")
    print(f"Category : {category}")
    print(f"Severity : {severity}")

    log_files = [
        "payment_timeout.log",
        "database_slow_query.log",
        "api_500_error.log",
        "disk_usage_high.log",
        "rabbitmq_connection_error.log"
    ]

    print("\n=== AVAILABLE LOG FILES ===")

    for index, file_name in enumerate(log_files, start=1):
        print(f"{index}. {file_name}")

    while True:
       try:
           choice = int(input("\nSelect log file: "))

           if 1 <= choice <= len(log_files):
              break

           print(
               f"Invalid selection. "
               f"Please choose between 1 and {len(log_files)}."
           )

       except ValueError:
           print("Invalid input. Please enter a number.")


    selected_file = log_files[choice - 1]

    log_file = f"../sample_logs/{selected_file}"


    logs = read_log_file(log_file)
    errors = find_errors(logs)

    print("\n=== ERROR LOGS ===")

    for error in errors:
        print(f"Timestamp : {error['timestamp']}")
        print(f"Level     : {error['level']}")
        print(f"Message   : {error['message']}")
        print()

    prompt = build_incident_prompt(
        incident,
        category,
        severity,
        errors
    )

    print("Sending incident analysis to Gemini...")

    ai_result = analyze_with_ai(prompt)

    print("\n=== AI INCIDENT ANALYSIS ===")
    print(ai_result)


if __name__ == "__main__":
    main()
