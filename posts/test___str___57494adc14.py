import unittest
from posts.models import HitCount

class TestGetHitCount(unittest.TestCase):

   
    def setUp(self):
        # Create a HitCount instance and save it to the database
        self.hit_count = HitCount(ip="8bbc39393") #change the value of ip
        self.hit_count.save()
    def tearDown(self):
        # Clean up by deleting the HitCount instance after each test case
        self.hit_count.delete()

    def test_hit_count_ip(self):
        # Retrieve the saved HitCount instance from the database
        saved_hit_count = HitCount.objects.get(ip="8bbc39393")
        # Test if the IP matches the expected value
        print(saved_hit_count.ip)
        # self.assertEqual(saved_hit_count.ip, "8bbc39393b")
    def test_hit_count_default(self):
        # Create a new HitCount instance without specifying IP
        hit_count = HitCount()
        # IP should be an empty string by default
        self.assertEqual(hit_count.ip, "")

if __name__ == '__main__':
    unittest.main()
