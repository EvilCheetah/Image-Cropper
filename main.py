from image_cropper import ImageCropper


def main():
    ImageCropper.main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(u'Program was terminated! \u274c')
    except Exception as error:
        print(error)
