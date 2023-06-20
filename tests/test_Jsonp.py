from requests import Response

from tests.api import Jsonp_api



class Test_create_place():

    def test_create_new_post(self):

        print("Метод post")
        result_post = Jsonp_api.create_new_post(id)
        check_post = result_post.json()

        print("Метод get")
        result_get = Jsonp_api.get_new_post(id)

        print("Метод delete ")
        result_delete = Jsonp_api.delete_new_post(id)


