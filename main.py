import webbrowser, time
url = input("Enter Youtube URL: ")
duration = int(input("Enter Duration (The amount of seconds that you want to stay on the page for) (MUST BE INT): "))
times = int(input("Enter amount of times to run (MUST BE INT): "))
try:
    for i in range(times):
        webbrowser.open_new(url)
        time.sleep(int(duration))
except Exception as e:
    print("Internal Error: " + str(e))
    time.sleep(5)
