from colors import Color


NUM_NAMES_LESS_THAN_NUM_IMAGES = u"""
\u274c ERROR \u274c
    {U}Number of names{E} is {R}{B}LESS{E} than {U}number of images{E} in directory
    {Y}Please, check the number of images in provided directory and number of names in povided file{E}'
""".format(U = Color.UNDERLINE, B = Color.BOLD, R = Color.RED, Y = Color.YELLOW, E = Color.END)

NUM_NAMES_GREATER_THAN_NUM_IMAGES = u"""
\u274c ERROR \u274c
    {U}Number of names{E} is {R}{B}GREATER{E} than {U}number of images{E} in directory
    {Y}Please, check the number of images in provided directory and number of names in povided file{E}'
""".format(U = Color.UNDERLINE, B = Color.BOLD, R = Color.RED, Y = Color.YELLOW, E = Color.END)
