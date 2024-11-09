import cx_Oracle
import numpy as np
import config
from io import BytesIO
from PIL import Image

def load_data(target_size=(128, 128)):
    dsn_tns = cx_Oracle.makedsn(config.DB_CONFIG['host'], config.DB_CONFIG['port'], sid=config.DB_CONFIG['sid'])
    connection = cx_Oracle.connect(
        user=config.DB_CONFIG['username'],
        password=config.DB_CONFIG['password'],
        dsn=dsn_tns
    )
    cursor = connection.cursor()

    cursor.execute("SELECT image, label FROM chest_xray")

    images = []
    labels = []

    for image_blob, label in cursor:
        blob_data = image_blob.read()

        image = Image.open(BytesIO(blob_data)).convert('L')

        image = image.resize(target_size)

        image_array = np.array(image)

        images.append(image_array)
        labels.append(label)

    cursor.close()
    connection.close()

    print("Data loaded successfully from the database.")

    return np.array(images), np.array(labels)