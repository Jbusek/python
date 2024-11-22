import unittest
from television import Television


class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.tv = Television()

    def test_initial_state(self):
        self.assertFalse(self.tv._Television__status)
        self.assertFalse(self.tv._Television__muted)
        self.assertEqual(self.tv._Television__volume, Television.MIN_VOLUME)
        self.assertEqual(self.tv._Television__channel, Television.MIN_CHANNEL)

    def test_power(self):
        self.tv.power()
        self.assertTrue(self.tv._Television__status)
        self.tv.power()
        self.assertFalse(self.tv._Television__status)

    def test_mute(self):
        self.tv.power()
        self.tv.mute()
        self.assertTrue(self.tv._Television__muted)
        self.tv.mute()
        self.assertFalse(self.tv._Television__muted)

    def test_channel_up(self):
        self.tv.power()
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, 1)
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, 2)
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, 3)
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, Television.MIN_CHANNEL)

    def test_channel_down(self):
        self.tv.power()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, 1)
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, 0)
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, Television.MAX_CHANNEL)

    def test_volume_up(self):
        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, 1)
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, 2)
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, Television.MAX_VOLUME)

    def test_volume_down(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, 1)
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, 0)
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, Television.MIN_VOLUME)

    def test_mute_volume_interaction(self):
        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, 1)
        self.tv.mute()
        self.assertTrue(self.tv._Television__muted)
        self.tv.volume_up()
        self.assertFalse(self.tv._Television__muted)
        self.assertEqual(self.tv._Television__volume, 2)

    def test_str_method(self):
        self.tv.power()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")
        self.tv.channel_up()
        self.tv.volume_up()
        self.assertEqual(str(self.tv), "Power = True, Channel = 1, Volume = 1")
        self.tv.mute()
        self.assertEqual(str(self.tv), "Power = True, Channel = 1, Volume = 0")
        self.tv.power()
        self.assertEqual(str(self.tv), "Power = False, Channel = 1, Volume = 0")


if __name__ == "__main__":
    unittest.main()
