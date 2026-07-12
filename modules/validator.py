import ast
def detect_language(code):

    if ("def " in code or
        "print(" in code or
        "import " in code or
        "if __name__" in code):

        return "🐍 Python"
    elif (
    "public class" in code or
    "class " in code or
    "public static void main" in code or
    "System.out.println" in code or
    "Scanner" in code or
    "import java" in code or
    "private " in code or
    "protected " in code or
    "extends " in code or
    "implements " in code
):
    

        return "☕ Java"

    return "Unknown"
def validate_python(code):
    try:

        ast.parse(code)

        return True, None

    except SyntaxError as e:

        return False, f"❌ Syntax Error (Line {e.lineno}): {e.msg}"