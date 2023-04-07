import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--topic")


args = parser.parse_args()

topic = args.topic

print(topic)

