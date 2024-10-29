#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8
"""


def validUTF8(data):
    """
    validUTF8:
        determines if a given data set represents a valid UTF-8
        Return: True if data is a valid UTF-8 encoding, otherwise
    """

    # Number of bytes left for the current character
    bytes_remaining = 0

    for byte in data:
        # Only the last 8 bits are core, so apply a mask of 0xFF
        byte = byte & 0xFF

        if bytes_remaining == 0:
            if (byte >> 5) == 0b110:
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110:
                bytes_remaining = 3
            elif (byte >> 7):
                return False
        else:
            # Check that this byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1

    # Return true if there are no leftover bytes exp
    return bytes_remaining == 0
