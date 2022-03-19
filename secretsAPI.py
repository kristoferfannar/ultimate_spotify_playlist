CLIENTID = 'c79f8f3e44374b02a328880197d78508'
CLIENTSECRET = '4223f8c46a6f418f97c2d7886c253793'
clienttohash = 'c79f8f3e44374b02a328880197d78508:4223f8c46a6f418f97c2d7886c253793'
client_64hash = 'Yzc5ZjhmM2U0NDM3NGIwMmEzMjg4ODAxOTdkNzg1MDg6NDIyM2Y4YzQ2YTZmNDE4Zjk3YzJkNzg4NmMyNTM3OTM='

redirect_urigoogle = 'https://google.com'
uri_decrypt = 'https%3A%2F%2Fgoogle.com'

spotify_auth_uri = 'https://accounts.spotify.com/authorize?client_id={}&response_type=code&redirect_uri={}&scope=playlist-modify-public%20playlist-modify-private'.format(CLIENTID, uri_decrypt) #skoða scope fyrir private playlista??


#print(spotify_auth_uri)

#access_code = AQCcGtwdz6qaUl6n4VnJMxzN2lgVbXnMHt-4qKunJEf584vhbUmLRsp8R94jtIkW44DP3AYovZsy72RMP-T-t0ngFeb-_FLrO2-o_QIROeJe7TdX0hM6_3ACSXwQNyQMx-fJG-Z-O0tUfgjR_13snaILLe3sjy9kQvoDIgyxASqgv5EBGHt6UmmTzrhoCEPfaPrDhAfVuXTzrxWZWKxYA87GyS86Bgo
#original
#curl -H "Authorization: Basic Yzc5ZjhmM2U0NDM3NGIwMmEzMjg4ODAxOTdkNzg1MDg6NDIyM2Y4YzQ2YTZmNDE4Zjk3YzJkNzg4NmMyNTM3OTM=" -d grant_type=authorization_code -d code=AQCcGtwdz6qaUl6n4VnJMxzN2lgVbXnMHt-4qKunJEf584vhbUmLRsp8R94jtIkW44DP3AYovZsy72RMP-T-t0ngFeb-_FLrO2-o_QIROeJe7TdX0hM6_3ACSXwQNyQMx-fJG-Z-O0tUfgjR_13snaILLe3sjy9kQvoDIgyxASqgv5EBGHt6UmmTzrhoCEPfaPrDhAfVuXTzrxWZWKxYA87GyS86Bgo -d redirect_uri=https%3A%2F%2Fgoogle.com https://accounts.spotify.com/api/token

#refreshtoken
#curl -H "Authorization: Basic Yzc5ZjhmM2U0NDM3NGIwMmEzMjg4ODAxOTdkNzg1MDg6NDIyM2Y4YzQ2YTZmNDE4Zjk3YzJkNzg4NmMyNTM3OTM=" -d grant_type=refresh_token -d refresh_token=AQA0JVVgeOV766E4K1STAdhWUcibnPcBUhWc-YrU6DcWYJ-ai6-qagQjp2UqbqDxisq6yuo6ZPEpa-fA73oTbmTY_NVcf22nDsg7LKxD9OSIJ5ojl1o0sGsjYt81_kY1sPk -d client_id=c79f8f3e44374b02a328880197d78508 https://accounts.spotify.com/api/token




#AccessDictPlaylist = {"access_token":"BQD7qeOPkYOh6h40hAwAdAqiJRaKvHNa-46pNQ1FQGmGTr6SkDFta7gTVuUWHqp-hMM7k-ikj53VKIVtvFnYygKNWlbbPyumIIPwdPVV6vNumP56KpAr3tsk497AtW67H2I1SENoiw5Ps6RjG7nmkqpFc6sjt9XSwdfFLdP9t_I6d6P8ZeLMPrsKrkUPI5jzq1lv5A","token_type":"Bearer","expires_in":3600,"refresh_token":"AQBeD64F1BDAf0F8YvSlry15nyR-up3HGDWBr-hMf0X377MoeFiEstdnMxgtyCsQHQpxu3STzFh2DtRkz8eEI_M0YSNK-I-6w2DCaeH4y0x1ZiwV-AWROxc0wZEI5rxwX1U","scope":"playlist-modify-public"}
AccessDictPlaylist = {"access_token":"BQAMCJHRtvIw1whMd4D1wmUVVqJsEU_HArf2x_dlPx3Abjv_Wazg-CLpnYTdfKVqRw0esJszop_Nb0DlEJip2Pg8anc9GnXZVMjVfXPKzW8yVVfvHk7VOma2fQJMPmulbSObA5gYjMHxaCH-9xuG263HRkxaKHqoBiQUi6qUOd-n-zDb_QjALaVKdm9CdscmA_Z82G9yJWz6dTIz8wWxVBxeMYazvaeEfEc","token_type":"Bearer","expires_in":3600,"refresh_token":"AQA0JVVgeOV766E4K1STAdhWUcibnPcBUhWc-YrU6DcWYJ-ai6-qagQjp2UqbqDxisq6yuo6ZPEpa-fA73oTbmTY_NVcf22nDsg7LKxD9OSIJ5ojl1o0sGsjYt81_kY1sPk","scope":"playlist-modify-private playlist-modify-public"}
AccessDictPlaylist = {"access_token":"BQDR2haVFjgxTcwwHvMfDqBKoX8VWGRQZjNZHqrWyBpaX2-nE1BfHiPfy2HiG2IVLdzw5XY3ghHMpDH0NAl17ne4SYQ0LsrKvT_IBX1vC08yce6J5VFawWMeCZ6Wo9TpIC2WdwwpZK-yr0I150olJthZKxtvtWG9i_GDeo7AwVDr1c0kJgSOzG27zPtjQo_40LZtIF_zHQSxPuOVkVBIhMWidb3XsfmzN18","token_type":"Bearer","expires_in":3600,"scope":"playlist-modify-private playlist-modify-public"}
AccessDictPlaylist = {"access_token":"BQDToH8ZuiEtUB5fH5Ipo6iyTJBbmx9DPQ2SUCmNYjL7p4bLh5IqnhxUm1dJJkhEVPHQaGvioZrVfjIyUfnEKyFi6VIUxu4BfZ06yfNOEeulCDMQsf1PCWhMxaD0RV7VVbbYjtj3iQT42SodJVPN-kGxeu3DPTLjUoAdWx_QPaE8GNYtxR0CmB0t28s6ApkBUJgrebaZLEXTiyydtSb2kVwCHj8-a4tZ-KI","token_type":"Bearer","expires_in":3600,"scope":"playlist-modify-private playlist-modify-public"}
AccessDictPlaylist = {"access_token":"BQC92v7nWS4Qlv1QMclwPyaMsriZdsRL5CQMpwFLJWkvcebJ5zc7PfnxG6ti6MC4MWEmewYlCGxyNk1ukyRaLZlD9ACDReCwqiDbP87yG5g6WW4gPANHyGsiOkxNjJ1q1v1lllUmOZHd1kOxIwHCkxf0fFdfwVMFS4_DAqZuIEaFpMHU9zBdaBNrqlc5J_QeD_jx3LCxRJKJBQh4QzoiYZtcAhF2GWUIB1s","token_type":"Bearer","expires_in":3600,"scope":"playlist-modify-private playlist-modify-public"}



spotify_token = AccessDictPlaylist["access_token"]
spotify_user_id = '21v67tuqo3p3vkixbrx5xkudq'

python_playlist_id = '18STgHLE9PYjzXuhRuxB9H'
python_playlist_uri = 'spotify:playlist:18STgHLE9PYjzXuhRuxB9H'