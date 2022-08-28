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
driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode='+'22009945')
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
print("1.예매페이지에서 연 팡까지 이동완료")
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
while True:
    try:
        # 입력해야될 문자 이미지 캡쳐하기.
        captcha = driver.find_element(By.XPATH, "//*[@id='imgCaptcha']")
    except:
        continue
    else:
        break
# easyocr 이미지내 인식할 언어 지정
reader = easyocr.Reader(['en'])
# 캡쳐한 이미지에서 문자열 인식하기
result = reader.readtext(captcha.screenshot_as_png, detail=0)
#문자열 인식오류 제거
result = result[0].replace(' ', '').replace('5', 'S').replace('0', 'O').replace('$', 'S').replace(',', '').replace(':', '').replace('.', '').replace('+', 'T').replace("'", '').replace('`', '').replace('1', 'L').replace('e', 'Q').replace('3', 'S').replace('€', 'C').replace('{', '').replace('-', '').replace('@','O')
# 입력할 텍스트박스 클릭하기.
driver.find_element(By.CLASS_NAME,'validationTxt').click()
# 추출된 문자열 텍스트박스에 입력하기.
chapchaText = driver.find_element(By.ID,'txtCaptcha')
print(result)
chapchaText.send_keys(result)
#captcha인증 완료
chapchaText.send_keys(Keys.ENTER)
print("3.captcha인증완료")

# 날짜 아이프레임
dateiframe = driver.find_element(By.CSS_SELECTOR, "#ifrmBookStep")
driver.switch_to.frame(dateiframe)

select = Select(driver.find_element_by_xpath('셀렉트박스XPATH'))
select.select_by_value('선택할 값')
print(year, month)


# driver.quit()