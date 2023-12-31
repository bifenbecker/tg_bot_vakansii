import requests
from requests import Response


class ApiClient:
    base_url = "url"
    endpoints = []

    def add_item(self):
        self.en


class Api:

    def __init__(self, url: str):
        self.url = url

    def get(self, params=None,
            data=None,
            headers=None,
            cookies=None,
            files=None,
            auth=None,
            timeout=None,
            allow_redirects=True,
            proxies=None,
            hooks=None,
            stream=None,
            verify=None,
            cert=None,
            json=None) -> Response:
        return requests.get(url=self.url, params=params,
                            data=data,
                            headers=headers,
                            cookies=cookies,
                            files=files,
                            auth=auth,
                            timeout=timeout,
                            allow_redirects=allow_redirects,
                            proxies=proxies,
                            hooks=hooks,
                            stream=stream,
                            verify=verify,
                            cert=cert,
                            json=json)

    def post(self, params=None,
             data=None,
             headers=None,
             cookies=None,
             files=None,
             auth=None,
             timeout=None,
             allow_redirects=True,
             proxies=None,
             hooks=None,
             stream=None,
             verify=None,
             cert=None,
             json=None) -> Response:
        return requests.post(url=self.url, params=params,
                             data=data,
                             headers=headers,
                             cookies=cookies,
                             files=files,
                             auth=auth,
                             timeout=timeout,
                             allow_redirects=allow_redirects,
                             proxies=proxies,
                             hooks=hooks,
                             stream=stream,
                             verify=verify,
                             cert=cert,
                             json=json)

    def put(self, params=None,
            data=None,
            headers=None,
            cookies=None,
            files=None,
            auth=None,
            timeout=None,
            allow_redirects=True,
            proxies=None,
            hooks=None,
            stream=None,
            verify=None,
            cert=None,
            json=None) -> Response:
        return requests.put(url=self.url, params=params,
                            data=data,
                            headers=headers,
                            cookies=cookies,
                            files=files,
                            auth=auth,
                            timeout=timeout,
                            allow_redirects=allow_redirects,
                            proxies=proxies,
                            hooks=hooks,
                            stream=stream,
                            verify=verify,
                            cert=cert,
                            json=json)

    def patch(self, params=None,
              data=None,
              headers=None,
              cookies=None,
              files=None,
              auth=None,
              timeout=None,
              allow_redirects=True,
              proxies=None,
              hooks=None,
              stream=None,
              verify=None,
              cert=None,
              json=None) -> Response:
        return requests.patch(url=self.url, params=params,
                              data=data,
                              headers=headers,
                              cookies=cookies,
                              files=files,
                              auth=auth,
                              timeout=timeout,
                              allow_redirects=allow_redirects,
                              proxies=proxies,
                              hooks=hooks,
                              stream=stream,
                              verify=verify,
                              cert=cert,
                              json=json)

    def delete(self, params=None,
               data=None,
               headers=None,
               cookies=None,
               files=None,
               auth=None,
               timeout=None,
               allow_redirects=True,
               proxies=None,
               hooks=None,
               stream=None,
               verify=None,
               cert=None,
               json=None) -> Response:
        return requests.delete(url=self.url, params=params,
                               data=data,
                               headers=headers,
                               cookies=cookies,
                               files=files,
                               auth=auth,
                               timeout=timeout,
                               allow_redirects=allow_redirects,
                               proxies=proxies,
                               hooks=hooks,
                               stream=stream,
                               verify=verify,
                               cert=cert,
                               json=json)
