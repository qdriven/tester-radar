# TODO 

- try: pip install confluent-kafka[avro]


## Send Events:

```bash
echo "{\"requestId\":\"eventId_32553\",\"userId\": \"12345557754324\",\"timestamp\":\"1491819682\",\"userIp\": \"10.0.0.1\"}" | sh bin/kafka-console-producer.sh --broker-list localhost:2181 --topic LoginEvent
```