# def parse_declaration(text):
#     category, value = text.split(':')
#     return category.strip().lower(), float(value)

# def duty_amount(text):
#     value, rate = text.split('@')
#     return float(value) * float(rate) / 100

# def hs_chapter(code):
#     return int(code.split('.')[0][:2])

# def main():
#     print("==== Running parse_declaration ====")
#     user_input = input("Enter category:value (e.g. electronics:25000): ")
#     result = parse_declaration(user_input)
#     print("Category and Value:", result)

#     print("\n==== Running duty_amount ====")
#     user_input = input("Enter value@rate (e.g. 25000@20): ")
#     result = duty_amount(user_input)
#     print("Duty Amount:", result)

#     print("\n==== Running hs_chapter ====")
#     user_input = input("Enter an HS code (e.g. 8517.12): ")
#     result = hs_chapter(user_input)
#     print("Chapter:", result)

# if __name__ == "__main__":
#     main()






import math


def parse_declaration(text):
    if not isinstance(text, str):
        return None

    if text.count(':') != 1:
        return None

    category, value = text.split(':')

    category = category.strip()
    value = value.strip()

    if not category or not value:
        return None

    try:
        value = float(value)
        if not math.isfinite(value):
            return None
    except ValueError:
        return None

    return category.lower(), value


def duty_amount(text):
    if not isinstance(text, str):
        return None

    if text.count('@') != 1:
        return None

    value, rate = text.split('@')

    try:
        value = float(value.strip())
        rate = float(rate.strip())

        if not math.isfinite(value) or not math.isfinite(rate):
            return None

        if value < 0 or rate < 0:
            return None

    except ValueError:
        return None

    return value * rate / 100


def hs_chapter(code):
    if not isinstance(code, str):
        return None

    code = code.strip()

    if not code:
        return None

    chapter = code.split('.')[0]

    if len(chapter) < 2 or not chapter.isdigit():
        return None

    return int(chapter[:2])


def main():
    print("==== Running parse_declaration ====")
    user_input = input("Enter category:value (e.g. electronics:25000): ")
    result = parse_declaration(user_input)
    print("Category and Value:", result)

    print("\n==== Running duty_amount ====")
    user_input = input("Enter value@rate (e.g. 25000@20): ")
    result = duty_amount(user_input)
    print("Duty Amount:", result)

    print("\n==== Running hs_chapter ====")
    user_input = input("Enter an HS code (e.g. 8517.12): ")
    result = hs_chapter(user_input)
    print("Chapter:", result)


if __name__ == "__main__":
    main()
