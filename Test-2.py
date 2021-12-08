import os
from glob import glob

# Решение задачи, результат складывается в файл "test.txt"
def solve_test(labels_dir):
    print("Solve")
    result, dir_path_list = [], []
    for dir in os.listdir(labels_dir):
        path = os.path.join(labels_dir, dir)
        # print(path)
        
        if os.path.isdir(path):
            list_match_file = []
            for file in os.listdir(path):
                
                name = file.split(".")
                if str.lower(name[1]) in ["jpg", "jpeg", "png"]:
                    print(name)
                # print(f"{path}/{name}.*")
                    match = glob (f"{path}/{name[0]}.*")
                    print (match, list_match_file)
                    print(f"{path}/{name[0]}.json")
                    if f"{path}\\{name[0]}.json" in match and match not in list_match_file:
                        list_match_file.append(match)
                    
            if len(list_match_file) != 0:
                result.append(
                    {
                        dir: list_match_file
                    }
                )
    
    for label in result:
        with open(f"{labels_dir}/test.txt", "a") as file:
            file.write(str(label) + "\n")

# Исходные данные
def start_task():
    labels_dir = "/tmp/labels"
    os.makedirs(labels_dir, exist_ok=True)
    labels = {
        "label1": ["1image.JPG", "2.jpeg", "2.json", "1image.json", "3.jpg"],
        "label2": ["1.jpg", "1.json", "2.json", "3.json"],
        "label3": ["15.png", "15.json", "16.json", "16.jpg", "1.PNG", "1.JSON"],
        "label4": ["1.png", "1.txt", "2.txt", ],
    }
    for label in labels:
        label_path = os.path.join(labels_dir, label)
        os.makedirs(label_path, exist_ok=True)
        for item in labels[label]:
            open(os.path.join(label_path, item), 'a').close()
        print(f"{label_path} {os.listdir(label_path)}")
    open(os.path.join(labels_dir, "test.txt"), 'a').close()
    return labels_dir

if __name__ == "__main__":
    solve_test(start_task())
    # solve_test("/tmp/labels")



