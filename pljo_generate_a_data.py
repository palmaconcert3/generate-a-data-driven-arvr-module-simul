import os
import random
import math
import json
from datetime import datetime

class DataDrivenARVRModuleSimulator:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            return json.load(f)

    def generate_data(self):
        data = {
            "timestamp": datetime.now().isoformat(),
            "sensors": self.generate_sensors_data(),
            "scene": self.generate_scene_data(),
            "user_input": self.generate_user_input_data()
        }
        return data

    def generate_sensors_data(self):
        sensors = {}
        for sensor in self.config["sensors"]:
            if sensor["type"] == "accelerometer":
                sensors[sensor["id"]] = {
                    "x": round(random.uniform(-10, 10), 2),
                    "y": round(random.uniform(-10, 10), 2),
                    "z": round(random.uniform(-10, 10), 2)
                }
            elif sensor["type"] == "gyroscope":
                sensors[sensor["id"]] = {
                    "x": round(random.uniform(-5, 5), 2),
                    "y": round(random.uniform(-5, 5), 2),
                    "z": round(random.uniform(-5, 5), 2)
                }
            elif sensor["type"] == "magnetometer":
                sensors[sensor["id"]] = {
                    "x": round(random.uniform(-100, 100), 2),
                    "y": round(random.uniform(-100, 100), 2),
                    "z": round(random.uniform(-100, 100), 2)
                }
        return sensors

    def generate_scene_data(self):
        scene = {
            "objects": []
        }
        for obj in self.config["scene"]["objects"]:
            obj_data = {
                "id": obj["id"],
                "type": obj["type"],
                "position": {
                    "x": round(random.uniform(-10, 10), 2),
                    "y": round(random.uniform(-10, 10), 2),
                    "z": round(random.uniform(-10, 10), 2)
                },
                "rotation": {
                    "x": round(random.uniform(-180, 180), 2),
                    "y": round(random.uniform(-180, 180), 2),
                    "z": round(random.uniform(-180, 180), 2)
                }
            }
            scene["objects"].append(obj_data)
        return scene

    def generate_user_input_data(self):
        user_input = {
            "touch": {
                "x": round(random.uniform(0, 1), 2),
                "y": round(random.uniform(0, 1), 2)
            }
        }
        return user_input

    def run_simulation(self):
        data = self.generate_data()
        print(json.dumps(data, indent=4))

if __name__ == "__main__":
    simulator = DataDrivenARVRModuleSimulator('config.json')
    simulator.run_simulation()