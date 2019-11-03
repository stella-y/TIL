## python callback 참고
https://mingrammer.com/translation-asynchronous-python/#%EC%B0%A8%EA%B7%BC-%EC%B0%A8%EA%B7%BC-%EC%82%B4%ED%8E%B4%EB%B3%B4%EA%B8%B0
https://stackoverflow.com/questions/40843039/how-to-write-a-simple-callback-function
https://gist.github.com/mchung/76d774879245b355e8bff95f9172f9f8
```python
def handle_response(response):
	if response.error:
		print('error')
	else:
		url=response.request.url
		data=response.body
		print('{}: {} bytes: {}'.format(url, len(data), data))
http_client=AsyncHTTPClient()

for url in urls:
	http_client.fetch(url, handle_response)
```
