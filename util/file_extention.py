import os


def get_filename_ext(filepath):
    """
    get file extention from uploaded file
    :param filepath:
    :return: - file name and its extentions
    """
    base_file = os.path.basename(filepath)
    file_name, exc = os.path.splitext(base_file)
    return file_name,exc