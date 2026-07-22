def generate_report(
    file_name,
    language,
    analysis_findings,
    security_findings,
    summary,
    score
):

    report = []

    report.append("=" * 50)
    report.append("      AI CODE REVIEW REPORT")
    report.append("=" * 50)

    report.append(f"\nFile Name : {file_name}")
    report.append(f"Language  : {language}")

    report.append("\n" + "-" * 50)
    report.append("CODE ANALYSIS")
    report.append("-" * 50)

    if analysis_findings:
        for _, message in analysis_findings:
            report.append(message)
    else:
        report.append("No code quality issues found.")

    report.append("\n" + "-" * 50)
    report.append("SECURITY ANALYSIS")
    report.append("-" * 50)

    if security_findings:
        for _, message in security_findings:
            report.append(message)
    else:
        report.append("No security issues found.")

    report.append("\n" + "-" * 50)
    report.append("RECOMMENDATIONS")
    report.append("-" * 50)

    if summary:
        for item in summary:
            report.append(item)
    else:
        report.append("No recommendations.")

    report.append("\n" + "-" * 50)
    report.append(f"OVERALL SCORE : {score}/100")

    if score >= 90:
        report.append("Rating : Excellent")
    elif score >= 70:
        report.append("Rating : Good")
    else:
        report.append("Rating : Needs Improvement")

    report.append("=" * 50)

    return "\n".join(report)