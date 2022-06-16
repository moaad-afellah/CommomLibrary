def input_Int(text, textError="Sorry!!!  give me a  number"):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print(textError)
