#!/usr/bin/python env

import unittest
import base

import animalcontrol
import utils

class TestAnimalControl(unittest.TestCase):
   
    nid = 0

    def setUp(self):
        self.nid = animalcontrol.insert_animalcontrol(base.get_dbo(), "test")

    def tearDown(self):
        base.execute("DELETE FROM animalcontrol WHERE ID = %d" % self.nid)

    def test_get_animalcontrol(self):
        assert len(animalcontrol.get_animalcontrol(base.get_dbo(), self.nid)) > 0

    def test_get_animalcontrol_animals(self):
        animalcontrol.get_animalcontrol_animals(base.get_dbo(), self.nid)

    def test_get_aniamlcontrol_for_animal(self):
        animalcontrol.get_animalcontrol_for_animal(base.get_dbo(), 0)

    def test_get_followup_two_dates(self):
        animalcontrol.get_followup_two_dates(base.get_dbo(), base.today(), base.today())

    def test_get_animalcontrol_find_simple(self):
        animalcontrol.get_animalcontrol_find_simple(base.get_dbo(), "test", "user")

    def test_get_animalcontrol_find_advanced(self):
        assert len(animalcontrol.get_animalcontrol_find_advanced(base.get_dbo(), { "number": str(self.nid) }, "user")) > 0

    def test_get_animalcontrol_satellite_counts(self):
        animalcontrol.get_animalcontrol_satellite_counts(base.get_dbo(), self.nid)

    def test_get_active_traploans(self):
        animalcontrol.get_active_traploans(base.get_dbo())

    def test_get_person_traploans(self):
        animalcontrol.get_person_traploans(base.get_dbo(), 0)

    def test_get_traploan_two_dates(self):
        animalcontrol.get_traploan_two_dates(base.get_dbo(), base.today(), base.today())

    def test_update_animalcontrol_completenow(self):
        animalcontrol.update_animalcontrol_completenow(base.get_dbo(), 1, "test", 1)

    def test_update_animalcontrol_dispatchnow(self):
        animalcontrol.update_animalcontrol_dispatchnow(base.get_dbo(), 1, "test")

    def test_update_animalcontrol_respondnow(self):
        animalcontrol.update_animalcontrol_respondnow(base.get_dbo(), 1, "test")

    def test_insert_animalcontrol_from_form(self):
        data = {
            "incidentdate":   "01/01/2014",
            "incidenttime":   "00:00:00"
        }
        post = utils.PostedData(data, "en")
        nid = animalcontrol.insert_animalcontrol_from_form(base.get_dbo(), post, "test", geocode=False)
        animalcontrol.delete_animalcontrol(base.get_dbo(), "test", nid)

    def test_update_animalcontrol_from_form(self):
        data = {
            "incidentdate":   "01/01/2014",
            "incidenttime":   "00:00:00"
        }
        post = utils.PostedData(data, "en")
        animalcontrol.update_animalcontrol_from_form(base.get_dbo(), post, "test", geocode=False)

    def test_insert_traploan_from_form(self):
        data = {
            "person":   "1",
            "type":     "1",
            "loandate": "01/01/2014"
        }
        post = utils.PostedData(data, "en")
        tid = animalcontrol.insert_traploan_from_form(base.get_dbo(), "test", post)
        animalcontrol.delete_traploan(base.get_dbo(), "test", tid)

    def test_update_traploan_from_form(self):
        data = {
            "person":   "2",
            "type":     "2",
            "loandate": "01/01/2014"
        }
        post = utils.PostedData(data, "en")
        animalcontrol.update_traploan_from_form(base.get_dbo(), "test", post)

    def test_update_dispatch_latlong(self):
        animalcontrol.update_dispatch_latlong(base.get_dbo(), self.nid, "54,52")

