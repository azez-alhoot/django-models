from django.test import TestCase

# Create your tests here.
from django.urls import reverse

class SnackTest(TestCase):


    def status_code(self,page_name):
        expected = 200
        url = reverse(page_name)
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected, actual)

    def page_template(self,page_name):
        url = reverse(page_name)
        response = self.client.get(url)
        actual = page_name + '.html'
        self.assertTemplateUsed(response, actual)
        self.assertTemplateUsed(response,'base.html')



    def test_home_page(self): 
        self.status_code('home')

    # def test_detail_page(self): 
    #     self.status_code('post-details')


    def test_templet_home_page(self): 
        self.page_template('home')

    # def test_templet_detail_page(self): 
    #     self.page_template('detail')