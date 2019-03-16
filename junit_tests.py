from unittest import TestCase
import txt
import img
import os

pathTxt = 'text/'
pathImg = 'images/'
url = 'https://a-achell.com/test/test.html'
testImg = img.Scraper()
testTxt = txt.Text()

class TestScraper(TestCase):

    def test_get_img(self):
        self.assertEqual(testImg.get_img(url), {'winter_cat.jpg': 'images/winter_cat.jpg'})

    def test_download_img(self):
        self.assertEqual(testImg.download_img(url), ['test.html', 'images/test.html'])
        os.remove('images/test.html')

    def test_delete_img(self):
        file = pathImg+'winter_cat.jpg'
        testImg.delete_img(file)
        self.assertFalse(os.path.exists(file))

    def test_check_fs_img(self):
        testImg.get_img(url)
        testData = testImg.check_fs_img()
        self.assertTrue('winter_cat.jpg' in testData.keys())

    def test_update_img(self):
        testImg.get_img(url)
        file = pathImg + 'winter_cat.jpg'
        testData = {'winter_cat.jpg': 'images/winter_cat.jpg'}
        testImg.delete_img(file)
        testImg.update_img(testData)
        self.assertFalse('winter_cat.jpg' in testData.keys())

class TestText(TestCase):
    def test_get_text(self):
        self.assertEqual(testTxt.get_text(url), {'test.txt': 'text/test.txt'})

    def test_delete_text(self):
        file = pathTxt+'test.txt'
        testTxt.delete_text(file)
        self.assertFalse(os.path.exists(file))

    def test_check_fs_text(self):
        testTxt.get_text(url)
        testData = testTxt.check_fs_text()
        self.assertTrue('test.txt' in testData.keys())

    def test_update_text(self):
        testTxt.get_text(url)
        file = pathTxt + 'test.txt'
        testData = {'test.txt': 'text/test.txt'}
        testTxt.delete_text(file)
        testTxt.update_text(testData)
        self.assertFalse('test.txt' in testData.keys())
