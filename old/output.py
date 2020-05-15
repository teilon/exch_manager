def to_textfile(filename, text):
    with open(filename, "a") as text_file:
        text_file.write(text)
