def security_review(code):

    findings = []
    score = 0
    summary = []
    
    if "api_key" in code.lower():
        findings.append(("error", "❌ Possible API key found."))
        summary.append("• Store API keys securely.")
        score += 20

    if "password" in code.lower():
        findings.append(("error", "❌ Possible hardcoded password detected."))
        summary.append("• Avoid hardcoding passwords.")
        score += 25

    if "eval(" in code:
        findings.append(("error", "❌ Use of eval() detected."))
        summary.append("• Avoid using eval().")
        score += 30

    if "exec(" in code:
        findings.append(("error", "❌ Use of exec() detected."))
        summary.append("• Avoid using exec().")
        score += 30
        
    if "secret" in code.lower():
         findings.append(("warning", "⚠ Secret detected."))
         
    if "token" in code.lower():
        findings.append(("warning", "⚠ Token detected."))

    if "SELECT" in code.upper():
        findings.append(("info", "ℹ SQL query detected. Ensure parameterized queries are used."))

    return findings, score, summary