from .conf import settings

import os


def get_media_structure():
    dirs = settings.MEDIA_DIRS
    media_dict = dict()
    for dir_name in dirs:
        if os.path.isdir(dir_name):
            res = _recursive_media_dir(dir_name, dir_name)
            if res:
                media_dict[dir_name] = res
    return media_dict


def _recursive_media_dir(dir_name, root_dir):
    dir_dict = dict()
    dir_dict[settings.MEDIA_LIST_NAME] = media_list = list()
    for entry in os.scandir(dir_name):
        if entry.is_dir():
            res = _recursive_media_dir(entry.path, root_dir)
            if res:
                dir_dict[entry.path.lstrip(root_dir)] = res
        else:
            if entry.name.lower().endswith(".mp4"):
                media_list.append(entry.path.lstrip(root_dir).replace("\\", "/"))
    if len(dir_dict) == 1 and len(media_list) == 0:
        return None
    else:
        return dir_dict


if __name__ == "__main__":
    import pprint
    pprint.pprint(get_media_structure())
