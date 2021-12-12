from azure.eventhub import EventHubConsumerClient, PartitionContext, EventData


class EHListener:
    """
    Create a Event Hub consumer to consume messages
    """
    def __init__(self, config):
        self.connection_string = config["connection_string"]
        self.consumer_group = config["consumer_group"]
        self.eventhub_name = config["eventhub_name"]
        self.eh_consumer_client = EventHubConsumerClient.from_connection_string(
                                                            conn_str=self.connection_string,
                                                            consumer_group=self.consumer_group,
                                                            eventhub_name=self.eventhub_name)

        self.eh_consumer_client.receive(self.on_receive)

    @staticmethod
    def on_receive(partition_context: PartitionContext, event: EventData):
        print(partition_context)
        print(event)



if __name__ == "__main__":
    config = {}
    #config["connection_string"] = "Endpoint=sb://ihsuprodblres073dednamespace.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=09PoOq5L+MRVd+0ecaPKto19MR6tCqI0+444l90uSqg=;EntityPath=iothub-ehub-linear-sen-16182762-5414f3deef"
    #config["consumer_group"] = "$Default"
    #config["eventhub_name"] = "iothub-ehub-linear-sen-16182762-5414f3deef"
    #config["connection_string"] = "Endpoint=sb://test-custom-ep.servicebus.windows.net/;SharedAccessKeyName=iothubroutes_linear-sensor;SharedAccessKey=KYRHyGpLejiRxvrMapMI++w6RzYPmFEUwY48vUQa9ow=;EntityPath=event-hub-iot"
    #config["consumer_group"] = "$Default"
    #config["eventhub_name"] = "event-hub-iot"
    #device = EHListener(config)

