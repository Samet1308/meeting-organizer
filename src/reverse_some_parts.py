import re


INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = ("John Griffith London was an American novelist, journalist, and social activist. "
                  "(A pioneer of commercial fiction and American magazines, he was one of the first "
                  "American authors to become an international celebrity and earn a large fortune from writing.)")

def fix_text(mystr):


    def reverse_if_not_in_parenthesis(match):
        text = match.group(0)
        if text.startswith('(') and text.endswith(')'):
            return text  # Parantez içindeki kısmı olduğu gibi bırak
        else:
            return text[::-1]  # Ters sıradaki kelimeleri düzelt

    # Regex ile kelimeleri parantez içi ve dışı olarak ayır
    fixed_text = re.sub(r'\([^)]*\)|\S+', reverse_if_not_in_parenthesis, mystr)

    # Son olarak parantezleri kaldır
    fixed_text = fixed_text.replace('(', '').replace(')', '')

    return fixed_text

if __name__ == "__main__":
    result = fix_text(INPUT)
    print("Correct!" if result == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
    print(result)  # Sonuçları görmek için çıktıyı yazdır