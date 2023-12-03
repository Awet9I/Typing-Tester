import time
import sys


def timer():
    result = {}
    # Initialize a variable to store the start time

    start_time = None

    # Initialize a variable to set the timeout (in seconds)
    timeout_seconds = 2

    # Record the start time when the user starts typing
    # input("Start typing when ready...")  # Prompt the user to start typing
    start_time = time.time()

    # Capture user input as a complete line
    user_input = ""
    while True:
        line = sys.stdin.readline()  # Read a complete line

        if not line:  # Check for EOF (End of File)
            break

        user_input += line
        time_elapsed = time.time() - start_time
        # Check for a timeout (no input for the specified time)
        if time_elapsed > timeout_seconds:
            time_re = round(time_elapsed, 2)
            text = line
            result[time_re] = text
            return result


if __name__ == "__main__":
    t = timer()
    print(t)
