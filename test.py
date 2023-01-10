
import requests, unittest, csv 
from unittest.mock import patch, Mock
from run import app
from write import write_csv
from bs4 import BeautifulSoup 

class TestGoogleScraper(unittest.TestCase):

    home = app.test_client()

    def test_1_conection(self):

        '''test connection and that HTML returns actual data'''

        response = self.home.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'form' in response.data)

    @patch('run.requests')
    def test_2_handle_message(self, mock_request):

        '''mock requests without sending actual HTTP request every time the test is run'''

        mock_response = Mock(status_code=200)
        mock_request = mock_response.status_code 
        self.assertEqual(mock_request, 200)

    def test_3_beautifulSoup(self):

        '''test beautifulSoup on preset/predictable data'''

        response_text = '''<html><body>
                           <div class="BNeawe UPmit AP7Wnd">Sample Search Result 1</div>
                           <div class="BNeawe UPmit AP7Wnd">Sample Search Result 2</div>
                           <div class="BNeawe UPmit AP7Wnd">Sample Search Result 3</div>
                           </body></html>
                        '''
        soup = BeautifulSoup(response_text, features='lxml')
        results = soup.findAll(attrs={'class' : 'BNeawe UPmit AP7Wnd'})
        self.assertEqual(len(results), 3)

class TestWriteFile(unittest.TestCase):

    def test_4_write_file(self):

        '''test write_csv function that will record all our search data'''

        data = ['website', 'www.website.com', 'We talk about website']
        write_csv(data)

        with open('google_search_data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            data_list = next(csv_reader)

        self.assertEqual(data, data_list)

if __name__ == '__main__':
    unittest.main()