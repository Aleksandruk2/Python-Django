import uuid

# завантаження зображення за вказаним шляхом з унікальним іменем та розширенням .webp
def upload_image(instance, filename):
    return f"images/{uuid.uuid4()}.webp"