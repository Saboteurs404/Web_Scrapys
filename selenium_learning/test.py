import scrapy
import requests
from scrapy.http import response
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
    'Cookie': 'Hm_lvt_866c9be12d4a814454792b1fd0fed295=1687190650; _ga=GA1.1.1580248024.1679579875; cto_bidid=HUn8dl9TWFU3WlRMQSUyQm4xUlVvRHBYaWlqd2xCcENFQ1dqTml5NVpqZUdDUXdpeGtpMEJEc1JUTjhmJTJGRHVVbHclMkJ5dERSJTJGTWkBRur1gRUx8k9yY7WR4EJehN6SCybYP7dzVmdmVTbVB0JTJGZTBVUkUlM0Q; cto_dna_bundle=rrYAYl80M0RITmhlJTJCZkMwOUJGQlhaMUN2czROWm56UUd6YXIlMkY5YzdEVzhYU3Z0N3BTR2NLb3hlVFBDRWVsUXc2dmhLUA; .Cnblogs.AspNetCore.Cookies=CfDJ8DuWIYDefEVJtUW7VadsHY85_CBWUxCAh2xbf6xIcuyIIXb-dDlB1bsuVegyrT5J5SNsS8VerM3NwF_8vKIRTFrk0dkYpa-1CopZeypHcpbuerDSNGYT8ryNJE3izi3UuOigLAElSy9w2go7b08U2MIGZxcxQu0XdhOjgzqkP1H77fHNYf-0Xry-ThBXQggHDmTUKVa2dXx4sp8RZzdR51U3-cArN2CMZz6onXz4R0c7-nlNSB7Ryf8uDua00YJK1va1XrKOb_BdaBJK1y4NKZnPN71_4B65D_d8Br17e9BLelYt4uW8sKg7BnCVykyotZcaQ_5DTOoM2wAKICia0TWkBRur1gRUx8k9yY7WR4EJehN6SCybYP76gSznKTRukEXmpMAVpGatl-d0zqeOOurMrzk4Ab8iJMEZWXMX4Ia6B562LuErJwu1LTgsV9TT4-Ynf-g4s2eQU5DT_4bE2-dQdpkDtGhxLSBn6yharCwUL_17x5J6x9i_5wBLNwjuB9vfXLAC3nmyStjyOPasUMwwIxsfQuWkJBx37j2IFsFXf4Zkr3JBOJ0rR4bicuA3w; .CNBlogsCookie=0604424ECB85ED48319019C1A60E81DFA5C1076348E9648B58D597E96E7882AAFA1F9004680E77869E5DC0C54BC99F97D9501D52284B488997CC650B132FD3F848F1B1A7C645120335603D17512E22C3B019DEF0D9C9AA60944BE3BC8747F844148C5C3D; __utmc=66375729; __utmz=66375729.1693017632.5.5.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/; cto_bundle=PrJIZ193YjhKZHczMng0djJ6azc5WVF5N0RHYm1MTzBxRXZBcll5UXFKamI0TWkBRur1gRUx8k9yY7WR4EJehN6SCybYP7g3dmhlZVRRUFpJMnk2ekhwUkwwcWpqT0pkQ2l0MmRKdHRXYTBMQ3lFNDYlMkJHVFg2b1BVcyUyQnpHNFVBMkVyZXBkSHdZQ01ienRlSUEyRGliVXlCdEElM0QlM0Q; _ga_M95P3TTWJZ=GS1.1.1693028408.30.1.1693028408.0.0.0; affinity=1693032329.247.579.442510|f1d132e1bdef0cb037c250e0486c61b3; _ga_3Q0DVSGN10=GS1.1.1693033181.3.1.1693033185.56.0.0; __utma=66375729.1580248024.1679579875.1693032328.1693035187.7; __utmt=1; __utmb=66375729.1.10.1693035187; __gads=ID=37eddb2f4bf7b702:T=1679579673:RT=1693035188:S=ALNI_MbI60_tZzXWdlKRqsV31kbEtR5UgA; __gpi=UID=00000bdf5e962d25:T=1679579673:RT=1693035188:S=ALNI_MYr4TqkvDlRoQY1N6MkyntU_IJrXw',
    'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'Referer': 'https://news.cnblogs.com/n/748239/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

url = 'https://news.cnblogs.com/n/748239/'
res = requests.get(url, headers=headers)
res.encoding = "utf-8"
print(res)
print(res.text)
ele = etree.HTML(res.text)
print(ele)
result_1 = ele.xpath('//div[@id="news_info"]/span[@class="time"]//text()')
result_2 = ele.xpath('//div[@id="news_title"]/a//text()')
print(result_1)
print(result_2)
