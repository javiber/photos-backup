import os
import subprocess
from datetime import datetime
from pathlib import Path

target = Path.home() / "google_drive" / "photos"

# subprocess.run(f"sudo google-drive-ocamlfuse -o nonempty {target.absolute()}".split())
source = Path("/media/javiber/EOS_DIGITAL/DCIM/100CANON/")

def tqdm(l):
    t = len(l)
    for i, x in enumerate(l):
        print(f"{i}/{t}", end='\r')
        yield x

l = list(os.listdir(source))
for f in tqdm(os.listdir(source)):
    current_source = source / f
    dt = datetime.fromtimestamp(os.path.getctime(current_source))
    current_target = target / str(dt.year) / str(dt.month) / current_source.name
    # __import__("ipdb").set_trace()
    subprocess.run(f"mkdir -p {current_target.parent}".split())
    subprocess.run(f"cp -n {current_source} {current_target}".split())

