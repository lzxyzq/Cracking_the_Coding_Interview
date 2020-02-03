import hashlib
# To learn more about the hashlib module read 
# https://docs.python.org/3/library/hashlib.html
# This module is part of teh Python Standard library
# as per https://docs.python.org/3.7/library/

md5 = hashlib.md5(b'Nobody inspects the spammish repetition').hexdigest()
sha1 = hashlib.sha1(b'Nobody inspects the spammish repetition').hexdigest()
sha224 = hashlib.sha224(b'Nobody inspects the spammish repetition').hexdigest()
sha256 = hashlib.sha256(b'Nobody inspects the spammish repetition').hexdigest()

# OUTPUT
print('{:7} | {:64} | {:3}'.format("Hashing","Check Sum", "Length"))
print('{:7} | {:64} | {:3}'.format("md5", md5, len(md5)))
print('{:7} | {:64} | {:3}'.format("sha1", sha1, len(sha1)))
print('{:7} | {:64} | {:3}'.format("sha224", sha224, len(sha224)))
print('{:7} | {:64} | {:3}'.format("sha256", sha256, len(sha256)))

# hash()
list(map(hash,(1,2,3)))
list(map(hash,("names","namb")))