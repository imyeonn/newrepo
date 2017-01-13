### 0905 전체 쇼핑몰 리스트 순위 및 조회수 출력 &매주 변화추이 파악 ###

# 웹사이트에 접근할 수 있는 도구상자 urllib request, bs 가져오기
import urllib.request
from bs4 import BeautifulSoup

# sort=F 뒤 &page=1, 2, 3... for문으로 1-28페이지 접근
TARGET = "http://www.style-chart.com/rank/?&sort=F&page=1"

# 각 페이지별로 정보 읽어서 뷰티풀수프 실행
url = urllib.request.urlopen(TARGET)
data = url.read()
soup = BeautifulSoup(data, "html.parser")

query = soup.find_all('li', attrs={'class': 'info2'})
print(query)
    #
    # # 그렇게 찾은 데이터를 for로 화면출력
    # for child in query:
    #     try:
    #         print(
    #             "%s\t%s" %
    #             (child.contents[1].strong.string, child.contents[-4].contents[-1].string)
    #         )
    #
    #
    #     except AttributeError:
    #         pass
    #
    #         # child.contents[1].strong은 위 child 리스트의 2번째 줄이 쇼핑몰이름이고 양쪽에 strong 태그로 둘러싸임
    #         # 여기서 <strong>쇼핑몰이름</strong> 태그 제외할거면 .string
