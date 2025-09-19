import unittest
from solution import bump_version

class TestBumpVersion(unittest.TestCase):
    def test_existing_version_increment(self):
        self.assertEqual(bump_version("report_v1.csv"), "report_v02.csv")
        self.assertEqual(bump_version("log_v09.txt"), "log_v10.txt")
        self.assertEqual(bump_version("data_v99.json"), "data_v100.json")

    def test_no_version_addition(self):
        self.assertEqual(bump_version("summary.csv"), "summary_v01.csv")
        self.assertEqual(bump_version("notes.txt"), "notes_v01.txt")

    def test_preserve_extension(self):
        self.assertTrue(bump_version("image_v2.png").endswith(".png"))
        self.assertTrue(bump_version("draft.docx").endswith(".docx"))

    def test_multiple_digits_padding(self):
        self.assertEqual(bump_version("archive_v007.zip"), "archive_v008.zip")
        self.assertEqual(bump_version("archive_v099.zip"), "archive_v100.zip")

    def test_edge_cases(self):
        self.assertEqual(bump_version("report_v0.csv"), "report_v01.csv")
        self.assertEqual(bump_version("file.with.dots_v2.tar.gz"), "file.with.dots_v03.tar.gz")

if __name__ == "__main__":
    unittest.main()
