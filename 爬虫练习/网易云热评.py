import requests
import bs4
import json


def get_url(url):
    header = {"usre-agent": "user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 ("
                            "KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36",

              "referer": "https://music.163.com/song?id = 4153366"
              }
    params = "x2MJIbXwzBjR51SuTyehH75VcV0x5aCrg8k0//sgQHY5o2pxLJGEA88edNTcAxMbpz5ifattANZZVC9bqd1t0NlH0aDCGOz" \
             "/vNX1AtPdrW8xAlbe3GILCMuqO40oNsK+fOTLMsi9XThUV4efWftiCX93FTCmK8HriLtUYuLI/GH3AGx00dKA" \
             "+oUkcotHqErw9wmCy6bJuINlMGrAzuzoOC8IuV7k9urR2YIfNDKU9yPW7VXFVz/OhlZ1re7oHTrlM6Hpmls+si5HOOlX8RBXjv" \
             "/GpYmvdFGYFdVOzvm9tXzEKnGOtVA9jpz4uE5JdKC4 "

    encSecKey = "42b4cb7a05dca18937b829bf70cdad3c3e5e2f783668055f435b324993472df7935c965e4624341f29db32eb4c2b5b9c1b2d9b41172ada7add99bb67b2210ab553c1d1b2319d5e85f1c239ae032967cbcea680cb9b4ebb3e60d5fcb60a1427d89528ffb81bde9a540f2c038a62262d823aba5066cd850e922ca5f1b255a5a304 "
    data = {
        "params": params, "encSecKey": encSecKey}
    res = requests.post(url, headers=header, data=data)

    return res


def get_hostcomments(res):
    comments_json = json.loads(res.text)
    print(comments_json)
    '''
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname'] + '：\n\n')
            file.write(each['content'] + '\n')
            file.write("---------------------------------------\n")
            '''


def main():
    url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=b3a11a739155adb8a0266be7275ec6eb"
    res = get_url(url)
    get_hostcomments(res)


if __name__ == "__main__":
    main()
