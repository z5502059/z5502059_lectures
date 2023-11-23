import os

def safe_open(pth, mode='rt'):
    """ Opens the file in `pth` using the mode in `mode` and returns 
    a file object. 

    Will not open a file in writing mode if the file already exists and has
    some content.

    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading, 
        and 'a' for appending. See the `open` function for more options.
        Defaults to 'rt'
    """
    pass


if __name__ == "__main__":

    # Opening an existing file with content for reading
    with safe_open("test_file_exists_with_content.txt", mode='r') as fobj:
       print(fobj.read())

    # Opening an existing file with no content for writing - should work
    with safe_open("test_file_exists_no_content.txt", mode='w') as fobj:
       fobj.write('content')


    # Opening an existing file with content for writing - should raise Exception
    with safe_open("test_file_exists_with_content.txt", mode='w') as fobj:
       fobj.write('content')


