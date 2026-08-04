from kafka.admin import KafkaAdminClient, NewTopic
from producer.utils.logger import LOGGER

class TopicManager:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.admin_client = KafkaAdminClient(bootstrap_servers=self.bootstrap_servers)

    def create_topic(self, topic_name, num_partitions=1, replication_factor=1):
        try:
            topic_list = [NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)]
            self.admin_client.create_topics(new_topics=topic_list, validate_only=False)
            LOGGER.info(f"Topic '{topic_name}' created successfully.")
        except Exception as e:
            LOGGER.error(f"Failed to create topic '{topic_name}': {e}")

    def delete_topic(self, topic_name):
        try:
            self.admin_client.delete_topics(topics=[topic_name])
            LOGGER.info(f"Topic '{topic_name}' deleted successfully.")
        except Exception as e:
            LOGGER.error(f"Failed to delete topic '{topic_name}': {e}")