from PIL import ExifTags, Image

def get_exif_data(img: Image) -> dict:
    """ gets exif data for an image """
    return {
        # from https://stackoverflow.com/a/4765242
        ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in ExifTags.TAGS and ExifTags.TAGS[k] != "MakerNote"
    }

def get_exif_value(img: Image, value: str) -> str:
    exif_data = get_exif_data(img=img)
    return exif_data[value]
