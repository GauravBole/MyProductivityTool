import random
from .file_extention import get_filename_ext
from django.contrib.contenttypes.models import ContentType


def file_path(instance, filename):
    """
    save file in prticular location and return its path
    :param instance:
    :param filename:
    :return: customize file saved path
    """

    new_folder = random.randint(1,999999999)
    content_type = ContentType.objects.get_for_model(instance.__class__)
    name, ext = get_filename_ext(filename)
    final_file_name = '{0}.{1}'.format(name,ext)
    return '{0}/{1}/{2}/'.format(content_type,new_folder,final_file_name)
