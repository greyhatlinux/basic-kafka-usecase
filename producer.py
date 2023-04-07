import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--topic")
parser.add_argument("--name")

args = parser.parse_args()

topic = args.topic
name = args.name

if not topic:
    print("Please mention topic name")
    raise SystemExit(1)
    
# print("Topic name-> ",args.topic)
print("Creating producer to the topic : ", args.topic)

cmd = "./kafka-console-producer.sh --topic {} --bootstrap-server localhost:9092".format(topic)

os.chdir('/usr/local/kafka/bin')
print("Start sending messages :")
os.system(cmd)