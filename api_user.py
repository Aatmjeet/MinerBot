import requests
import steamsignin
import webbrowser

if __name__ == "__main__":
    hwid = "Bullshit hardware ID"
    url_data = f"http://0.0.0.0:5000/login/{hwid}"
    url_data = requests.get(url_data).json()
    if url_data["status"]:
        webbrowser.open(url_data['data']['URL'])
        print(f"please verify account.")
    else:
        print("FAILED")
