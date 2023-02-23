#                     strong password


p=input("enter the password")
len=len(p)
if len>=5 and len<=9:
    if "A"in p or"B"in p or "C"in p or "D"in p or"E"in p or "F"in p or"G"in p or "H"in p or "I" in p or "J"in p or "K"in p or "L"in p or "M" in p or "N" in p or "O"in p or "P"in p or"Q"in p or "R"in p or"S"in p or "T"in p or "U"in p or"V"in p or"W"in p or"X"in p or"Y"in p or"Z"in p :
        if  "a"in p or"b"in p or "c"in p or "d"in p or"e"in p or "f"in p or"g"in p or "h"in p or "i" in p or "j"in p or "k"in p or "l"in p or "m" in p or "n" in p or "o"in p or "p"in p or"q"in p or "r"in p or"s"in p or "t"in p or "u"in p or"v"in p or"w"in p or"x"in p or"y"in p or"z"in p :
            if "@"in p or "#"in p or"$"in p or"*"in p or "%"in p or "^"in p or"&"in p :
                if "1"in p or"2"in p or"3"in p or"4"in p or"5"in p or "6"in p or"7"in p or"8"in p or "9"in p:
                    print("strong password ")
                else:
                    print("u miss numerics")
            else:
                print("u miss special charecter")
        else:
            ("u miss small alphabit") 
    else:
        print("u miss capital alphabets")

                            