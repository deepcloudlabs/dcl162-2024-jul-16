from threading import Thread

data: int = 0


def task(name: str):
    global data
    print(f"Thread ({name}) is running the task")
    for i in range(0, 10_000_000):
        local = data
        local += 1
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
