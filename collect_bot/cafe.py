from dataclasses import dataclass, field
import datetime
import geo_util


@dataclass
class Cafe:
    data_id: str
    data_type: str
    name: str
    x: str
    y: str
    _id: str = ""
    parcel_addr: str = ""
    road_addr: str = ""
    phone: str = ""
    tags: dict = field(default_factory=dict)
    location: dict = field(default_factory=dict)
    create_dt: datetime.date = datetime.datetime.utcnow()
    update_dt: datetime.date = datetime.datetime.utcnow()

    def __post_init__(self):
        self._id = f"{self.data_type}-{self.data_id}"
        (lon, lat) = geo_util.GeoUtil.transform_location(self.x, self.y)
        self.location = {
            "type": "Point",
            "coordinates": [
                lon, lat
            ]
        }

        self.valid()

    def valid(self):
        if self._id == "":
            raise Exception("not exist id", self)
        if self.name == "":
            raise Exception("not exist name", self)
        if self.location is None:
            raise Exception("not exist location", self)


if __name__ == "__main__":
    print(Cafe(data_id="id-1234", data_type="sample", name="sample", x="196078.0075", y="442261.8928"))
