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

extensions = {
    "python3": python3.extension,
    "java": java.extension,
    "c++": cpp.extension,
    "javascript": javascript.extension,
    "go": go.extension,
    "rust": rust.extension,
}

comments = {
    "python3": python3.comment,
    "java": java.comment,
    "c++": cpp.comment,
    "javascript": javascript.comment,
    "go": go.comment,
    "rust": rust.comment,
}


languages = list(syntax_checkers.keys())


def check_syntax(code, language, debug=False):
    language = language.lower()

    if language not in languages:
        logging.warning(f"Language {language} not supported")
        return False

    return syntax_checkers[language](code, debug=debug)
