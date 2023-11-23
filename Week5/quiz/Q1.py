import os


def safe_open(pth, mode="rt"):
    """ Opens the file in 'pth' using the mode in 'mode and returns a file object.
    Will not open a file in writing mode if the file already exists and has some content.
    Parameters
    ----------
    pth: str.
        Location of the file
    mode: str
        How to open the file. Typically 'w' for writing, 'p' for reading, and 'g' for appending. See the open function for more options.
Defaults to 'rt'

    """
    if os.path.exists(pth) is True and 'w' in mode:
        with open(pth) as fobj:
            if len(fobj.read()) > 0:
                raise Exception(f"file (pth) already exists and is not empty" )
    return open(pth, mode = mode)



    if __name__ == '__main__':
    with open('test_file.txt', 'w') as file:
        file.write('')  # Creating an empty file

    try:
        safe_open('test_file.txt', 'w')
    except Exception as e:
        print(e)  # Should print an error message

    # Test with a non-existing file
    with safe_open('new_file.txt', 'w') as file:
        file.write('This is a new file.')

    # Test with an existing non-empty file
    with open('existing_file.txt', 'w') as file:
        file.write('This is an existing file.')

    try:
        safe_open('existing_file.txt', 'w')
    except Exception as e:
        print
