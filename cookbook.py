import json
import pickle

# Serialization using JSON
data = {"name": "John", "age": 30}
json_serialized = json.dumps(data)
print(json_serialized)  # Outputs: {"name": "John", "age": 30}

# Deserialization using JSON
json_deserialized = json.loads(json_serialized)
print(json_deserialized)  # Outputs: {'name': 'John', 'age': 30}

# Serialization using Pickle
pickle_serialized = pickle.dumps(data)
print(pickle_serialized)  # Outputs: b'\x80\x04\x95\x1f\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x04John\x94\x8c\x03age\x94K\x1eu.'

# Deserialization using Pickle
pickle_deserialized = pickle.loads(pickle_serialized)
print(pickle_deserialized)  # Outputs: {'name': 'John', 'age': 30}