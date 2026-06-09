def validate_query(sql):

    sql = sql.strip().upper()

    if not sql.startswith("SELECT"):
        return False

    blocked = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE"
    ]

    for word in blocked:
        if word in sql:
            return False

    return True