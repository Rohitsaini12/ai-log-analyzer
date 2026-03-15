def parse_log(file_path):

    errors = []
    warnings = []
    info = []

    with open(file_path, "r") as f:
        lines = f.readlines()

    for line in lines:

        if "ERROR" in line:
            errors.append(line.strip())

        elif "WARNING" in line:
            warnings.append(line.strip())

        elif "INFO" in line:
            info.append(line.strip())

    return {
        "errors": errors,
        "warnings": warnings,
        "info": info
    }