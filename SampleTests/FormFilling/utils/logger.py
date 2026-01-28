import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("D:\\Github\\InternWorks\\SampleTests\\FormFilling\\logs\\informations.log", mode="a"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
