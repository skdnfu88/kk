import zlib, base64
exec(zlib.decompress(base64.b64decode(b'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')))
