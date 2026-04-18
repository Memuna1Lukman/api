import hashlib
from .config import settings
import secrets

PEPPER = settings.pepper

def generate():
    random_bytes = secrets.token_bytes(32)
    plain_key = secrets.token_urlsafe(32)

    return plain_key



def generate_api_keys(plain_key):
    # Encode the string
    encoded_text= plain_key + PEPPER

    # Create the hash object
    
    return hashlib.sha256(encoded_text.encode()).hexdigest()

    # Get the hexadecimal representation
    

def verify_api_keys(incoming_plain_key,stored_hash_from_db):
    new_hash = generate_api_keys(incoming_plain_key)
    
    return secrets.compare_digest(new_hash,stored_hash_from_db)



 


