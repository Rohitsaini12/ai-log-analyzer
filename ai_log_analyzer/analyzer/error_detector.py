from collections import Counter

def analyze_errors(errors):

    error_messages = [e.split("ERROR:")[-1].strip() for e in errors]

    counter = Counter(error_messages)

    most_common = counter.most_common(1)

    return {
        "total_errors": len(errors),
        "most_common_error": most_common[0][0] if most_common else None,
        "count": most_common[0][1] if most_common else 0
    }