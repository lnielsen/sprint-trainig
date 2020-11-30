"""Data descriptor exercise

Implement the SystemField.

Documentation: https://docs.python.org/3/howto/descriptor.html
"""

class SystemField:
    # pass


class Record(dict):
    pid = SystemField('id')


# Create a record
rec = Record({'id': 1})

# Access the system field from an instance
assert rec.pid == 1
# Access the system field from the class
assert isinstance(Record.pid, SystemField)
# Set a new value
rec.pid = 2
assert rec['id'] == 2

print("Congratulations you solved the exercise")
