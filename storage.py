import os
import tempfile
import argparse
import json

parse = argparse.ArgumentParser()
parse.add_argument("--key", type=str, metavar='key', help="input key name")
parse.add_argument("--val", metavar='value')

arg = parse.parse_args()
key = arg.key

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with tempfile.TemporaryFile()  as f:
    storage = json.loads(f.read())
    if arg.val:
        if not key in storage:
            storage[key] = arg.val
        else:
            storage[key].append(arg.val)
        f.write(json.dumps(storage))
    else:
        if key in storage:
            print(*storage[key], sep=", ")
        else:
            print()
