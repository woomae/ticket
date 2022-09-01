import re
from time import sleep
import easyocr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select



# Options= webdriver.ChromeOptions()
# user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
# Options.add_argument('user-agent='+user_agent)

driver = webdriver.Chrome('./chromedriver.exe')
# 사이즈조절
driver.set_window_size(1400, 1000)  # (가로, 세로)
driver.get('https://ticket.interpark.com/Gate/TPLogin.asp') # 페이지 이동

driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='leftLoginBox']/iframe[@title='login']"))
userId = driver.find_element(By.ID, 'userId')
userId.send_keys('chg01111') # 로그인 할 계정 id
userPwd = driver.find_element(By.ID, 'userPwd')
userPwd.send_keys('gudrms0!') # 로그인 할 계정의 패스워드
userPwd.send_keys(Keys.ENTER)

# 원하는 티켓의 상세페이지의 링크를 가져옴(URL의 마지막숫자는 상세페이지에 있는 도메인)
driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode='+'22007717')
sleep(1)
# 태그가 없으면 에러발생
def check_exists_by_element(by, name):
    try:
        driver.find_element(by, name)
    except NoSuchElementException:
        return False
    return True
# 혹시 예매안내가 있는지 체크 후 있으면 닫기 버튼 클릭
close_check = check_exists_by_element(By.CSS_SELECTOR, "#popup-prdGuide > div > div.popupFooter > button")
print(close_check)
if close_check:
	driver.find_element(By.CLASS_NAME, "is-bottomBtn").click()
# 예매버튼클릭
while True:
    try:
       driver.find_element(By.CSS_SELECTOR, "#productSide > div > div.sideBtnWrap > a.sideBtn.is-primary").click()
    except:
        continue
    else:
        break
sleep(1)
# 예매하기 눌러서 새창이 뜨면 포커스를 새롭게 열린탭으로 변경
driver.switch_to.window(driver.window_handles[-1])
print("1.예매페이지에서 예매탭까지 이동완료")
while True:
    try:
        seatiframe = driver.find_element(By.CSS_SELECTOR, "#ifrmSeat")
    except:
        continue
    else:
        break
# iframe 이동
driver.switch_to.frame(seatiframe)
print("2.seat_iframe이동완료")
checktime=0
while checktime<5:
    try:
        # 입력해야될 문자 이미지 캡쳐하기.
        checktime+=1
        captcha = driver.find_element(By.XPATH, "//*[@id='imgCaptcha']")
    except:
        continue
    else:
        break
if checktime!=5:
  # easyocr 이미지내 인식할 언어 지정
  reader = easyocr.Reader(['en'])
  # 캡쳐한 이미지에서 문자열 인식하기
  result = reader.readtext(captcha.screenshot_as_png, detail=0)
  #문자열 인식오류 제거
  result = result[0].replace('t', 'T').replace('s', 'S').replace('c', 'C').replace(' ', '').replace('z', 'Z').replace('8', 'B').replace('5', 'S').replace('0', 'O').replace('$', 'S').replace(',', '').replace(':', '').replace('.', '').replace('+', 'T').replace("'", '').replace('`', '').replace('1', 'L').replace('e', 'Q').replace('3', 'S').replace('€', 'C').replace('{', '').replace('-', '').replace('@','O').replace('p', 'D')
  # 입력할 텍스트박스 클릭하기.
  driver.find_element(By.CLASS_NAME,'validationTxt').click()
  # 추출된 문자열 텍스트박스에 입력하기.
  chapchaText = driver.find_element(By.ID,'txtCaptcha')
  print(result)
  chapchaText.send_keys(result)
  #captcha인증 완료
  chapchaText.send_keys(Keys.ENTER)
  print("3.captcha인증완료")

#관람일자선택
select1 = Select(driver.find_element(By.CSS_SELECTOR,"#PlayDate"))
select1.select_by_value("20221001")#날짜입력
sleep(1)
select2 = Select(driver.find_element(By.ID,"PlaySeq"))
select2.select_by_value("001")#시간입력(확인필요!!, 날짜에 따라 value값이 달라짐)

#좌석선택
def seat_title_checking1(level, block, seat):
    return "[title*='" + level + "석'][title*='" + block + "구역 " + str(seat) + "열']"

def seat_title_checking2(level, block, seat):
    return "[title*='" + level + "석'][title*='" + block + "구역" + str(seat) + "열']"

def seat_title_checking3(level,  block, seat):
    return "[title*='" + level + "석'][title*='" + block + "블럭" + str(seat) + "열']"

def seat_title_checking4(level, block, seat):
    return "[title*='" + level + "석'][title*='-" + str(seat) + "열']"

def seat_title_checking5(level, block, seat):
    return "[title*='" + level + "석'][title*='-" + chr(64 + seat) + "열']"

# 좌석 선택 iframe
while True:
    try:
        driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='ifrmSeatDetail']"))
    except:
        continue
    else:
        break
sleep(3)#미니맵이있는경우 3초안에 클릭
# 활성화 되어 있는 좌석의 class 속성 stySeat 
try:
    seat_check = driver.find_element(By.CLASS_NAME, "stySeat")
except:
    c_name ="e"
    seat_check = driver.find_element(By.CLASS_NAME, "SeatN")
else:
    print("좌석을 찾을 수 없습니다.")

seat_title = seat_check.get_attribute('title')
b = seat_title.split('-')

# 좌석 선택하는 태그의 title 속성의 포멧  
# [VIP석] 1층-A구역18열-11
# [VIP석] 1층-B구역 11열-1
# [VIP석] 1층-D열-99
# [VIP석] 1층-11열-11
# [VIP석] 1층-A블럭8열-10

if '구역' in b[1]:
    if b[1][b[1].find('역') + 1] == ' ':
        zone_seat_return = seat_title_checking1
    else:
        zone_seat_return = seat_title_checking2
elif '블럭' in b[1]:
    zone_seat_return = seat_title_checking3
else:
    c = re.compile('[0-9]')
    if c.match(b[1]):
        zone_seat_return = seat_title_checking4
    else:
        zone_seat_return = seat_title_checking5

# 좌석 선택
w_check = False
seat = 0
cnt = 0
while seat < 20:
    seat = seat + 1
    # zon_seat_return의 매개변수 설명
    # level : VIP, R, A  등 좌석의 등급
    # block : A, B, C 등 좌석의 구역을 설정
    # seat : 숫자 또는 영어. 열을 지정
    seat_string = zone_seat_return('S', 'A5', 14)#level,block,seat
    if c_name=="e":
        imgs = driver.find_elements(By.CSS_SELECTOR, "span.SeatN" + seat_string)
    else:
        imgs = driver.find_elements(By.CSS_SELECTOR, "img.stySeat" + seat_string)

    for i in imgs:
        i.click()
        cnt = cnt + 1
        if cnt == int(4):# 인원
            w_check = True
            break

    if w_check:
        break
        
# 원래 팝업 프레임으로 돌아가기
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='divBookSeat']/iframe[@id='ifrmSeat']"))
# 다음 버튼 클릭
driver.find_element(By.XPATH, "//div[@class='seatR']/div[@class='inner']/div[@class='btnWrap']/a/img").click()





# driver.quit()