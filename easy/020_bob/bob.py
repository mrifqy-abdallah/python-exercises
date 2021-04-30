def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    # If you address him without actually saying anything
    if hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"

    # If you YELL AT HIM
    if hey_bob.isupper():
        # Yelling but ends with question mark
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    # Other than yelling
    else:
        # Asking a casual question
        if hey_bob[-1] == "?":
            return "Sure."
        # Saying anything else
        return "Whatever."
