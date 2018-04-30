import requests
from selenium import webdriver


# 짧은 작업인 만큼 부족한 점이 많으니 이 점 양해 바랍니다.

# 쿠키값을 가져오기 위한 크롬 웹드라이버입니다. 경로를 설정해 주세요.
driver = webdriver.Chrome('C:\Users\주형\Desktop\crawler\chromedriver.exe')


# requests.get으로 쿠키를 인자로 넘겨주려면 형식이 dict여야 하는데, 웹 드라이버에서 쿠키를 가져오면 자료형이 list입니다. 그걸 바꿔주는 메소드입니다.
def makecookie(cookies):

    result = {}

    for x in cookies:
        for y in x.keys():
            result[y] = str(x[y])

    return result


# url을 받아 결과를 file에 저장하고 total은 계속 누적시키는 메소드입니다.
def getkey(url, total, file):

    # txt 파일에서 한 줄을 읽어오면 맨 뒤에 \n가 붙습니다. 그걸 떼주어야 오류가 나지 않습니다.
    url = url.replace("\n", "")

    # http 프로토콜과 https 프로토콜을 준비합니다.
    httpurl = 'http://' + url + '/'
    httpsurl = 'https://' + url + '/'

    # request 헤더입니다. 헤더가 없으면 데이터를 반환하지 않는 사이트가 대부분입니다.
    headers = {'Accept-Encoding': 'gzip, deflate',
               "Pragma": "no-cache",
               "Cache-Control": "no-cache",
               "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
               'Content-Type': 'application/json;charset=UTF-8',
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
               'Host': url,
               "Referer" : 'https://www.google.com/',
               'Connection': 'Keep-Alive'}

    #http
    try:
        # 웹드라이버가 http 프로토콜로 설정된 url로 접속합니다. 이때 크롬창이 뜨는데, 닫으시면 안 됩니다.
        driver.get(httpurl)

        # 웹드라이버가 접속한 페이지의 쿠키를 가져옵니다.
        cookie = driver.get_cookies()

        # 헤더와 쿠키, url로 request를 보내고 결과를 response에 저장합니다.
        response = requests.get(httpurl, headers=headers, cookies=makecookie(cookie))

        # key="aaaaa" 형태의 키값을 뽑기 위해 앞뒤의 ""를 기준으로 모두 떼줍니다.
        result = (response.text.split('key="')[1].split('"')[0])
        # 각 결과를 구분하는 문자입니다.
        file.write(result+"||")
        total += 1

    # header가 올바르지 않은 경우
    except ValueError as e:
        print(e)

    # key가 명시된 패턴에 맞게 존재하지 않는 경우
    except IndexError as e:
        print(e)

    # 접속 불가한 url의 경우
    except requests.exceptions.ConnectionError as e:
        print(e)

    # 똑같이 https 프로토콜로 작업을 합니다.
    try:
        driver.get(httpsurl)

        cookie = driver.get_cookies()

        response = requests.get(httpsurl, headers=headers, cookies=makecookie(cookie))
        result = (response.text.split('key="')[1].split('"')[0])
        file.write(result+"||")
        total += 1

    # header가 올바르지 않은 경우
    except ValueError as e:
        print(e)

    # key가 명시된 패턴에 맞게 존재하지 않는 경우
    except IndexError as e:
        print(e)

    # 접속 불가한 url의 경우
    except requests.exceptions.ConnectionError as e:
        print(e)

    return total


def readfile():
    # live 파일을 경로에 맞게 설정해주세요.
    urlfile = open("C:\Users\주형\Desktop\crawler\live.txt", 'r')

    # 결과 파일은 실행된 스크립트의 경로에 저장됩니다.
    resultfile = open("result.txt", 'w')
    total = 0

    # 한 줄 씩 getkey 메소드에 넘겨주고, total을 계속 누적합니다.
    while True:
        line = urlfile.readline()
        if not line: break
        total = getkey(line, total, resultfile)

    # 반복이 끝나면 total을 뒤에 써줍니다.
    resultfile.write("total : "+ str(total))
    resultfile.close()
    urlfile.close()

if __name__ == '__main__':
    readfile()
