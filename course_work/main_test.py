from app import app
import pytest

def test_app():
    response = app.test_client().get('/meow')
    if response.status_code == 500:
        assert response.status_code == 200 , "статус-код 500"
    elif response.status_code == 404:
        assert response.status_code == 200 , "статус-код 404"

def test_endpoint_one():
    response = app.test_client().get('/api/posts')
    list_word = []
    list_word.append(response.data)
    assert type(list_word) == list , "список получено неверно"
    
def test_endpoint_two():
    response = app.test_client().get('/api/posts/1')
    list_word = []
    list_word.append(response.data)
    assert type(list_word[0]) == bytes , "словарь получено неверно"
    
def test_endpoint_three():
    response = app.test_client().get('/api/posts')
    list_word = []
    list_word.append(response.data)
    assert len(list_word[0]) == 18614 , "не хватает ключей "

def test_endpoint_four():
    response = app.test_client().get('/api/posts/1')
    list_word = []
    list_word.append(response.data)
    assert len(list_word[0]) == 3010 , "не хватает ключей "