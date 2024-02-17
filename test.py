import json
import requests

# read the file
with open('testing.json', 'r') as file:
    test_data = json.load(file)

for event in test_data:
    data = {
        'book_id': event['book_id'],
        'member_id': event.get('member_id'),
        'date': event['date'],
        'eventtype': event['eventtype'],
    }
    print(f"processing event {data['eventtype']}")
    response = requests.post('http://localhost:8000/handle/', json=data)