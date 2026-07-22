import re

def security_review(code):

    findings = []
    score = 0
    summary = []

    # Hardcoded Password
    password_pattern = r'(?i)(password|passwd|pwd)\s*[:=]\s*["\'].*?["\']'

    if re.search(password_pattern, code):
        findings.append(("error", "🔴 Hardcoded password detected."))
        summary.append("• Store passwords securely using environment variables.")
        score += 15

    # Hardcoded API Key
    api_pattern = r'(?i)(api[_-]?key|apikey)\s*[:=]\s*["\'].*?["\']'

    if re.search(api_pattern, code):
        findings.append(("error", "🔴 Hardcoded API key detected."))
        summary.append("• Store API keys securely using environment variables.")
        score += 15

    # Hardcoded Secret
    secret_pattern = r'(?i)(secret|secret_key|client_secret)\s*[:=]\s*["\'].*?["\']'

    if re.search(secret_pattern, code):
        findings.append(("error", "🔴 Hardcoded secret detected."))
        summary.append("• Never store secrets in source code.")
        score += 15

    # Hardcoded Token
    token_pattern = r'(?i)(token|access_token)\s*[:=]\s*["\'].*?["\']'

    if re.search(token_pattern, code):
        findings.append(("error", "🔴 Hardcoded access token detected."))
        summary.append("• Store tokens securely outside the application.")
        score += 15

    # Dangerous Functions
    if "eval(" in code:
        findings.append(("error", "🔴 Use of eval() detected."))
        summary.append("• Avoid using eval().")
        score += 15

    if "exec(" in code:
        findings.append(("error", "🔴 Use of exec() detected."))
        summary.append("• Avoid using exec().")
        score += 15

    # SQL Injection Risk
    sql_pattern = r'\b(SELECT|INSERT|UPDATE|DELETE)\b'

    if re.search(sql_pattern, code, re.IGNORECASE):
        findings.append(("info", "🟡 SQL query detected. Review for SQL Injection risks."))
        summary.append("• Use prepared statements or parameterized queries.")
        score += 8

    return findings, score, summary