import json
import os


class DataService:

    FILE = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "data.json"
    )

    def get_all(self):
        try:
            with open(
                self.FILE,
                "r",
                encoding="utf8"
            ) as f:

                return json.load(f)

        except:
            return []
        
    def add(self, item):

        data = self.get_all()

        next_id = 1

        if len(data) > 0:
            next_id = max(
                x["id"] for x in data
            ) + 1

        item["id"] = next_id

        data.append(item)

        with open(
            self.FILE,
            "w",
            encoding="utf8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print("Zapisano:", item)
        print("Plik:", self.FILE)
        
    def update_status(self, item_id, new_status):

        data = self.get_all()

        for item in data:

            if item["id"] == item_id:

                item["status"] = new_status
                break

        with open(
            self.FILE,
            "w",
            encoding="utf8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


    def get_available_items(self):

        with open(
            "data/merchandise.json",
            "r",
            encoding="utf8"
        ) as f:
            return json.load(f)