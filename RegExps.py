import re


# 1
def check_email_format(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


# 2
def find_words_starts_with_letter_s_and_S(text):
    pattern = r'\b[Ss]\w+'
    return re.findall(pattern, text)


# 3
def find_numbers_in_words(text):
    numbers = re.findall('[0-9]+', text3)
    return numbers


# 4
def check_text_for_having_yes_and_absense_no(text):
    pattern = r'^Да(?!, нет)'
    if re.match(pattern, text):
        return True
    else:
        return False


# 5
def find_dates_in_format_dd_mm_yyyy(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, text)


text1 = "aza@gmail.com"
text2 = 'sf mkgmerg ngjtrng sjgnrejs gjnerngs gsssgknrl Ssnjgwkn gs segekgnr Ssewfew fwer sgsdgdss'
text3 = 'hireug 156 gruigjoer6 6262 uigjrneog, 5152 greogmerl 26262 265'
text4 = "Да, конечно"
text5 = "Today is 09/08/2023, and tomorrow 10/08/2023"

print(check_email_format(text1))
print(find_words_starts_with_letter_s_and_S(text2))
print(find_numbers_in_words(text3))
print(check_text_for_having_yes_and_absense_no(text4))
print(find_dates_in_format_dd_mm_yyyy(text5))
