def code_analysis(code):
    if len(code.strip()) == 0:
        findings.append(("warning", "⚠ Empty source code."))
        summary.append("• Paste or upload valid source code.")
    findings = []
    summary = []
    score = 0

    if "print(" in code or "System.out.println" in code:
        findings.append(("warning", "⚠ Debug print statements found."))
        summary.append("• Remove unnecessary debug print statements.")
        score += 10

    if "TODO" in code:
        findings.append(("warning", "⚠ TODO comments found."))
        summary.append("• Complete pending TODO items.")
        score += 5

    if len(code.splitlines()) > 100:
        findings.append(("warning", "⚠ Large source file detected."))
        summary.append("• Consider splitting large files into smaller modules.")
        score += 10
    
    if len(code.splitlines()) > 200:
        findings.append(("warning", "⚠ Very large source file."))
        summary.append("• Break large files into smaller modules.")
        score += 15

    if "#" in code or "//" in code:
        findings.append(("success", "✔ Comments detected."))

    return findings, score, summary