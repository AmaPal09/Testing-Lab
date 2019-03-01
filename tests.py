"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get("/")
        self.assertIn(b"Please RSVP", result.data)
        

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        self.assertIn(b"Party Details", result.data)
        self.assertNotIn(b"Please RSVP", result.data)
        

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        
        rsvp_info = {'name': "Mel Melitpolski", 'email': "jane@jane.com"}
        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)
        self.assertIn(b"This is kind of awkward",result.data)
        self.assertNotIn(b"Party Details", result.data)
        

        rsvp_info2 = {'name': "Mel", 'email': "mel@ubermelon.com"}
        result2 = self.client.post("/rsvp", data=rsvp_info2,
                                  follow_redirects=True)
        self.assertIn(b"This is kind of awkward",result2.data)
        self.assertNotIn(b"Party Details", result2.data)

        rsvp_info3 = {'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"}
        result3 = self.client.post("/rsvp", data=rsvp_info3,
                                  follow_redirects=True)
        self.assertIn(b"This is kind of awkward",result3.data)
        self.assertNotIn(b"Party Details", result3.data)

        rsvp_info4 = {'name': "Mel ", 'email': "jane@jane.com"}
        result4 = self.client.post("/rsvp", data=rsvp_info4,
                                  follow_redirects=True)
        self.assertIn(b"Party Details", result4.data)
        self.assertNotIn(b"This is kind of awkward",result4.data)


if __name__ == "__main__":
    unittest.main()
