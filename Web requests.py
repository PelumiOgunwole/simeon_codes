import requests
"""A Response is a powerful object for inspecting the results of the request."""
response=requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(response.status_code)
print(len(response.text))
print(response.text[:250])
"""Always use raise_for_status() after requests.get()"""
print(response.raise_for_status())
"To save the web content to a file, open it as a binary content 'wb'"
with open('RomeoAndJuliet.txt', 'wb') as f:
    for chunk in response.iter_content(100000):#iter_content() method returns “chunks” of the content on eachiteration through the loop with no of nbytes in bracket
        f.write(chunk)
    print(f)

"""
How to use Requests Library

1. Call requests.get() to download the file.
2. Call open() with 'wb' to create a new file in write binary mode.
3. Loop over the Response object’s iter_content() method.
4. Call write() on each iteration to write the content to the file.
5. Call close() to close the file.
"""