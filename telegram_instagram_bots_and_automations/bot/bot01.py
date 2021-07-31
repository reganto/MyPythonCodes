import requests

TOKEN = ""
baseurl = "https://api.telegram.org/bot" + TOKEN


# response = requests.get(
#     baseurl+"/sendMessage?chat_id={0}&text={1}&disable_notification={2}&reply_to_message_id={3}"
#     .format(447010443, "Good day", True, 24))

caption = "dlmsdklmksfkmsdkfmsl kdfm ksmklfmklmflcvdvsdvsdlmlsdmkzsmkvmkdmkzmsdkvmlzsdkvmlzskdmvkzsldvkmzlsdmvkzsmdvlkmzslkvmlzskmvkmzsldvkmzklsmdvkdssdsdfsdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssdlflsdfklsd;flskdlfks;kfs;lkflsddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddda"
response = requests.get(
    baseurl+"/sendPhoto?chat_id={0}&photo={1}&caption={2}"
    .format(447010443, "https://data.hu/get/11739983/01.png", caption)    
)
response = response.json()

print(response)
