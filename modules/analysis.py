 
import re

def code_analysis(code):
    findings = []
    summary = []
    score = 0

    if len(code.strip()) == 0:
        findings.append(("warning", "⚠ Empty source code."))
        summary.append("• Paste or upload valid source code.")
        return findings, score, summary

    # Debug print statements
    if "print(" in code or "System.out.println" in code:
        findings.append(("warning", "⚠ Debug print statements found."))
        summary.append("• Remove unnecessary debug print statements.")
        score += 5

    # TODO comments
    if "TODO" in code:
        findings.append(("warning", "⚠ TODO comments found."))
        summary.append("• Complete pending TODO items.")
        score += 5

    # File size
    line_count = len(code.splitlines())

    if line_count > 100:
        findings.append(("warning", "⚠ Large source file detected."))
        summary.append("• Consider splitting large files into smaller modules.")
        score += 10

    if line_count > 200:
        findings.append(("warning", "⚠ Very large source file."))
        summary.append("• Break large files into smaller modules.")
        score += 15

    # Comments
    if "#" in code or "//" in code:
        findings.append(("success", "✔ Comments detected."))

    # Tabs
    if "\t" in code:
        findings.append(("warning", "⚠ Tabs detected. Use spaces for consistent formatting."))
        summary.append("• Replace tabs with spaces.")

    # Trailing whitespace
    for line in code.splitlines():
        if line.endswith(" "):
            findings.append(("warning", "⚠ Trailing whitespace detected."))
            summary.append("• Remove trailing whitespace.")
            score += 2
            break

    # NEW: Long functions
    inside_function = False
    function_lines = 0

    for line in code.splitlines():

        stripped = line.strip()

        if stripped.startswith("def ") or stripped.startswith("public"):

            inside_function = True
            function_lines = 0

        if inside_function:
            function_lines += 1

        if inside_function and stripped == "":
            if function_lines > 30:
                findings.append(("warning", "⚠ Long function detected (>30 lines)."))
                summary.append("• Split long functions into smaller reusable functions.")
                score += 5

            inside_function = False
            
            
    # Magic Number Detection

    ignore = {"0", "1", "2"}

    magic_numbers = {}

    for line_no, line in enumerate(code.splitlines(), start=1):

        numbers = re.findall(r'\b(?:\d+(?:\.\d+)?)\b', line)

        for value in numbers:

            if value not in ignore:

                if value not in magic_numbers:
                    magic_numbers[value] = []

                magic_numbers[value].append(line_no)

    if magic_numbers:

        findings.append((
            "warning",
            f"⚠ Multiple magic numbers detected ({len(magic_numbers)} unique values)."
        ))

        for value, lines in magic_numbers.items():

            if len(lines) == 1:
                summary.append(
                    f"• Line {lines[0]}: Replace '{value}' with a named constant."
                )
            else:
                summary.append(
                    f"• Lines {', '.join(map(str, lines))}: Replace '{value}' with a named constant."
                )
            score = score + min(len(magic_numbers), 3)

              
            
    # Deep Nesting Detection

    max_nesting = 0
    current_nesting = 0

    for line in code.splitlines():

        stripped = line.strip()

        # Python indentation
        if stripped.startswith(("if ", "for ", "while ", "elif ", "else:", "try:", "except", "with ")):
            current_nesting += 1
            max_nesting = max(max_nesting, current_nesting)

        # Java braces
        current_nesting += line.count("{")
        current_nesting -= line.count("}")

        if stripped == "":
            current_nesting = max(0, current_nesting - 1)

    if max_nesting >= 4:
        findings.append(("warning", "⚠ Deep nesting detected."))
        summary.append("• Reduce nested blocks by using helper methods or early returns.")
        score += 5    

    return findings, score, summary 