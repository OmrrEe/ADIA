def grade_p1(globals):
    if "format" not in globals:
        print("The variable 'format' is not defined. Did you run the cell above?")
        return 
    
    format = globals["format"]

    if format != "%B %d, %Y at %H:%M":
        print("Try again! You can do this!")
    else:
        print("You got it!")

    return

def grade_p2(globals):
    if "day_of_week_format" not in globals:
        print("The variable 'format' is not defined. Did you run the cell above?")
        return 
    
    format = globals["day_of_week_format"]

    if format != "%A":
        print("Try again! You can do this!")
    else:
        print("You got it! Looks like Friday the 14th should have been the unlucky date then...")

    return
