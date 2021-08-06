from colors import Color


NUM_NAMES_LESS_THAN_NUM_IMAGES = u'''
\u274c ERROR \u274c
    {U}Number of names{E} is {R}{B}LESS{E} than {U}number of images{E} in directory
    {Y}Please, check the number of images in provided directory and number of names in povided file{E}'
'''.format(U = Color.UNDERLINE, B = Color.BOLD, R = Color.RED, Y = Color.YELLOW, E = Color.END)


NUM_NAMES_GREATER_THAN_NUM_IMAGES = u'''
\u274c ERROR \u274c
    {U}Number of names{E} is {R}{B}GREATER{E} than {U}number of images{E} in directory
    {Y}Please, check the number of images in provided directory and number of names in povided file{E}'
'''.format(U = Color.UNDERLINE, B = Color.BOLD, R = Color.RED, Y = Color.YELLOW, E = Color.END)


FIELD_DOES_NOT_EXIST = u'''
\u274c ERROR \u274c
    Set {R}{B}{FIELD}{E} in '.env' file
'''


PATH_DOES_NOT_EXIST = u'''
\u274c ERROR \u274c
    Given path, specifiend in '.env', {R}{B}DOES NOT EXIST{E}:
    {Y}{PATH}{E}
'''


TYPE_ERROR = u'''
\u274c ERROR \u274c
    {R}{B}{FIELD}{E} {U}MUST BE{E} an {R}INT{E} type
'''


STATUS_MESSAGE = u'Currently Processing: {G}{INDEX}{E} out of {G}{B}{TOTAL_NUMBER}{E} items...'


DONE_WITH_SINGLE_ITEM_MESSAGE = u'\u2705 DONE!'


SUCCESS_MESSAGE = u'''
\u2705 {B}{G}DONE{E} \u2705
    Program {G}successfully executed{E}!
    {U}Check the output folder{E}!
'''.format(G = Color.GREEN, B = Color.BOLD, U = Color.UNDERLINE, E = Color.END)


def GET_FIELD_DOES_NOT_EXIST_ERROR(field: str) -> str:
    return FIELD_DOES_NOT_EXIST.format(FIELD = field, B = Color.BOLD, R = Color.RED, E = Color.END)


def GET_PATH_DOES_NOT_EXIST_ERROR(path: str) -> str:
    return PATH_DOES_NOT_EXIST.format(PATH = path, B = Color.BOLD, R = Color.RED, Y = Color.YELLOW, E = Color.END)


def GET_TYPE_ERROR(field: str) -> str:
    return TYPE_ERROR.format(FIELD = field, B = Color.BOLD, U = Color.UNDERLINE, R = Color.RED, E = Color.END)


def GET_STATUS_MESSAGE(index: int, number_of_items: int) -> str:
    return STATUS_MESSAGE.format(INDEX = index, TOTAL_NUMBER = number_of_items, G = Color.GREEN, B = Color.BOLD, E = Color.END)
