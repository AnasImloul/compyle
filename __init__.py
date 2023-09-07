from . import cpp, java, javascript, python, python3


syntax_checkers = {
    "python": python.check_syntax,
    "python3": python3.check_syntax,
    "java": java.check_syntax,
    "c++": cpp.check_syntax,
    "javascript": javascript.check_syntax,
}

LANGUAGES = list(syntax_checkers.keys())


def check_syntax(code, language):
    language = language.lower()
    return syntax_checkers[language](code)
