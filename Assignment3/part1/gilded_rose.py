# -*- coding: utf-8 -*-


class Item:
    """DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def decrease_sell_in(self):
        self.sell_in -= 1

    def increase_quality(self, value=1):
        self.quality = min(50, self.quality + value)

    def decrease_quality(self, value=1):
        self.quality = max(0, self.quality - value)

    def is_expired(self):
        return self.sell_in < 0

    def is_max_quality(self):
        return self.quality >= 50

    def is_min_quality(self):
        return self.quality <= 0

    def update(self):
        if self.name == "Aged Brie":
            self.update_aged_brie()
        elif self.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass()
        elif self.name.startswith("Conjured"):
            self.update_conjured_item()
        else:
            self.update_standard_item()

    def update_aged_brie(self):
        self.increase_quality()
        if self.is_expired():
            self.increase_quality()

    def update_backstage_pass(self):
        self.increase_quality()
        if self.sell_in < 11:
            self.increase_quality()
        if self.sell_in < 6:
            self.increase_quality()
        if self.is_expired():
            self.quality = 0

    def update_conjured_item(self):
        self.decrease_quality(2)
        if self.is_expired():
            self.decrease_quality(2)

    def update_standard_item(self):
        self.decrease_quality()
        if self.is_expired():
            self.decrease_quality()


class GildedRose(object):
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.decrease_sell_in()
            item.update()
