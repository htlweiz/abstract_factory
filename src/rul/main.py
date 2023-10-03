""" Main Module

@author Robert Ulmer
"""
import random

from rul import AlchemyMessageFactory, PeeWeeMessageFactory, JsonMessageFactory

FACTORIES = [AlchemyMessageFactory, PeeWeeMessageFactory, JsonMessageFactory]


def main():
    """This is the main function called by the package entry point"""
    factory = random.choice(FACTORIES)

    message = factory().buildMessage()

    max_id = 0
    for msg in message.getMessages():
        print("Message %s" % msg)
        if int(msg["id"]) > max_id:
            max_id = int(msg["id"])
    message.postMessage("Subj %d" % (max_id + 1), "body %d" % (max_id + 1))
