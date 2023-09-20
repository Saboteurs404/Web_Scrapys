from bs4 import BeautifulSoup
import requests

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
    'Cookie': 'ip_ck=4caD4P7zj7QuNjEyNzQ0LjE2ODQ3NTUwODk%3D; __bid_n=188433a958ea01e2ff4207; FPTOKEN=ng8AkVtw1rYU/N+vKhrnaQa83AcJ+psA00wwWbUIaoKUFNUC2N8UiFAd/iI226rwGYpfzq19O8f33ccRHYeItclFpFJJoTwuNH4JnGeghKMQKUjKyrXL8sptJDWhbZnsAKel3KwHB2+Rb+JR1KSioKhGsj+Hb0cWaMHn93CZRZ9p+QWR0qxPelTsk5bkVFma0TRsSsx6rx91zzhtaPYsieqHcW8N7ALzrJ3K5kpB6R7y8zANnE4NWWzNaOFNbaD3E7xX5HZhW6GEtExxP6pSAFnmjXAnbznLdr/+HkKviZdns7phXWZdS9Xgd/Tt6sF8YVeBss/qWzPwDx6fVtIdWXfiydN1ibeSEldKCy7KubLUPe+QXsnkeppa0LsvL8M+Z0ipXd+Niwdrff6/ObRw==|MNEWGfcM7sWLntzrxkiZWpVWN2L4Ml/RAhg58G7ZMx8=|10|b9bc916db85033841c72f1eeb93941f2; zol_userid=swxehs; last_userid=swxehs; zol_check=1738187301; zol_sid=58106813; SSID=%242a%2410%24ee2a0834777bdda8b95caa6ff92741285b0d9c718df27d8d57cf51a51cc40d59; zol_cipher=5812bd816e7db4a869d9ebe3ec35b0d0; zol_ssid_token=f3mKcI8-NbtS1jLdhdevhx5qfh6BfCHsFobk9g61s8MtLku-YOmUAPcj1G7MssUFfopTqbdan_Et3qkxkAnc4nHmoXS09vA0rsJXsdEL4osLc8kpLJrEh5TlAk9TbVJjhu5ToKKD2pFY5Wm1UlzFWLzfDb9DWpCG; Adshow=4; listSubcateId=792; z_pro_city=s_provice%3Dshanxi%26s_city%3Ddatong; userProvinceId=11; userCityId=34; userCountyId=318; userLocationId=17191; lv=1694567562; vn=7; Hm_lvt_ae5edc2bc4fc71370807f6187f0a2dd0=1693564258,1693748480,1694567562; _ga=GA1.3.1745220676.1694567564; _gid=GA1.3.666779974.1694567564; zol_bind_swxehs=1; z_day=icnmo11564%3D1%26ixgo20%3D1; questionnaire_pv=1694563204; Hm_lpvt_ae5edc2bc4fc71370807f6187f0a2dd0=1694568357; _ga_6XFCZ4WP8R=GS1.3.1694567567.1.1.1694568357.0.0.0; 9f52bc65588694d252974a5bb638b7cc=10r177n1v1v2fs38g166a.aaq%7B%7BZ%7D%7D3%7B%7BZ%7D%7Dnull; MyZClick_9f52bc65588694d252974a5bb638b7cc=/html/body/div%5B5%5D/div/div%5B2%5D/div/a%5B3%5D/',
}
for i in range(1, 10):
    html = requests.get('https://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i), headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    jokes = soup.select(".article-summary")
    for joke in jokes:
        connect = joke.select(".summary-text")
        # connect = connect.text
        print(connect)


