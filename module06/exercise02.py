from threading import Thread

data: int = 0


def task(name: str):
    global data
    print(f"Thread ({name}) is running the task")
    for i in range(0, 1_000_000):
        local = data
        local += 1
        if i % 100_000 == 0:
            print(f"Thread ({name}): data={data}")
        data = local
    print(f"Thread ({name}) is completed: {data}")


print("Application is just started.")
threads: list[Thread] = []
for i in range(1, 10):
    t = Thread(target=task, args=(f"t{i}",))
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Application is just completed: {data}")
"""
Application is just completed: 2888428
Application is just completed: 3441105
Application is just completed: 3206465
Application is just completed: 3030215
"""