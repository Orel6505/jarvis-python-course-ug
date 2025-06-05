import pyttsx3

# Initialize the text-to-speech engine globally
engine = pyttsx3.init()

def input_validation(request: str, lowerbound=0, upperbound=0) -> int:
    """
    Validates that the request is a digit and within (lowerbound, upperbound).
    Returns the digit if valid, -1 if the user wants to exit, otherwise -2 for error.
    """
    request = request.strip()
    if request == "-1":
        return -1  # Explicit request to exit

    if not request.isdigit():
        print("Invalid input.")
        return -2

    value = int(request)
    if lowerbound < value < upperbound:
        return value
    else:
        print("The number specified is not in range.")
        return -2

def talk(text: str) -> None:
    """Speak the provided text using TTS."""
    print(text)
    engine.say(text)
    engine.runAndWait()

def ttsx_stop():
    global engine
    if engine:
        engine.stop()
        engine = None
        print("Text-to-speech engine stopped.")
    else:
        print("Text-to-speech engine is not running.")