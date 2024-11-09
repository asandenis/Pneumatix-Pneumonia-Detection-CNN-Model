import os
import cx_Oracle
import config

def insert_images():
    train_directory = os.path.join(config.DATASET_PATH, 'train')

    dsn_tns = cx_Oracle.makedsn(config.DB_CONFIG['host'], config.DB_CONFIG['port'], sid=config.DB_CONFIG['sid'])
    connection = cx_Oracle.connect(
        user=config.DB_CONFIG['username'],
        password=config.DB_CONFIG['password'],
        dsn=dsn_tns
    )
    cursor = connection.cursor()

    allowed_labels = ['NORMAL', 'PNEUMONIA']

    for label in allowed_labels:
        label_path = os.path.join(train_directory, label)

        if os.path.isdir(label_path):
            for image_file in os.listdir(label_path):
                file_path = os.path.join(label_path, image_file)

                if os.path.isfile(file_path) and image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    print(f"Inserting image: {file_path} with label '{label}'")

                    with open(file_path, 'rb') as file:
                        image_data = file.read()

                    cursor.execute("""
                        INSERT INTO chest_xray (image, label)
                        VALUES (:image, :label)
                    """, {'image': image_data, 'label': label})

    connection.commit()
    print("All images with labels 'NORMAL' and 'PNEUMONIA' have been successfully inserted into the database.")

    cursor.close()
    connection.close()

insert_images()