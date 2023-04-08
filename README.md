# Basic Kafka Usecase

This repository showcases the basic usecase of kafka in a bare minimum setup. 
Feel free to use the module, experiment with it features and suggest changes.

## Prerequite : 
Please install and configure the config files for Apache Kafka and Zookeeper in your Ubuntu system before going ahead with this setup.
1. Install Kafka : [Link](https://kafka.apache.org/downloads)
2. Install Zookeeper : [Link](https://zookeeper.apache.org/releases.html)


## Contribution guidelines
The repository has 4 branches : 
1. Main
2. Topic
3. Producer
4. Consumer


# Running the setup 
Do ensure that before running the producer, consumers from this repository, your kafka.service and zookeerper.service should be in running state. 

For the purpose of feature addition, please switch to specific branch before adding your code changes.

# Expected feature additions
1. Adding a script 'setup.py' for automatic kafka and zookeeper installation.
2. replace the module 'os' with 'subprocess' within the scripts.


Thanks!