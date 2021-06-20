from PIL import ExifTags

def get_exif_data(img: Image) -> dict:
    """ gets exif data for an image """
    return {
        # from https://stackoverflow.com/a/4765242
        ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in ExifTags.TAGS and ExifTags.TAGS[k] != "MakerNote"
    }