import random
import json

from rul import AlchemyMessageFactory, PeeWeeMessageFactory, JsonMessageFactory

FACTORIES = [PeeWeeMessageFactory, AlchemyMessageFactory, JsonMessageFactory]


def main():
    """This is the main function called by the package entry point"""
    factory = random.choice(FACTORIES)

    message = factory().buildMessage()

    max_id = 0
    for msg in message.getMessages():
        print("Message %s" % msg)
        if int(msg["id"]) > max_id:
            max_id = int(msg["id"])
    
    new_subject = "Subj %d" % (max_id + 1)
    new_body = "body %d" % (max_id + 1)
    
    message.postMessage(new_subject, new_body)
    message.saveMessagesToFile()
    
if __name__ == "__main__":
    main()
