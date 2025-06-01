from pathlib import Path
from uuid import uuid4

from loguru import logger

from thispersondoesnotexist.helpers import save_picture
from thispersondoesnotexist.online_getter import get_online_person

for i in range(100):
    # Generate a unique filename using uuid4
    filename = f"person_{uuid4()}.jpeg"

    filepath = Path("out/" + filename)
    # Ensure the directory exists
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Get a picture of a fictional person
    picture = get_online_person()  # bytes representation of the image

    # Save to a file
    save_picture(picture, str(filepath))
    logger.debug(f"Saved {filepath}")
