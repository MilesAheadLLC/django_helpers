import StringIO

from django_helpers.helpers.utils import decrypt_file, encrypt_file


def test_encrypt_file_encrypts():
    """
     Check to see if  encrypt_file actually encrypts
    """
    test_file = StringIO.StringIO()
    test_file.write("This is the test")
    encrypted_file = encrypt_file("TheKey12TheKey12", test_file)

    #check to see if the resulting file is binary
    assert b'\x00' in encrypted_file.getvalue()
    test_file.close()

def test_decrypt_file_decrypts():
    """
     Check to is if decrypt_file actually decrypts
    """
    test_file = StringIO.StringIO()
    test_file.write('This the test')

    encrypted_file = encrypt_file("TheKey12TheKey12", test_file)
    decrypted_file = decrypt_file("TheKey12TheKey12", encrypted_file)

    assert test_file.getvalue() == decrypted_file.getvalue()
    test_file.close()

