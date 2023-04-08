import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--topic")


args = parser.parse_args()

topic = args.topic

if not topic:
    print("Please mention topic name  : --topic topicName")
    print("Exiting!")
    raise SystemExit(1)
    
# print("Topic name-> ",args.topic)
print("Creating the topic : ", args.topic)

cmd = "./kafka-topics.sh --create --topic {} --bootstrap-server localhost:9092".format(topic)

os.chdir('/usr/local/kafka/bin')
os.system(cmd)
# print("Topic {} created successfully!".format(topic))