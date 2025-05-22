Aim: To Build a radar-based ADAS object validation system with simulated CAN messages and real-time dashboard telemetry.

This project aims to validate radar-based object detection using Python and ROS, simulate vehicle communication over CAN, and send critical ADAS data to a real-time dashboard. It demonstrates system integration skills relevant to automotive validation, embedded systems, and telematics engineering roles.

## Modules
- **radar_processing**: Parse and analyze radar logs (.bag, .h5)
- **can_simulation**: Generate and log simulated CAN messages
- **telemetry**: Upload data to cloud (MQTT or Firebase)
- **dashboard**: Real-time visualization using Dash

Learning Goals:

1.Build the core radar data processing module using Python
2.Simulate CAN communication and integrate with radar processing.
3.Send data to the cloud and visualize in real time.
4.Pull all parts into a working prototype and document it.

Tools:
Python 3.11, ROS, Pandas, Dash, python-can, paho-mqtt, bagpy

## Milestones
- Week 1: Data parsing and CAN simulation
- Week 2: Telemetry and dashboard integration
- Week 3: Validation and testing
	