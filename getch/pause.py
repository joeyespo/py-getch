from .getch import getch


def pause(message='Press any key to continue . . . '):
    """Prints the specified message if it's not None and waits for a keypress."""
    if message is not None:
        print message,
    getch()
    print
