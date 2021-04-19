import paho.mqtt.client as mqtt
import json


mqtt_username = "wisense"
mqtt_password = "Wisense@123"
mqtt_topic = "wsn_get_node_access"
mqtt_broker_ip = "18.217.221.246"				#aws ec2 instance static ip, unless the instances wont gets shutdown and restarts again

mqtt_response_topic = "wsn_node_access_response"

verbose = 1

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)

node_macId_1 = "fc:c2:3d:ff:fe:0d:4a:46";
node_macId_2 = "fc:c2:3d:ff:fe:0d:5f:7c";
node_macId_3 = "fc:c2:3d:00:00:00:69:1c";			#mlitson demo SN-egg

nodeMacId1RespMsg = {"macId":"fc:c2:3d:ff:fe:0d:4a:46", "username":"p0lsPBWqHD2AWhmKUlEu"}
nodeMacId2RespMsg = {"macId":"fc:c2:3d:ff:fe:0d:5f:7c", "username":"st8T3pTKQ2LUBWBhCrzk"}
nodeMacId3RespMsg = {"macId":"fc:c2:3d:00:00:00:69:1c", "username":"hWeD9zf8oWnCx4LUxgXr"}


if verbose == 1:
	print("*****************************************************************************************************")
	print("nodeMacId1RespMsg type : ", type(nodeMacId1RespMsg))
	print("nodeMacId1RespMsg macId: ", nodeMacId1RespMsg["macId"], "username: ", nodeMacId1RespMsg["username"])
	print("nodeMacId2RespMsg type : ", type(nodeMacId2RespMsg))
	print("nodeMacId2RespMsg macId: ", nodeMacId2RespMsg["macId"], "username: ", nodeMacId2RespMsg["username"])
	print("nodeMacId3RespMsg type : ", type(nodeMacId3RespMsg))
	print("nodeMacId3RespMsg macId: ", nodeMacId3RespMsg["macId"], "username: ", nodeMacId3RespMsg["username"])
	print("Converting to MSG String Type...")

nodeMacId1RespMsgDump = json.dumps(nodeMacId1RespMsg)
nodeMacId2RespMsgDump = json.dumps(nodeMacId2RespMsg)
nodeMacId3RespMsgDump = json.dumps(nodeMacId3RespMsg)

if verbose == 1:
	print("nodeMacId1RespMsgDump type: ", type(nodeMacId1RespMsgDump))
	print("nodeMacId1RespMsgDUmp Content: ", nodeMacId1RespMsgDump)
	print("nodeMacId2RespMsgDump type: ", type(nodeMacId2RespMsgDump))
	print("nodeMacId2RespMsgDump Content: ", nodeMacId2RespMsgDump)
	print("nodeMacId3RespMsgDump type: ", type(nodeMacId3RespMsgDump))
	print("nodeMacId3RespMsgDump Content: ", nodeMacId3RespMsgDump)
	print("*****************************************************************************************************")

def on_connect(client, userdata, flags, rc):
    # rc - error code
    print "Connected!", str(rc)

    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
  
    print "Topic: ", msg.topic + "\nMessage: " + str(msg.payload)
    if node_macId_1 == msg.payload:
        print("Sending Node access response to wisense coord client !!")
        client.publish(mqtt_response_topic, nodeMacId1RespMsgDump)
    if node_macId_2 == msg.payload:
        print("Sending Node access response to wisense coord client !!")
        client.publish(mqtt_response_topic, nodeMacId2RespMsgDump)
    if node_macId_3 == msg.payload:
	print("Sending Node access response to wisense coord client !!")
	client.publish(mqtt_response_topic, nodeMacId3RespMsgDump)


client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker_ip, 1883)

client.loop_forever()
client.disconnect()
