import time
import json
from azure.iot.device import IoTHubModuleClient, MethodRequest, MethodResponse, ProvisioningDeviceClient

from sensor import Linear_Sensor
import uuid


class Device:
    """
        A device that connects with theazure iot-hub
    """
    def __init__(self, config):
        self.device = ProvisioningDeviceClient.create_from_symmetric_key(
            provisioning_host="global.azure-devices-provisioning.net", 
            registration_id="rajat-123-456",
            id_scope="0ne004518BA",
            symmetric_key="sfT4dQsywba7sLPNZ83dj7UHw52n2FyOh7vlyCa4cTxhYl1F51yGPnPh7+wU/kMlXDAGd8Zvq1LsA/OXDJRv2w==")
        self.device.register()
        #self.connection_string = config["connection_string"]
        #self.hub_client = IoTHubModuleClient.create_from_connection_string(self.connection_string)
        #self.initialize_hub()

        #self.linear_sensor = Linear_Sensor()
        #self.initialize_sensor()

    def initialize_hub(self):
        self.hub_client.connect()
        self.hub_client.on_method_request_received = self.on_message_received(self.hub_client)

    def initialize_sensor(self):
        while True:
            x, y = self.linear_sensor.gen_data()

            data = str({
                "x": x,
                "y": y
            })
            print(f"Data send. {data}")
            self.hub_client.send_message(data)
            time.sleep(5.0)
        
    @staticmethod
    def on_message_received(client: IoTHubModuleClient):
        print("on_message")
        def create_response(request_id, status, data):
            return MethodResponse(
                request_id,
                status,
                data
            )

        def _func(method_request: MethodRequest):
            if method_request.name == "ping":
                print(f"ping received from IoT Hub")
                status = 200
                data = "ping received!"
                response = create_response(method_request.request_id, status, data)
                client.send_method_response(response)
            

        return _func
        



if __name__ == "__main__":
    config = {}
    #config["connection_string"] = "HostName=linear-sensor.azure-devices.net;DeviceId=test;SharedAccessKey=FKje22ODC5ltzA+8iJoo6ctCyFzBSoPdNzJdUr8mgYo="
    device = Device(config)
