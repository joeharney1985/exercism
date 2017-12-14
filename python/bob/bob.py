def blank_response(phrase):
    return 'Fine. Be that way!' if phrase.strip() == '' else None

def yell_response(phrase):
    return 'Whoa, chill out!' if phrase.isupper() else None

def question_response(phrase):
    return 'Sure.' if phrase.strip().endswith('?') else None

def other_response():
    return 'Whatever.'

def hey(phrase):
    return blank_response(phrase) or yell_response(phrase) or \
        question_response(phrase) or other_response()
