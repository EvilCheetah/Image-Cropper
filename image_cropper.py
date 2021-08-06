import messages
from config import Config
from os import (
    remove as file_remove,
    name as os_name,
    system
)
from pathlib import Path
from PIL import Image


def _clear_screen() -> None:
    if ( os_name == 'nt' ):
        system('cls')

    else:
        system('clear')


class ImageCropper:
    def __init__(self):
        self.CONFIG = Config()

    def crop(self):
        '''
            Opens, crops, saves the image
        '''
        _clear_screen()
        for index, (name, file) in enumerate( zip(self.CONFIG.NAMES, self.CONFIG.FILES), 1 ):
            self._print_currently_processing_message(index)

            image = Image.open(file)
            image = image.crop(self.CONFIG.AREA)
            image.save(
                Path(self.CONFIG.OUTPUT_FOLDER).joinpath(
                    f'{name}.{self.CONFIG.EXTENSION.lower()}'
                )
            )

            self._print_done_processing_single_item()

        self._delete_files()
        self._print_success_message()

    def _print_currently_processing_message(self, index: int) -> None:
        print(messages.GET_STATUS_MESSAGE(index, len(self.CONFIG.FILES)), end = '')

    def _print_done_processing_single_item(self) -> None:
        print(messages.DONE_WITH_SINGLE_ITEM_MESSAGE)

    def _print_success_message(self) -> None:
        _clear_screen()
        print(messages.SUCCESS_MESSAGE)

    def _delete_files(self) -> None:
        '''
            If DELETE_ORIGINAL_FILES is True, removes original images
        '''
        if self.CONFIG.DELETE_ORIGINAL_FILES:
            for file in self.CONFIG.FILES:
                file_remove(file)
