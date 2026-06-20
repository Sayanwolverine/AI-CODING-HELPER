def fix_code(code, language):

    code = code.strip()

    # Python
    if language == "Python":
        if "print " in code:
            return f"❌ Error: Missing brackets\n\n✅ Fixed Code:\n{code.replace('print ', 'print(') + ')'}"

        if "=" not in code and "print(" not in code:
            return "⚠️ This doesn't look like valid Python code."

        return "✅ Python code looks correct!"

    # C
    if language == "C":
        if ";" not in code:
            return "❌ Missing semicolon (;) in C code."

        if "#include" not in code:
            return "⚠️ Missing #include<stdio.h>"

        return "✅ C code looks fine!"

    # JavaScript
    if language == "JavaScript":
        if "console.log" in code and ";" not in code:
            return "❌ Missing semicolon ;"

        return "✅ JavaScript code OK!"

    # HTML
    if language == "HTML":
        if "<html>" not in code:
            return "⚠️ Missing <html> tag"

        return "✅ HTML looks fine!"

    return "🤖 AI: I analyzed your code. Looks okay or unsupported language."