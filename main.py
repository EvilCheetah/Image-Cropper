import environ
import messages
from pathlib import Path
from PIL import Image

env = environ.Env()
environ.Env.read_env()

IMAGES                = env('PATH_TO_IMAGES')
NAMES                 = env('PATH_TO_NAMES_LIST')
EXTENSION             = env('IMAGE_EXTENSION')
OUTPUT_FOLDER         = env('OUTPUT_FOLDER')
DELETE_ORIGINAL_FILES = bool(env('DELETE_ORIGINAL_FILES'))
AREA                  = (
    int(env('START_COORDINATE_X')),
    int(env('START_COORDINATE_Y')),
    int(env('END_COORDINATE_X')),
    int(env('END_COORDINATE_Y'))
)


def check_lengths_of_lists(num_names: int, num_images: int) -> None:
    if (num_names < num_images):
        raise Exception(messages.NUM_NAMES_LESS_THAN_NUM_IMAGES)
    if (num_names > num_images):
        raise Exception(messages.NUM_NAMES_GREATER_THAN_NUM_IMAGES)



def main():
    # Reads in the future names of the files
    with open(NAMES, 'r') as fin:
        image_names = [name.strip() for name in fin.readlines()]

    # Reads in the paths of all image files in the directory
    file_paths = list(Path(IMAGES).glob(f'*.{EXTENSION}'))

    check_lengths_of_lists(len(image_names), len(file_paths))

    # Opens, crops, saves the image
    for name, path in zip(image_names, file_paths):
        image = Image.open(path)
        image = image.crop(AREA)
        image.save(f'{name}.{EXTENSION}')



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(u'Program was terminated! \u274c')
    # except Exception as error:
    #     print(error)
