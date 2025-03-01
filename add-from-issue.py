import subprocess
import os


parts = subprocess.run(["gh", "issue", "view", "837", "-c"], capture_output=True).stdout.split(b"\n--\n")

for info, content in zip(parts[::2], parts[1::2]):
    info_dict = {}
    for line in info.decode().split("\n"):
        key, value = line.split(":\t")
        info_dict[key] = value

    author = info_dict["author"]

    content_lines = [line.strip() for line in content.decode().replace("`", "").strip().split("\n")]
    for i in range(len(content_lines) - 1):
        if content_lines[i].startswith("name:") and content_lines[i + 1].startswith("link:"):
            if not os.path.isfile(f"_data/signed/{author}.yaml"):
                with open(f"_data/signed/{author}.yaml", "w") as f:
                    f.write(content_lines[i] + "\n" + content_lines[i + 1] + "\n")
