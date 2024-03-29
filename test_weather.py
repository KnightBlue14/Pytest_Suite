import pytest
import Weather_noSQL
import requests
import unittest.mock as mock

@mock.patch('requests.get')
def test_api_status_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        Weather_noSQL.status_check()

def test_frame_gen_size():
    assert len(Weather_noSQL.df4) == 1
    assert len(Weather_noSQL.df4.columns) == 32
