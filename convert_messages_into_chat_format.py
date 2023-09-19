from pathlib import Path
import json

root_folder = Path("/home/tom/Downloads/facebook/messages/inbox/user_123456789")
output_file = root_folder / "concatenated_messages.txt"
message_files = list(root_folder.glob("message_*.json"))
messages = []


def parse_obj(obj):
    if isinstance(obj, str):
        return obj.encode('latin_1').decode('utf-8')

    if isinstance(obj, list):
        return [parse_obj(o) for o in obj]

    if isinstance(obj, dict):
        return {key: parse_obj(item) for key, item in obj.items()}

    return obj


for message_file in message_files:
    with open(message_file) as message_f:
        message_s = message_f.read()
    data = parse_obj(json.loads(message_s))
    messages.extend(data["messages"])

messages = sorted(messages, key=lambda message: message["timestamp_ms"])

with open(output_file, "w+") as f:
    for message in messages:
        if "sender_name" in message and "content" in message:
            f.write(f"{message['sender_name']}:\n")
            f.write(message["content"])
            f.write("\n\n")
