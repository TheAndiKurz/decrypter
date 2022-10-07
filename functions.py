import os


CHUNK_SIZE = 4096


def _auxilary_crypt_file(callback_chunk_processing, filepath, password, output_filepath):
    if os.path.exists(output_filepath):
        if input(f"Do you want to overwrite {output_filepath}? (y/n) ").lower() == "y":
            os.remove(output_filepath)
        else:
            exit()

    password = bytes(password, encoding="utf8")
    chunk = bytes()

    with open(filepath, "rb") as f:
        chunk = f.read(CHUNK_SIZE)

        while len(chunk) != 0:
            encrypted_chunk = callback_chunk_processing(chunk, password)

            with open(output_filepath, "ab+") as encrypted_file:
                encrypted_file.write(encrypted_chunk)

            chunk = f.read(CHUNK_SIZE)


def encrypt_file(filepath, password, encrypted_filepath=None):
    if encrypted_filepath is None:
        encrypted_filepath = filepath + "_encrypted"

    _auxilary_crypt_file(encrypt_chunk, filepath, password, encrypted_filepath)


def decrypt_file(filepath, password, decrypted_filepath=None):
    if decrypted_filepath is None:
        decrypted_filepath = filepath + "_decrypted"

    _auxilary_crypt_file(decrypt_chunk, filepath, password, decrypted_filepath)


def encrypt_chunk(chunk: bytes, password: bytes):
    encrypted_chunk = bytearray()

    for i, byte in enumerate(chunk):
        encrypted_chunk.append(byte + password[i % len(password)])

    return encrypted_chunk


def decrypt_chunk(chunk: bytes, password: bytes):
    encrypted_chunk = bytearray()

    for i, byte in enumerate(chunk):
        encrypted_chunk.append(byte - password[i % len(password)])

    return encrypted_chunk


if __name__ == "__main__":
    encrypt_file("./s.txt", "hallo")
    decrypt_file("./s.txt_encrypted", "hallo")
