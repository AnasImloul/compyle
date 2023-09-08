from . import cpp, java, javascript, python3, rust, go
import logging

syntax_checkers = {
    "python3": python3.check_syntax,
    "java": java.check_syntax,
    "c++": cpp.check_syntax,
    "javascript": javascript.check_syntax,
    "go": go.check_syntax,
    "rust": rust.check_syntax,
}

LANGUAGES = list(syntax_checkers.keys())


def check_syntax(code, language):
    language = language.lower()

    if language not in LANGUAGES:
        logging.warning(f"Language {language} not supported")
        return False

    return syntax_checkers[language](code)
