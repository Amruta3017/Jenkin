
import time

from selenium.webdriver.common.by import By

from PageObjects.QA_LOGIN_PAGE import Login
from Utilities import XLUtils
from Utilities.readProperties import ReadConfig
from Utilities.commonMethods import get_path
from Utilities.customLogger import LogGen

class Test_Login:
    baseURL = ReadConfig.get_app_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    logger = LogGen()
    log = logger.configure_logger()

    #xl_path = get_path("TestData", "Test_cases_Pre_Login_QA.xlsx")
    xl_path = get_path("TestData", "Testcases_PreLogin.xlsx")
    def advance(self, setup):
        advanced_button = self.driver.find_elements(By.XPATH, '//*[@id="details-button"]')
        if advanced_button:
            advanced_button[0].click()
            time.sleep(5)  # Give some time for the page to load after clicking "Advanced"
            proceed_link = self.driver.find_element(By.XPATH, '//*[@id="proceed-link"]')
            proceed_link.click()
            time.sleep(1)  # Give some time for the page to load after clicking "Proceed"
    def test_log_001(self, setup):
        self.log.info("========== Verifying URL of login page ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Login", "test_log_001")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 5, 4, "pass")
            self.driver.close()
            self.log.info("==========Verifying URL of login page PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 5, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "verify URL.png"))
            self.driver.close()
            self.log.info("=========Verifying URL of login page FAILED ==========")
            assert False

    def test_log_002(self, setup):
        self.log.info("========== Click Log In Button  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        chk = self.lo.chk_login_dropdown_menu()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 6, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Log In Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 6, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Log In Button.png"))
            self.driver.close()
            self.log.info("========= Click Log In Button FAILED ==========")
            assert False

    def test_log_003(self, setup):
        self.log.info("========== Check Color of personal  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        befor_hover = self.lo.get_css_personal()
        self.lo.hover_personal()
        after_hover = self.lo.get_css_personal()
        if befor_hover != after_hover:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 7, 4, "pass")
            self.driver.close()
            self.log.info("========== Check Color of personal PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 7, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Check Color of personal.png"))
            self.driver.close()
            self.log.info("========= Check Color of personal FAILED ==========")
            assert False

    def test_log_004(self, setup):
        self.log.info("========== Click Log In Button of presonal ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Login", "test_log_004")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 8, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Log In Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 8, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Log In Button.png"))
            self.driver.close()
            self.log.info("=========Click Log In Button FAILED ==========")
            assert False

    def test_log_005(self, setup):
        self.log.info("========== Click Back Button  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_back()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Login", "test_log_005")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 9, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Back Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 9, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Back Button.png"))
            self.driver.close()
            self.log.info("=========Click Back Button FAILED ==========")
            assert False

    def test_log_006(self, setup):
        self.log.info("========== Click Register Button ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_register()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Login", "test_log_006")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 10, 4, "pass")
            self.driver.close()
            self.log.info("========= Click Register Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 10, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click Register Button.png"))
            self.driver.close()
            self.log.info("========= Click Register Button FAILED ==========")
            assert False

    def test_log_007(self, setup):
        self.log.info("========== Click login Button without fill any field  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_per_login_btn()
        chk = self.lo.chk_error_msg()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 11, 4, "pass")
            self.driver.close()
            self.log.info("=========Click login Button without fill any field PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 11, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click login Button without fill any field.png"))
            self.driver.close()
            self.log.info("=========Click login Button without fill any field FAILED ==========")
            assert False

    def test_log_008(self, setup):
        self.log.info("========== Click login Button with valid email only ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.send_email()
        self.lo.clk_per_login_btn()
        chk = self.lo.chk_error_msg()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 12, 4, "pass")
            self.driver.close()
            self.log.info("=========Click login Button with valid email only PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 12, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click login Button with valid email only.png"))
            self.driver.close()
            self.log.info("=========Click login Button with valid email only FAILED ==========")
            assert False

    def test_log_009(self, setup):
        self.log.info("========== Click login Button with valid password only  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.send_password()
        self.lo.clk_per_login_btn()
        chk = self.lo.chk_error_msg()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 13, 4, "pass")
            self.driver.close()
            self.log.info("=========Click login Button with valid password only PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 13, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click login Button with valid password only.png"))
            self.driver.close()
            self.log.info("=========Click login Button with valid password only FAILED ==========")
            assert False

    def test_log_010(self, setup):
        self.log.info("========== Click login with invalid email and valid password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.send_email1()
        self.lo.send_password()
        self.lo.clk_per_login_btn()
        chk = self.lo.chk_error_msg()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 14, 4, "pass")
            self.driver.close()
            self.log.info("=========Click login with invalid email and valid password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 14, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click login with invalid email and valid password.png"))
            self.driver.close()
            self.log.info("=========Click login with invalid email and valid password FAILED ==========")

    def test_log_011(self, setup):
        self.log.info("========== Click login with valid email and invalid password  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.send_email()
        self.lo.send_password1()
        self.lo.clk_per_login_btn()
        time.sleep(5)
        chk = self.lo.chk_error_msg()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 15, 4, "pass")
            self.driver.close()
            self.log.info("=========Click login with valid email and invalid password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 15, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click login with valid email and invalid password.png"))
            self.driver.close()
            self.log.info("=========Click login with valid email and invalid password FAILED ==========")

    def test_log_012(self, setup):
        self.log.info("========== Click login with invalid email and invalid password  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.send_email1()
        self.lo.send_password1()
        self.lo.clk_per_login_btn()
        time.sleep(5)
        chk = self.lo.chk_error_msg()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 16, 4, "pass")
            self.driver.close()
            self.log.info("=========Click login with invalid email and invalid password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 16, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click login with invalid email and invalid password.png"))
            self.driver.close()
            self.log.info("=========Click login with invalid email and invalid password FAILED ==========")

    def test_log_013(self, setup):
        self.log.info("========== Click login with valid email and valid password  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.send_email()
        self.lo.send_password()
        self.lo.clk_per_login_btn()
        time.sleep(7)
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Login", "test_log_013")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 17, 4, "pass")
            self.driver.close()
            self.log.info("=========Click login with valid email and valid password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 17, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click login with valid email and valid password.png"))
            self.driver.close()
            self.log.info("=========Click login with valid email and valid password FAILED ==========")
            assert False

    def test_log_014(self, setup):
        self.log.info("========== Click eye icon  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.send_email()
        self.lo.send_password()
        self.lo.clk_eye_icon()
        if self.lo.get_password() == "text":
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 18, 4, "pass")
            self.driver.close()
            self.log.info("=========Click eye icon PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 18, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click eye icon.png"))
            self.driver.close()
            self.log.info("=========Click eye icon FAILED ==========")
            assert False

    def test_log_015(self, setup):
        self.log.info("========== Click forget password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Login", "test_log_015")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 19, 4, "pass")
            self.driver.close()
            self.log.info("========= Click forget password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 19, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click forget password.png"))
            self.driver.close()
            self.log.info("========= Click forget password FAILED ==========")
            assert False

    def test_log_016(self, setup):
        self.log.info("========== Click Back Button of forget password  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.clk_back()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Login", "test_log_016")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 20, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Back Button of forget password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 20, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Back Button of forget password.png"))
            self.driver.close()
            self.log.info("=========Click Back Button of forget password FAILED ==========")
            assert False

    def test_log_017(self, setup):
        self.log.info("========== Click Register Button of forget password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.clk_register()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Login", "test_log_017")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 21, 4, "pass")
            self.driver.close()
            self.log.info("========= Click Register Button of forget password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 21, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click Register Button of forget password.png"))
            self.driver.close()
            self.log.info("========= Click Register Button of forget password FAILED ==========")
            assert False

    def test_log_018(self, setup):
        self.log.info("========== Click Next Button without fill of forget password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.clk_forget_password_next()
        chk = self.lo.chk_forget_pwd_next_error_msg()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 22, 4, "pass")
            self.driver.close()
            self.log.info("========= Click Next Button without fill of forget password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 22, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Next Button without fill of forget password.png"))
            self.driver.close()
            self.log.info("========= Click Next Button without fill of forget password FAILED ==========")
            assert False

    def test_log_019(self, setup):
        self.log.info("========== send invalid email to forget password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.send_forget_pwd_email1()
        self.lo.clk_forget_password_next()
        chk = self.lo.chk_forget_pwd_next_error_msg()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 23, 4, "pass")
            self.driver.close()
            self.log.info("========= send invalid email to forget password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 23, 4, "fail")
            self.driver.save_screenshot(
                get_path("Screenshots", "send invalid email to forget password.png"))
            self.driver.close()
            self.log.info("=========send invalid email to forget password FAILED ==========")
            assert False

    def test_log_020(self, setup):
        self.log.info("========== send valid email to forget password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.send_forget_pwd_email()
        self.lo.clk_forget_password_next()
        chk = self.lo.chk_forget_pwd_code()
        time.sleep(10)
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 24, 4, "pass")
            self.driver.close()
            self.log.info("========= send valid email to forget password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 24, 4, "fail")
            self.driver.save_screenshot(
                get_path("Screenshots", "send valid email to forget password.png"))
            self.driver.close()
            self.log.info("=========send valid email to forget password FAILED ==========")
            assert False

    def test_log_021(self, setup):
        self.log.info("========== Check email is same as enterd in forget password field ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.send_forget_pwd_email()
        time.sleep(2)
        chk1=self.lo.get_forget_pwd_email()
        self.lo.clk_forget_password_next()
        chk2 = self.lo.check_email_forget_pwd()
        if chk1 == chk2:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 25, 4, "pass")
            self.driver.close()
            self.log.info("========= Check email is same as enterd in forget password field PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 25, 4, "fail")
            self.driver.save_screenshot(
                get_path("Screenshots", "send valid email to forget password.png"))
            self.driver.close()
            self.log.info("=========Check email is same as enterd in forget password field FAILED ==========")
            assert False

    def test_log_022(self, setup):
        self.log.info("========== send_code ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.send_forget_pwd_email()
        self.lo.clk_forget_password_next()
        self.lo.send_forget_code()
        assert True
        result = XLUtils.writeData(self.xl_path, "Login", 26, 4, "pass")
        self.driver.close()
        self.log.info("========= send_code PASS ==========")

    def test_log_023(self, setup):
        self.log.info("========== send_code less than 4 digit ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.send_forget_pwd_email()
        self.lo.clk_forget_password_next()
        self.lo.send_forget_code1()
        self.lo.clk_next()
        time.sleep(2)
        chk = self.lo.chk_forget_pwd_error_msg()
        print(chk)
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 27, 4, "pass")
            self.driver.close()
            self.log.info("========= send_code less than 4 digit PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 27, 4, "fail")
            self.driver.save_screenshot(
                get_path("Screenshots", "send_code less than 4 digit.png"))
            self.driver.close()
            self.log.info("=========send_code less than 4 digit FAILED ==========")
            assert False
    def test_log_024(self, setup):
        self.log.info("========== resend button enable ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.send_forget_pwd_email()
        self.lo.clk_forget_password_next()
        time.sleep(65)
        chk = self.lo.chk_reverse_counter()
        if chk == '0':
            self.lo.clk_resend()
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 28, 4, "pass")
            self.driver.close()
            self.log.info("========= resend button enable PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 28, 4, "fail")
            self.driver.save_screenshot(
                get_path("Screenshots", "resend button enable.png"))
            self.driver.close()
            self.log.info("=========resend button enable FAILED ==========")
            assert False
    def test_log_025(self, setup):
        self.log.info("========== reset password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.advance(setup)
        self.lo = Login(self.driver)
        self.lo.clk_log_in()
        self.lo.clk_personal_login()
        self.lo.clk_forget_password()
        self.lo.send_forget_pwd_email()
        self.lo.clk_forget_password_next()
        #self.lo.send_forget_code()
        time.sleep(30)
        self.lo.clk_next()
        time.sleep(2)
        self.lo.clk_change_reset_pwd()
        chk = self.lo.chk_reset_error_msg()
        if chk == "Please fill in all fields.":
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 29, 4, "pass")
            self.log.info("========= click reset password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 29, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "click reset password.png"))
            self.log.info("=========click reset password FAILED ==========")
            assert False
        time.sleep(2)
        before_enter = self.lo.get_css_small_ch_box()
        txt = XLUtils.readExpData(self.xl_path, "Login", "test_log_030")
        self.lo.send_password11(txt)
        after_enter = self.lo.get_css_small_ch_box()
        if before_enter == after_enter:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 34, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter Small letter and check Checkbox PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 34, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter Small letter and check Checkbox.png"))
            self.driver.close()
            self.log.info("=========Enter Small letter and check Checkbox FAILED ==========")
            assert False
        time.sleep(2)
        before_enter = self.lo.get_css_small_ch_box()
        txt = XLUtils.readExpData(self.xl_path, "Login", "test_log_031")
        self.lo.send_password11(txt)
        after_enter = self.lo.get_css_small_ch_box()
        if before_enter == after_enter:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 35, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter Capital letter and check Checkbox PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 35, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter Capital letter and check Checkbox.png"))
            self.driver.close()
            self.log.info("=========Enter Capital letter and check Checkbox FAILED ==========")
            assert False
        time.sleep(2)
        before_enter = self.lo.get_css_small_ch_box()
        txt = XLUtils.readExpData(self.xl_path, "Login", "test_log_032")
        self.lo.send_password11(txt)
        after_enter = self.lo.get_css_small_ch_box()
        if before_enter == after_enter:
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 36, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter Digit and check Checkbox PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 36, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter Digit letter and check Checkbox.png"))
            self.driver.close()
            self.log.info("=========Enter Digit letter and check Checkbox FAILED ==========")
            assert False
        txt = XLUtils.readExpData(self.xl_path, "Login", "test_log_033")
        self.lo.send_password11(txt)
        self.lo.clk_change_reset_pwd11()
        chk = self.lo.chk_reset_error_msg()
        if chk == "Password must be at least 6 characters long.":
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 37, 4, "pass")
            self.driver.close()
            self.log.info("=========password less than 6 PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 37, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "password less than 6.png"))
            self.driver.close()
            self.log.info("=========password less than 6 FAILED ==========")
            assert False
        time.sleep(2)
        self.lo.clr_send_reset_pwd()
        self.lo.clr_send_reset_con_pwd()
        self.lo.send_reset_pwd()
        self.lo.clk_change_reset_pwd()
        chk = self.lo.chk_reset_error_msg()
        if chk == "Please fill in all fields.":
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 30, 4, "pass")
            self.log.info("========= send pwd reset password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 30, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "send pwd reset password.png"))
            self.log.info("=========send pwd reset password FAILED ==========")
            assert False
        time.sleep(2)
        self.lo.clr_send_reset_pwd()
        self.lo.send_confirm_reset_pwd()
        self.lo.clk_change_reset_pwd()
        chk = self.lo.chk_reset_error_msg()
        if chk == "Please fill in all fields.":
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 31, 4, "pass")
            self.log.info("========= send confirm pwd reset confirm password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 31, 4, "fail")
            self.driver.save_screenshot(
                get_path("Screenshots", "reset confirm pwd password.png"))
            self.log.info("=========reset confirm pwd password FAILED ==========")
            assert False
        self.lo.send_reset_pwd()
        self.lo.clk_eye_icon_password()
        time.sleep(4)
        if self.lo.chk_eye_icon_password() == 'text':
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 32, 4, "pass")
            self.log.info("========= eye icon of password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 32, 4, "fail")
            self.driver.save_screenshot(
                get_path("Screenshots", "eye icon of password.png"))
            self.log.info("=========eye icon of password FAILED ==========")
            assert False
        self.lo.clk_eye_icon_con_password()
        time.sleep(4)
        if self.lo.chk_eye_icon_password() == 'text':
            assert True
            result = XLUtils.writeData(self.xl_path, "Login", 33, 4, "pass")
            self.log.info("========= eye icon of confirm password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Login", 33, 4, "fail")
            self.driver.save_screenshot(
                get_path("Screenshots", "eye icon of confirm password.png"))
            self.log.info("=========eye icon of confirm password FAILED ==========")
            assert False
        self.lo.clr_send_reset_pwd()

