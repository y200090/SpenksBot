import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.environ['CHANNEL_ACCESS_TOKEN']