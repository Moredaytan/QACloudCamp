from utils.http_methods import Http_methods

"""методы для тестирования различных api"""

base_url = "https://jsonplaceholder.typicode.com"  # базовая URL



class Jsonp_api():


    @staticmethod
    def create_new_post(id):
        json_for_create_new_post = {
                "title": "foo",
                "body": "bar",
                "userId": 2

        }

        post_resource = "/posts"  # ресурс метода post
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_post)
        print(result_post.text)
        return result_post



    @staticmethod
    def get_new_post(self):
        get_resource = "/posts/2"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get



    @staticmethod
    def delete_new_post(id):
        delete_resource = "/posts/2"
        delete_url = base_url + delete_resource
        print(delete_url)
        json_for_delete_new_post = {

        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_new_post)
        print(result_delete.text)
        return result_delete