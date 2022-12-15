def find_packet_marker(buffer: str, substring_length: int) -> int:
    """
    Finds the start of the packet marker in a buffer of characters.

    This function searches the given buffer for a substring with the specified length that does not contain any repeating characters. If such a substring is found, the function returns the index of the start of the substring in the buffer. Otherwise, the function returns -1.

    Args:
        buffer (str): The buffer of characters to search.
        substring_length (int): The length of the substring to search for.

    Returns:
        int: The index of the start of the packet marker in the buffer, or -1 if the packet marker was not found.
    """
    start_of_packet_marker = -1
    for i in range(len(buffer)):
        substring = buffer[i:i+substring_length]
        if len(set(substring)) == len(substring):
            start_of_packet_marker = i + len(substring)
            break

    return start_of_packet_marker
