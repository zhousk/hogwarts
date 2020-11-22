import yaml


class DataUtils:
    def load_data(self, path):
        with open(path,encoding="utf-8") as f:
            return yaml.load(f,Loader=yaml.FullLoader)


if __name__ == "__main__":
    print(DataUtils().load_data("../data/contact.yaml"))
