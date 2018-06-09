#!/usr/bin python

import base64

def decrypt_message(encrypted_message, google_user):
  encrypted_message_b64 = base64.b64decode(encrypted_message)
  google_user *= (1 + len(encrypted_message) / len(google_user))
  return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(encrypted_message_b64, google_user))

message = "GkkHHQwNHAMeTlJbTkMGHBEJG0lVUEoKHQ0CAQAJAQ1ITkNQSgwBFQsBDAsQT0NOXhULDx0TGhdG Tk5ISAcXEx8MFggMCARJWEhIDxoYBAwEBAMBDxpTSFVOXgUDBR0CBQEFSVhISBwYEg8ABhJJRFtO UxsOCBxXQUlVBwELRk5OSEgZEB5MTg8="
user = "anthonypmirand"
print decrypt_message(message, user)

'''
{
  'success' : 'great',
  'colleague' : 'esteemed',
  'efforts' : 'incredible',
  'achievement' : 'unlocked',
  'rabbits' : 'safe',
  'foo' : 'win!'
}
'''
