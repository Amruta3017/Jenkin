import time

from selenium.webdriver.common.by import By

from PageObjects.Registration import Register
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

    def reload(self, setup):
        reload_button = self.driver.find_elements(By.XPATH, '//*[@id="reload-button"]')
        if reload_button:
            reload_button[0].click()
    def test_re_001(self, setup):
        self.log.info("========== Verifying URL==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Register", "test_re_001")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 5, 4, "pass")
            self.driver.close()
            self.log.info("==========Verifying URL PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 5, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "verify URL.png"))
            self.driver.close()
            self.log.info("=========Verifying URL FAILED ==========")
            assert Register

    def test_re_002(self, setup):
        self.log.info("========== Click Log In Button  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        chk = self.re.chk_login_dropdown_menu()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 6, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Log In Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 6, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Log In Button.png"))
            self.driver.close()
            self.log.info("========= Click Log In Button FAILED ==========")
            assert False

    def test_re_003(self, setup):
        self.log.info("========== Check Color of personal  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        befor_hover = self.re.get_css_personal()
        self.re.hover_personal()
        after_hover = self.re.get_css_personal()
        if befor_hover != after_hover:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 7, 4, "pass")
            self.driver.close()
            self.log.info("========== Check Color of personal PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 7, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Check Color of personal.png"))
            self.driver.close()
            self.log.info("========= Check Color of personal FAILED ==========")
            assert False

    def test_re_004(self, setup):
        self.log.info("========== Click Register Button of presonal ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Register", "test_re_004")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 8, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Register Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 8, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Register Button.png"))
            self.driver.close()
            self.log.info("=========Click Register Button FAILED ==========")
            assert False

    def test_re_005(self, setup):
        self.log.info("========== Click Back Button  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.clk_back()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Register", "test_re_005")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 9, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Back Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 9, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Back Button.png"))
            self.driver.close()
            self.log.info("=========Click Back Button FAILED ==========")
            assert False

    def test_re_006(self, setup):
        self.log.info("========== Click Register Button  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.clk_register()
        actual_msg = self.re.get_error_msg()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_006")
        print(expected_msg)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 10, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Register Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 10, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Register Button.png"))
            self.driver.close()
            self.log.info("=========Click Register Button FAILED ==========")
            assert False

    def test_re_007(self, setup):
        self.log.info("========== Click Login Button  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.clk_login_button()
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Register", "test_re_007")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 11, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Login Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 11, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Login Button.png"))
            self.driver.close()
            self.log.info("=========Click Login Button FAILED ==========")
            assert False

    def test_re_008(self, setup):
        self.log.info("========== enter email only  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.clk_register()
        actual_msg = self.re.get_error_msg()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_008")
        print(expected_msg)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 12, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Register Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 12, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Register Button.png"))
            self.driver.close()
            self.log.info("=========Click Register Button FAILED ==========")
            assert False

    def test_re_009(self, setup):
        self.log.info("========== enter email and password  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password()
        self.re.clk_register()
        actual_msg = self.re.get_error_msg()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_009")
        print(expected_msg)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 13, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Register Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 13, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Register Button.png"))
            self.driver.close()
            self.log.info("=========Click Register Button FAILED ==========")
            assert False

    def test_re_010(self, setup):
        self.log.info("========== enter email,password,confirm password  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password()
        self.re.send_confirm_password()
        self.re.clk_register()
        time.sleep(10)
        chk = self.re.get_verify_msg()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 14, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Register Button PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 14, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Register Button.png"))
            self.driver.close()
            self.log.info("=========Click Register Button FAILED ==========")
            assert False

    def test_re_011(self, setup):
        self.log.info("========== Click Go to Email  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password()
        self.re.send_confirm_password()
        self.re.clk_register()
        time.sleep(10)
        self.re.clk_go_to_email()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        chk = self.re.chk_sign_in_go_to_email()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 15, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Go to Email PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 15, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Go to Email.png"))
            self.driver.close()
            self.log.info("=========Click Go to Email  FAILED ==========")
            assert False

    def test_re_012(self, setup):
        self.log.info("========== Click Close Go to Email  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password()
        self.re.send_confirm_password()
        self.re.clk_register()
        time.sleep(10)
        self.re.clk_close_go_to_email()
        chk = self.re.chk_go_to_email_pop()
        if chk == False:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 16, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Close Go to Email PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 16, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Close Go to Email.png"))
            self.driver.close()
            self.log.info("=========Click Close Go to Email  FAILED ==========")
            assert False
    def test_re_013(self, setup):
        self.log.info("========== Enter previouslly added email, password and Confirm password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_Existed_email()
        self.re.send_password()
        self.re.send_confirm_password()
        self.re.clk_register()
        time.sleep(2)
        actual_msg = self.re.get_error_msg()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_013")
        print(expected_msg)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 17, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter previouslly added email, password and Confirm password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 17, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter previouslly added email, password and Confirm password.png"))
            self.driver.close()
            self.log.info("=========Enter previouslly added email, password and Confirm password FAILED ==========")
            assert False

    def test_re_014(self, setup):
        self.log.info("==========Enter invalid email, password and Confirm password ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_invalid_email()
        self.re.send_password()
        self.re.send_confirm_password()
        self.re.clk_register()
        time.sleep(2)
        actual_msg = self.re.get_error_msg0()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_014")
        print(expected_msg)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 18, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter invalid email, password and Confirm password PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 18, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter invalid email, password and Confirm password.png"))
            self.driver.close()
            self.log.info("=========Enter invalid email, password and Confirm password FAILED ==========")
            assert False

    def test_re_015(self, setup):
        self.log.info("==========Enter valid email, password and Confirm password different ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password()
        self.re.send_confirm_password2()
        self.re.clk_register()
        time.sleep(2)
        actual_msg = self.re.get_error_msg()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_015")
        print(expected_msg)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 19, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter valid email, password and Confirm password different PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 19, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter valid email, password and Confirm password different.png"))
            self.driver.close()
            self.log.info("=========Enter valid email, password and Confirm password different FAILED ==========")
            assert False

    def test_re_016(self, setup):
        self.log.info("==========Click Password eye Icon ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password()
        self.re.clk_eye_icon_password()
        time.sleep(4)
        if self.re.chk_eye_icon_password() == 'text':
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 20, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Password eye Icon PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 20, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Password eye Icon.png"))
            self.driver.close()
            self.log.info("=========Click Password eye Icon FAILED ==========")
            assert False

    def test_re_017(self, setup):
        self.log.info("==========Click Confirm Password eye Icon ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password()
        # self.re.clk_eye_icon_password()
        # time.sleep(4)
        self.re.send_confirm_password()
        time.sleep(2)
        self.re.clk_eye_icon_confirm_pwd()
        time.sleep(7)
        if self.re.chk_eye_icon_confirm_pwd() == 'text':
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 21, 4, "pass")
            self.driver.close()
            self.log.info("=========Click Confirm Password eye Icon PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 21, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Confirm Password eye Icon.png"))
            self.driver.close()
            self.log.info("=========Click Confirm Password eye Icon FAILED ==========")
            assert False

    def test_re_018(self, setup):
        self.log.info("==========Enter Small letter and check Checkbox ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        before_enter = self.re.get_css_small_ch_box()
        txt = XLUtils.readExpData(self.xl_path, "Register", "test_re_018")
        self.re.send_password1(txt)
        after_enter = self.re.get_css_small_ch_box()
        if before_enter == after_enter:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 22, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter Small letter and check Checkbox PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 22, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter Small letter and check Checkbox.png"))
            self.driver.close()
            self.log.info("=========Enter Small letter and check Checkbox FAILED ==========")
            assert False

    def test_re_019(self, setup):
        self.log.info("==========Enter Capital letter and check Checkbox ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        before_enter = self.re.get_css_small_ch_box()
        txt = XLUtils.readExpData(self.xl_path, "Register", "test_re_019")
        self.re.send_password1(txt)
        after_enter = self.re.get_css_small_ch_box()
        if before_enter == after_enter:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 23, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter Capital letter and check Checkbox PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 23, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter Capital letter and check Checkbox.png"))
            self.driver.close()
            self.log.info("=========Enter Capital letter and check Checkbox FAILED ==========")
            assert False

    def test_re_020(self, setup):
        self.log.info("==========Enter Digit letter and check Checkbox ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        before_enter = self.re.get_css_small_ch_box()
        txt = XLUtils.readExpData(self.xl_path, "Register", "test_re_020")
        self.re.send_password1(txt)
        after_enter = self.re.get_css_small_ch_box()
        if before_enter == after_enter:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 24, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter Digit and check Checkbox PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 24, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter Digit letter and check Checkbox.png"))
            self.driver.close()
            self.log.info("=========Enter Digit letter and check Checkbox FAILED ==========")
            assert False

    def test_re_021(self, setup):
        self.log.info("==========Enter Samll letter and capital letter only ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password2()
        self.re.send_confirm_password2()
        self.re.clk_register()
        actual_msg = self.re.get_error_msg1()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_021")
        print(expected_msg)
        time.sleep(50)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 25, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter Samll letter and capital letter only PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 25, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter Samll letter and capital letter only.png"))
            self.driver.close()
            self.log.info("=========Enter Samll letter and capital letter only FAILED ==========")
            assert False

    def test_re_022(self, setup):
        self.log.info("==========Enter Samll letter and Digit ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password4()
        self.re.send_confirm_password4()
        self.re.clk_register()
        actual_msg = self.re.get_error_msg1()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_022")
        print(expected_msg)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 26, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter Samll letter and Digit PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 26, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter Samll letter and Digit.png"))
            self.driver.close()
            self.log.info("=========Enter Samll letter and Digit FAILED ==========")
            assert False

    def test_re_023(self, setup):
        self.log.info("==========Enter capital letter and Digit only ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.re = Register(self.driver)
        self.re.clk_log_in()
        self.re.clk_per_register()
        self.re.send_email()
        self.re.send_password3()
        self.re.send_confirm_password3()
        self.re.clk_register()
        actual_msg = self.re.get_error_msg1()
        print(actual_msg)
        expected_msg = XLUtils.readExpData(self.xl_path, "Register", "test_re_023")
        print(expected_msg)
        if actual_msg == expected_msg:
            assert True
            result = XLUtils.writeData(self.xl_path, "Register", 27, 4, "pass")
            self.driver.close()
            self.log.info("=========Enter capital letter and Digit only PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Register", 27, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Enter capital letter and Digit only.png"))
            self.driver.close()
            self.log.info("=========Enter capital letter and Digit only FAILED ==========")
            assert False

