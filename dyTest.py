from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = 'vivo X9Plus'
#desired_caps['udid'] = '621QECQF4CQV8'
#desired_caps['deviceName'] = 'MEIZU'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = '.splash.SplashActivity'
desired_caps['newCommandTimeout'] = '6000'
#desired_caps['app'] = '/Users/yaoyao/Downloads/dy4.3.apk'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#driver.implicitly_wait(20)
#driver.find_element_by_id("com.ss.android.ugc.aweme:id/c_3").click()
driver.find_element_by_xpath('//android.widget.TextView[@text="同意"]').click()
driver.implicitly_wait(20)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/aev").click()

driver.swipe(533,1538,533,369)

driver.implicitly_wait(10)
driver.tap([(986,149)])
#driver.find_element_by_id("com.ss.android.ugc.aweme:id/alw").click()
driver.implicitly_wait(10)
#进入搜索页定位
driver.find_element_by_id("com.ss.android.ugc.aweme:id/p6").find_elements_by_class_name("android.widget.EditText")[0].click()
#driver.find_element_by_xpath('//android.view.View[@content-desc="热点榜"]').click()
driver.implicitly_wait(10)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/b7l").click()

driver.implicitly_wait(10)

# for i in range(len(elem)):
for i in range(8):
    ele = driver.find_element_by_id("com.ss.android.ugc.aweme:id/akl").find_elements_by_class_name("android.widget.RelativeLayout")[i]
    ele.click()
    driver.implicitly_wait(5)
    driver.find_element_by_id("com.ss.android.ugc.aweme:id/afx").find_element_by_xpath('//android.widget.TextView[@text="视频"]').click()
    time.sleep(5)
    driver.find_element_by_id("com.ss.android.ugc.aweme:id/acz").click()

driver.implicitly_wait(10)
driver.quit()


