import os
def get_remediation(issue):

    fixes = {

        "Hardcoded password": {
            "severity": "🔴 High",
            "why": "Hardcoded passwords can be exposed through source code or version control.",
            "recommendation": "Store passwords using environment variables or a secrets manager.",
            "example": '''import os

password = os.getenv("DB_PASSWORD")
'''
        },

        "API key": {
            "severity": "🔴 High",
            "why": "API keys should never be committed to source code.",
            "recommendation": "Store API keys securely using environment variables.",
            "example": '''import os

api_key = os.getenv("API_KEY")
'''
        },

        "Magic number": {
            "severity": "🟡 Medium",
            "why": "Magic numbers reduce readability and make maintenance difficult.",
            "recommendation": "Replace numeric literals with named constants.",
            "example": '''PASS_MARK = 70

if marks >= PASS_MARK:
    print("Pass")
'''
        },

        "TODO": {
            "severity": "🟢 Low",
            "why": "Leaving TODOs in production code may indicate incomplete functionality.",
            "recommendation": "Complete or remove TODO comments before deployment.",
            "example": "# TODO: Implement input validation"
        },

        "Debug print": {
            "severity": "🟢 Low",
            "why": "Debug statements clutter production logs.",
            "recommendation": "Remove debug print statements before deployment.",
            "example": "# Remove print() after debugging"
        },

        "Deep nesting": {
            "severity": "🟡 Medium",
            "why": "Deep nesting makes code difficult to understand and maintain.",
            "recommendation": "Use helper methods or early returns to reduce nesting.",
            "example": "Refactor nested if-statements into smaller functions."
        }

    }
    
   

    return fixes.get(issue)