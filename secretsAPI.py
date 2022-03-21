CLIENTID = 'c79f8f3e44374b02a328880197d78508'
CLIENTSECRET = '4223f8c46a6f418f97c2d7886c253793'
clienttohash = 'c79f8f3e44374b02a328880197d78508:4223f8c46a6f418f97c2d7886c253793'
client_64hash = 'Yzc5ZjhmM2U0NDM3NGIwMmEzMjg4ODAxOTdkNzg1MDg6NDIyM2Y4YzQ2YTZmNDE4Zjk3YzJkNzg4NmMyNTM3OTM='

redirect_urigoogle = 'https://google.com'
uri_decrypt = 'https%3A%2F%2Fgoogle.com'

spotify_auth_uri = 'https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope=playlist-modify-public%20playlist-modify-private'.format(CLIENTID, uri_decrypt) #skoða scope fyrir private playlista??


#access_code = AQCcGtwdz6qaUl6n4VnJMxzN2lgVbXnMHt-4qKunJEf584vhbUmLRsp8R94jtIkW44DP3AYovZsy72RMP-T-t0ngFeb-_FLrO2-o_QIROeJe7TdX0hM6_3ACSXwQNyQMx-fJG-Z-O0tUfgjR_13snaILLe3sjy9kQvoDIgyxASqgv5EBGHt6UmmTzrhoCEPfaPrDhAfVuXTzrxWZWKxYA87GyS86Bgo
#original
#curl -H "Authorization: Basic Yzc5ZjhmM2U0NDM3NGIwMmEzMjg4ODAxOTdkNzg1MDg6NDIyM2Y4YzQ2YTZmNDE4Zjk3YzJkNzg4NmMyNTM3OTM=" -d grant_type=authorization_code -d code=AQCcGtwdz6qaUl6n4VnJMxzN2lgVbXnMHt-4qKunJEf584vhbUmLRsp8R94jtIkW44DP3AYovZsy72RMP-T-t0ngFeb-_FLrO2-o_QIROeJe7TdX0hM6_3ACSXwQNyQMx-fJG-Z-O0tUfgjR_13snaILLe3sjy9kQvoDIgyxASqgv5EBGHt6UmmTzrhoCEPfaPrDhAfVuXTzrxWZWKxYA87GyS86Bgo -d redirect_uri=https%3A%2F%2Fgoogle.com https://accounts.spotify.com/api/token

#refreshtoken#
#curl -H "Authorization: Basic Yzc5ZjhmM2U0NDM3NGIwMmEzMjg4ODAxOTdkNzg1MDg6NDIyM2Y4YzQ2YTZmNDE4Zjk3YzJkNzg4NmMyNTM3OTM=" -d grant_type=refresh_token -d refresh_token=AQA0JVVgeOV766E4K1STAdhWUcibnPcBUhWc-YrU6DcWYJ-ai6-qagQjp2UqbqDxisq6yuo6ZPEpa-fA73oTbmTY_NVcf22nDsg7LKxD9OSIJ5ojl1o0sGsjYt81_kY1sPk -d client_id=c79f8f3e44374b02a328880197d78508 https://accounts.spotify.com/api/token
def refresh_token():
    import requests
    headers = {
        'Authorization': 'Basic Yzc5ZjhmM2U0NDM3NGIwMmEzMjg4ODAxOTdkNzg1MDg6NDIyM2Y4YzQ2YTZmNDE4Zjk3YzJkNzg4NmMyNTM3OTM=',
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': 'AQA0JVVgeOV766E4K1STAdhWUcibnPcBUhWc-YrU6DcWYJ-ai6-qagQjp2UqbqDxisq6yuo6ZPEpa-fA73oTbmTY_NVcf22nDsg7LKxD9OSIJ5ojl1o0sGsjYt81_kY1sPk',
        'client_id': 'c79f8f3e44374b02a328880197d78508',
    }
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    json_response = response.json()
    print(json_response)
    with open("accesstoken.txt", 'w') as accessfile:
        accessfile.write(json_response['access_token'])

        pass
    return response


def get_access_token_from_file():
    with open('accesstoken.txt', 'r') as file:
        for line in file:
            return str(line)


AccessDictPlaylist = {"access_token":"BQAMCJHRtvIw1whMd4D1wmUVVqJsEU_HArf2x_dlPx3Abjv_Wazg-CLpnYTdfKVqRw0esJszop_Nb0DlEJip2Pg8anc9GnXZVMjVfXPKzW8yVVfvHk7VOma2fQJMPmulbSObA5gYjMHxaCH-9xuG263HRkxaKHqoBiQUi6qUOd-n-zDb_QjALaVKdm9CdscmA_Z82G9yJWz6dTIz8wWxVBxeMYazvaeEfEc","token_type":"Bearer","expires_in":3600,"refresh_token":"AQA0JVVgeOV766E4K1STAdhWUcibnPcBUhWc-YrU6DcWYJ-ai6-qagQjp2UqbqDxisq6yuo6ZPEpa-fA73oTbmTY_NVcf22nDsg7LKxD9OSIJ5ojl1o0sGsjYt81_kY1sPk","scope":"playlist-modify-private playlist-modify-public"}
AccessDictPlaylist = {'access_token': 'BQDmJSq6sOK_tjf1gvhLtvpe3udAKaBX2-2tjdXKKfuJTtoYrDYwRw2DOO3tNf2ULmXfWuTKPJHoCjgiePVrhsWUhfsMGugyh-NeCkmVQtJ2EFnSCdJ1-YpAiEHqeI9Zf4YQdBT_b3OOdgvE_Sn0q4j0rEG5NjWcETXE124Z0Em-iJZyrbihBRSqAUoPBIhMwyPciLkoedl8lkDJ8lcK6kSW-9juT4zPhDQ', 'token_type': 'Bearer', 'expires_in': 3600, 'scope': 'playlist-modify-private playlist-modify-public'}


#spotify_token = AccessDictPlaylist["access_token"]
spotify_token = get_access_token_from_file()

spotify_user_id = '21v67tuqo3p3vkixbrx5xkudq'

python_playlist_id = '18STgHLE9PYjzXuhRuxB9H'
python_playlist_uri = 'spotify:playlist:18STgHLE9PYjzXuhRuxB9H'


if __name__ == "__main__":
    newaccess = refresh_token()