import os
import MetadataManager


def does_sound_exist(sound: str) -> bool:
    """TODO: Docstring for does_sound_exist.

    Args:
        sound (str): TODO

    Returns: TODO

    """
    metadata = MetadataManager.get_metadata()

    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        metadata["paths"]["sound_bytes"],
        sound,
    )

    return os.path.exists(path)


def get_sound_path(sound: str) -> str:
    """TODO: Docstring for get_sound_path.

    Args:
        sound (str): TODO

    Returns: TODO

    """
    metadata = MetadataManager.get_metadata()

    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        metadata["paths"]["sound_bytes"],
        sound,
    )
