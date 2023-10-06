import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_generic_item(self):
        items = [Item("Generic Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Generic Item", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("Generic Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 5, 25)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(26, items[0].quality)

    def test_backstage_passes_increase_by_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(32, items[0].quality)

    def test_backstage_passes_increase_by_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(33, items[0].quality)

    def test_backstage_passes_quality_drops_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured_item(self):
        items = [Item("Conjured Mana Cake", 5, 15)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(13, items[0].quality)


if __name__ == "__main__":
    unittest.main()
