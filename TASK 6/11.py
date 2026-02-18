
import os

class FileManager:
    @staticmethod
    def ensure_directory(directory_path):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Created directory: {directory_path}")
        else:
            print(f"Directory already exists: {directory_path}")

    @staticmethod
    def save_file(file_path, content):
        directory = os.path.dirname(file_path)
        FileManager.ensure_directory(directory)
        with open(file_path, "w") as f:
            f.write(content)
        print(f"File saved at: {file_path}")


def main():
    dataset_dir = "datasets/experiment1"
    file_path = f"{dataset_dir}/data.txt"
    content = "Sample dataset content"
    FileManager.save_file(file_path, content)

    nested_file_path = "datasets/experiment1/results/result1.txt"
    FileManager.save_file(nested_file_path, "Result data here")

    new_dataset_path = "datasets/experiment2/data.txt"
    FileManager.save_file(new_dataset_path, "Experiment 2 dataset")

if __name__ == "__main__":
    main()