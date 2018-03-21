import csv

class GPDataCSV:
    def __init__(self):
        pass

    def save(self, dt, title_list):
        with open('some.csv', 'a+', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([dt] + title_list)

    def read(self):
        items = []
        with open('some.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for item in reader:
                items.append(item)

        size = 7 if len(items) > 6 else len(items)
        #print(size)
        results = []
        for i in range(size):
            results.append(items.pop())
        #print(results)

        return results

if __name__ == "__main__":
    d = GPDataCSV()
    data = d.read()
