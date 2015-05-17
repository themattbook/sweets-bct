def primary():
    class pcolors:
        HEADER = '\033[91m'
	RETURN = '\033[0m'
	    
    print pcolors.HEADER + "\nSweet's Binary Conversion Tool v1.0"
    print pcolors.RETURN + "Easily convert characters to Binary."
    print "Matthew Sweet - themattbook@gmail.com\n"

    print pcolors.HEADER + "\tWarning:",
    print pcolors.RETURN + """
    \tThis tool will not differentiate spacing. For example,
    \ttyping "Rock on" will also include the space between
    \tRock and on. A more accurate conversion would be "Rockon".
    """

    print pcolors.RETURN + "Enter characters to convert: ",

    data = raw_input()

    print "\nResults: ",
    print pcolors.HEADER + (' '.join(format(ord(x), 'b') for x in data) + pcolors.RETURN)
    print
    repeat = str(raw_input("Would you like to convert more? y/n: "))
    if repeat == "y": 
        primary()
    elif repeat == "Y":
        primary()
    else:
        quit()
primary()
