"""
Definitions of command and error codes as stated in the "Mecom" protocol standard.
https://www.meerstetter.ch/category/35-latest-communication-protocols
"""


PARAMETERS = [
    {"id": 100, "name": "Device Type", "format": "INT32"},
    {"id": 104, "name": "Device Status", "format": "INT32"},
    {"id": 108, "name": "Save Data to Flash", "format": "INT32"},
    {"id": 109, "name": "Flash Status", "format": "INT32"},
    {"id": 1000, "name": "Object Temperature", "format": "FLOAT32"},
    {"id": 1001, "name": "Sink Temperature", "format": "FLOAT32"},
    {"id": 1010, "name": "Target Object Temperature", "format": "FLOAT32"},
    {"id": 1011, "name": "Ramp Object Temperature", "format": "FLOAT32"},
    {"id": 1020, "name": "Actual Output Current", "format": "FLOAT32"},
    {"id": 1021, "name": "Actual Output Voltage", "format": "FLOAT32"},
    {"id": 1046, "name": "Object Sensor Type", "format": "INT32"},
    {"id": 1200, "name": "Temperature is Stable", "format": "INT32"},
    {"id": 2000, "name": "Input Selection", "format": "INT32"},
    {"id": 2010, "name": "Status", "format": "INT32"},
    {"id": 2020, "name": "Set Current", "format": "FLOAT32"},
    {"id": 2021, "name": "Set Voltage", "format": "FLOAT32"},
    {"id": 2030, "name": "Current Limitation", "format": "FLOAT32"},
    {"id": 2031, "name": "Voltage Limitation", "format": "FLOAT32"},
    {"id": 2040, "name": "General Operating Mode", "format": "INT32"},
    {"id": 2051, "name": "Device Address", "format": "INT32"},
    {"id": 3000, "name": "Target Object Temp (Set)", "format": "FLOAT32"},
    {"id": 3010, "name": "Kp", "format": "FLOAT32"}, 
    {"id": 3011, "name": "Ti", "format": "FLOAT32"}, 
    {"id": 3012, "name": "Td", "format": "FLOAT32"},
    {"id": 5000, "name": "Live Enable", "format": "INT32"},
    {"id": 5001, "name": "Live Set Current", "format": "FLOAT32"},
    {"id": 5002, "name": "Live Set Voltage", "format": "FLOAT32"},
    {"id": 5030, "name": "Sink Temperature Selection", "format": "INT32"},
    {"id": 6005, "name": "Sensor Type Selection", "format": "INT32"},
    {"id": 6310, "name": "Delay till Restart", "format": "FLOAT32"},
    {"id": 51000, "name": "Auto Tuning Start", "format": "INT32"},
    {"id": 51014, "name": " PID Parameter Kp", "format": "FLOAT32"}
]

ERRORS = [
    {"code": 1, "symbol": "EER_CMD_NOT_AVAILABLE", "description": "Command not available"},
    {"code": 2, "symbol": "EER_DEVICE_BUSY", "description": "Device is busy"},
    {"code": 3, "symbol": "ERR_GENERAL_COM", "description": "General communication error"},
    {"code": 4, "symbol": "EER_FORMAT", "description": "Format error"},
    {"code": 5, "symbol": "EER_PAR_NOT_AVAILABLE", "description": "Parameter is not available"},
    {"code": 6, "symbol": "EER_PAR_NOT_WRITABLE", "description": "Parameter is read only"},
    {"code": 7, "symbol": "EER_PAR_OUT_OF_RANGE", "description": "Value is out of range"},
    {"code": 8, "symbol": "EER_PAR_INST_NOT_AVAILABLE", "description": "Parameter is read only"},
]
