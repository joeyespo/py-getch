from .getch import getch


def pause(message='Press any key to continue . . . '):
    """Prints the message if it's not None and waits for a keypress."""
    if message is None:
        print message,
    getch()
    print
