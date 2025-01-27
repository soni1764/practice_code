import requests

d = {
    "operation": "add",
    "num1": 10,
    "num2": 5
}
res = requests.post("http://127.0.0.1:5000/calculate", json=d)
print(res.status_code)
print(res)
print(res.json())
