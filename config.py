import messages
from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from natsort import natsorted


class Config:
    '''
        Reads in the values from '.env' file
        Also, creates derivative variables
    '''
    def __init__(self):
        '''
            Loads '.env' file and reads the fields
        '''
        load_dotenv()

        self._PATH_TO_IMAGES       = getenv('PATH_TO_IMAGES')
        self._PATH_TO_NAMES        = getenv('PATH_TO_NAMES_LIST')
        self.OUTPUT_FOLDER         = getenv('OUTPUT_FOLDER')
        self.EXTENSION             = getenv('IMAGE_EXTENSION')
        self.DELETE_ORIGINAL_FILES = getenv('DELETE_ORIGINAL_FILES')

        # Set for None for now, will change in '_verify'
        self.FILES                 = None
        self.NAMES                 = None

        self.START_X               = getenv('START_COORDINATE_X')
        self.START_Y               = getenv('START_COORDINATE_Y')
        self.END_X                 = getenv('END_COORDINATE_X')
        self.END_Y                 = getenv('END_COORDINATE_Y')

        # Set for empty tuple, will change in '_verify'
        self.AREA                  = ()

        self._verify()

    def _verify(self):
        '''
            Verifies the field and tries to cast them to proper types
            Also, sets 'AREA'
        '''
        # Checks PATH_TO_IMAGES
        if ( not self._PATH_TO_IMAGES ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('PATH_TO_IMAGES'))
        elif ( not Path(self._PATH_TO_IMAGES).is_dir() ):
            raise Exception(messages.GET_PATH_DOES_NOT_EXIST_ERROR(self._PATH_TO_IMAGES))

        # Since _PATH_TO_IMAGES is Valid, set FILES
        # Uses 'natsorted' to sort the files in ascending order
        self.FILES = [
            Path(p) for p in natsorted(
                [str(path) for path in list(Path(self._PATH_TO_IMAGES).glob(f'*.{self.EXTENSION}'))]
            )
        ]

        # Checks PATH_TO_NAMES_LIST
        if ( not self._PATH_TO_NAMES ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('PATH_TO_NAMES_LIST'))
        elif ( not Path(self._PATH_TO_NAMES).is_file() ):
            raise Exception(messages.GET_PATH_DOES_NOT_EXIST_ERROR(self._PATH_TO_NAMES))

        # Since _PATH_TO_NAMES is Valid, set NAMES
        # rstrip() makes sure empty line is not appended
        with open(self._PATH_TO_NAMES, 'r') as fin:
            self.NAMES = [name.strip() for name in fin.readlines() if name.rstrip()]

        # Checks EXTENSION
        if ( not self.EXTENSION ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('IMAGE_EXTENSION'))

        # Checks OUTPUT_FOLDER
        if ( not self.OUTPUT_FOLDER ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('OUTPUT_FOLDER'))
        elif ( not Path(self.OUTPUT_FOLDER).is_dir() ):
            raise Exception(messages.GET_PATH_DOES_NOT_EXIST_ERROR(self.OUTPUT_FOLDER))

        # Checks DELETE_ORIGINAL_FILES
        if ( not self.DELETE_ORIGINAL_FILES ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('DELETE_ORIGINAL_FILES'))
        else:
            self.DELETE_ORIGINAL_FILES = self.DELETE_ORIGINAL_FILES.upper() in ['TRUE', '1', 'YES', 'Y', 'T']

        # Checks COORDINATEs
        if ( not self.START_X ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('START_COORDINATE_X'))
        elif ( not self.START_Y ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('START_COORDINATE_Y'))
        elif ( not self.END_X ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('END_COORDINATE_X'))
        elif ( not self.END_Y ):
            raise Exception(messages.GET_FIELD_DOES_NOT_EXIST_ERROR('END_COORDINATE_Y'))
        else:
            try:
                self.START_X = int(self.START_X)
            except ValueError:
                raise Exception(messages.GET_TYPE_ERROR('START_COORDINATE_X'))

            try:
                self.START_Y = int(self.START_Y)
            except ValueError:
                raise Exception(messages.GET_TYPE_ERROR('START_COORDINATE_Y'))

            try:
                self.END_X = int(self.END_X)
            except ValueError:
                raise Exception(messages.GET_TYPE_ERROR('END_COORDINATE_X'))

            try:
                self.END_Y = int(self.END_Y)
            except ValueError:
                raise Exception(messages.GET_TYPE_ERROR('END_COORDINATE_Y'))

        # Compares the lengths of FILES and NAMES
        if ( len(self.NAMES) < len(self.FILES) ):
            raise Exception(messages.NUM_NAMES_LESS_THAN_NUM_IMAGES)
        if ( len(self.NAMES) > len(self.FILES) ):
            raise Exception(messages.NUM_NAMES_GREATER_THAN_NUM_IMAGES)

        # Since Coordinates are Valid, sets AREA
        self.AREA = (
            self.START_X,
            self.START_Y,
            self.END_X,
            self.END_Y
        )
