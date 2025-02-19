import os

from src.config import Config
from src.logger import Logger

def init_marketmaker():
    config = Config()
    logger = Logger()

    logger.info("Initializing MarketMaker...")
    sqlite_db = config.get_sqlite_db()
    screenshots_dir = config.get_screenshots_dir()
    projects_dir = config.get_projects_dir()
    logs_dir = config.get_logs_dir()

    logger.info("Initializing Prerequisites Jobs...")
    os.makedirs(os.path.dirname(sqlite_db), exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)
    os.makedirs(projects_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    
    # from src.bert.sentence import SentenceBert

    # logger.info("Loading sentence-transformer BERT models...")
    # prompt = "Light-weight keyword extraction excercise for BERT model loading.".strip()
    # SentenceBert(prompt).extract_keywords()
    # logger.info("BERT model loaded successfully.")
