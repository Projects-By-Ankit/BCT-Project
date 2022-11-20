import hashlib
from Block import Block as blk

obj = blk("data")
# print(obj.Data)
sha256 = hashlib.sha256(obj.Data.encode("ascii")).hexdigest()
print(sha256)
