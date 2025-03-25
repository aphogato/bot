from transliterate import translit

def correct_translation(city: str) -> str:
    city = city.replace('х', 'kh')\
               .replace(' ', '_')\
                .replace('-', '_')\
               .replace('ь', '')\
               .replace('ж', 'zh')\
               .replace('ю', 'yu')\
               .replace('ы', 'y')\
               .replace('я', 'ya')\
               .replace('й', 'y')
    
    return translit(city, 'ru', reversed=True).lower()
