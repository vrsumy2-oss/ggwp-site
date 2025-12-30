import urllib.request
import json


def test_url(url):
    print(f"\nTesting: {url}")
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf-8"))
        print(f"Count: {len(data)}")
        for item in data:
            print(f"- {item['title']} (ID: {item['id']})")
    except Exception as e:
        print(f"Error: {e}")


base_url = "http://127.0.0.1:8000/api/items/"
test_url(base_url)
test_url(base_url + "?game=dota-2")
test_url(base_url + "?game=cs2")
