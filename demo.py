from hate.logger import logging
from hate.exception import CustomException

from hate.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()

obj.sync_folder_from_gcloud("hate_speech_classification_2024", 'dataset.zip', 'download/dataset.zip')