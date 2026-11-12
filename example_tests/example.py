def send_message(destination, message: str):
    destination.write(message)


def copy(source_file, n: int, label: str):
    source_file.seek(n)
    source_file.close()
    source_file.seek(label)
