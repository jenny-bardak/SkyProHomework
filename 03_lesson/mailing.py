from address import Address  # импорт класса для связки


class Mailing:
    def __init__(self, to_address: Address, from_address: Address,
                 cost: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
