import os
import uuid

def save_file(file):
    os.makedirs("uploads", exist_ok=True)

    # Nombre único
    filename = f"{uuid.uuid4()}.csv"
    filepath = os.path.join("uploads", filename)

    with open(filepath, "wb") as buffer:
        buffer.write(file.file.read())

    return filepath