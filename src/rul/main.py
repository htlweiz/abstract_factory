import random
import json  # Add this import for JSON handling

from rul import AlchemyMessageFactory, PeeWeeMessageFactory

FACTORIES = [PeeWeeMessageFactory, AlchemyMessageFactory]


def main():
    """This is the main function called by the package entry point"""
    factory = random.choice(FACTORIES)

    message = factory().buildMessage()

    max_id = 0
    messages = []  # Create an empty list to store messages as dictionaries

    for msg in message.getMessages():
        message_dict = {
            "id": msg["id"],
            "header": msg["header"],
            "body": msg["body"]
        }
        messages.append(message_dict)  # Append each message dictionary to the list
        print("Message %s" % message_dict)
        if int(msg["id"]) > max_id:
            max_id = int(msg["id"])

    new_message_header = "Subj %d" % (max_id + 1)
    new_message_body = "body %d" % (max_id + 1)

    # Post a new message
    message.postMessage(new_message_header, new_message_body)

    new_message_dict = {
        "id": max_id + 1,
        "header": new_message_header,
        "body": new_message_body
    }
    messages.append(new_message_dict)  # Append the new message dictionary

    # Convert the list of message dictionaries to JSON
    json_messages = json.dumps(messages, indent=4)

    # Write the JSON data to a file (optional)
    with open("messages.json", "w") as json_file:
        json_file.write(json_messages)

    # Print the JSON data
    print("JSON representation of messages:")
    print(json_messages)


if __name__ == "__main__":
    main()
