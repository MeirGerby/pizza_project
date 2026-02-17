import string

def search_words(text: str) -> bool:
    words = ['GLUTEN', 'PEANUT', 'ALLERGY']
    for i in convert_to_upper(text):
            if i in words:
                return True 
    return False 

def convert_to_upper(text: str) -> list:
    """convert the text to upper and remove punctuation marks"""
    removed_text = remove_punctuation(text)
    return [i.upper() for i in removed_text.split()]

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)



