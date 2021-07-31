
import os
import colab

"""Menghubungkan drive ke google colab"""

from google.colab import drive
drive.mount("/content/drive",force_remount=True)

"""Menghubungkan ke kaggle"""

#menghubungkan dengan kaggle ubah isi path dibawah ke lokasi file kaggle.json
os.environ['KAGGLE_CONFIG_DIR'] = "/content/drive/Shareddrives/Drive-1/DataScience"

