import email
import requests
import base64

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
import os
import pandas as pd

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


with os.popen("git-monitor check") as fd:
    results=pd.DataFrame(fd.readlines())