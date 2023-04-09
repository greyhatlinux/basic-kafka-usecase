import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--topic")
parser.add_argument("--topics", nargs="+")
parser.add_argument("--name")

args = parser.parse_args()

name = args.name
topic = args.topic
topics = args.topics

n_topics = 0
all_topics = ""
if topics:
    n_topics = len(topics)
    for i in range(n_topics):
        all_topics += topics[i] + "|"

# print(all_topics)

if not topic and not topics:
    print("Please mention topic(s) name")
    raise SystemExit(1)

if not name:
    print("Please mention consumer name")
    raise SystemExit(1)
    
# print("Topic name-> ",args.topic)
print("Creating consumer to the topic(s) : ", args.topic)

if n_topics == 0:
    cmd = "./kafka-console-consumer.sh --topic {} --bootstrap-server localhost:9092".format(topic)
else:
    cmd = "./kafka-console-consumer.sh --include '{}' --bootstrap-server localhost:9092".format(all_topics)

os.chdir('/usr/local/kafka/bin')
os.system('clear')
print("Consumer '{}' is receiving messages :".format(name))
os.system(cmd)