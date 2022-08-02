from core import storage

s3_teste = storage.S3CloudManager('plaguewielder')

s3_teste.upload('teste.txt')