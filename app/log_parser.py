def read_log_file(file_path):
    with open(file_path, "r") as file:
        logs = file.readlines()

    return logs


def parse_log(log):
    parts = log.strip().split(" ", 3)

    if len(parts) < 4:
        return None

    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = parts[3]

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }


def find_errors(logs):
    errors = []

    for log in logs:
        parsed_log = parse_log(log)


        if parsed_log and parsed_log["level"] == "ERROR":
            errors.append(parsed_log)


    return errors
