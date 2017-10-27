lastNameIn = input("Napis svoje prijimeni bez diakritiky: ")
def guess(lastName):
    if lastNameIn[-3:] == "ova":
        print(lastNameIn + "? Tak to jsi nejspis holka.")
    else:
        print(lastNameIn + "? Tak to jsi asi kluk.")
guess(lastNameIn)
