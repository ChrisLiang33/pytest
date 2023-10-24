import pytest
import service
import unittest.mock as mock


@mock.patch('service.get_user_from_db')
def test_get_user_from_db(mock_get_user_from_db):
  mock_get_user_from_db.return_value = 'Mocked bob'
  user_name = service.get_user_from_db(2)
  assert user_name == 'Mocked bob'
    
@mock.patch('requests.get')
def test_gt_users(mock.get):
  mock_response = mock.Mock()
  mock_response.status_code = 200
  mock_response.json.return_value = {'id':1,'name':'john'}
  mock_get.return_value = mock_response
  data = service.get_users()
  assert data == {'id':1, 'name':'john doe'}
  
