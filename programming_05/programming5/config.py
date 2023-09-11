
"""
submodule of io_utils.py and get_gene_level_information.py
"""

# pylint: disable=C0116
#ignore all "Function name "get_error_string_4_ValueError"
# doesn't conform to snake_case naming style"
#ignore all "Function name "get_error_string_4_TypeError"
# doesn't conform to snake_case naming style"
#ignore all "Function name "get_error_string_4_EXCEPTION_TYPE"
# doesn't conform to snake_case naming style"

_DIRECTORY_FOR_UNIGENE = "C://Users//Lenovo//PycharmProjects//pythonProject" \
                         "//pranathi_limmala//Programming_6200//assignment_05" \
                         "//assignment5_data//assignment5_data"
_FILE_ENDING_FOR_UNIGENE = "unigene"


def get_directory_for_unigene():
    """
    file directory path
    :return:
    """
    return _DIRECTORY_FOR_UNIGENE


def get_extension_for_unigene():
    """
    file suffix
    :return:
    """
    return _FILE_ENDING_FOR_UNIGENE


def get_host_keywords():
    """
    create a dictionary for mapping common
    names to scientific names
    :return:
    """
    bos_tarus = "Bos_taurus"
    homo_sapiens = "Homo_sapiens"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"
    host_keywords = {
        "bos taurus": bos_tarus,
        "cow": bos_tarus,
        "cows": bos_tarus,
        "homo sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,
        "equus caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,
        "mus_musculus": mus_musculus,
        "mouse": mus_musculus,
        "mice": mus_musculus,
        "ovis_aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "rattus_norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus
    }
    return host_keywords


def get_error_string_4_EXCEPTION_TYPE(file, arg):
    """ Print the invalid argument type
    message and exits the program """
    print("Could not open the file: {} for "
          "type '{}'".format(file, arg))


def get_error_string_4_ValueError():  # error when used get_fh(file, "1234")
    """ Print the invalid argument type
     message and exits the program """
    print("Invalid argument Value for "
          "opening a file for reading/writing")


def get_error_string_4_TypeError():  # error when used get_fh(file, "r", "w")
    """ Print the invalid argument type
    message and exits the program """
    print("Invalid argument Type")


if __name__ == '__main__':
    get_directory_for_unigene()
    get_extension_for_unigene()
    get_host_keywords()
    get_error_string_4_TypeError()
    get_error_string_4_ValueError()
    get_error_string_4_EXCEPTION_TYPE()
