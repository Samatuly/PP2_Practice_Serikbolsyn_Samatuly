with open("1st_text.txt") as f:
    with open("2nd_text.txt", "w") as f1:
        for line in f:
            f1.write(line)