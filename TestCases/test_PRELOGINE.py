import time
import re
from selenium.webdriver.common.by import By
from PageObjects.PreLoginPage import PreLogin
from Utilities import XLUtils
from Utilities.readProperties import ReadConfig
from Utilities.commonMethods import get_path
from Utilities.customLogger import LogGen

class Test_PreLogin:
    baseURL = ReadConfig.get_app_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    logger = LogGen()
    log = logger.configure_logger()

    xl_path = get_path("TestData", "Testcases_PreLogin.xlsx")
    #xl_path = get_path("TestData", "Test_cases_Pre_Login_QA.xlsx")
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

    def test_pl_001(self, setup):
        self.log.info("========== Verifying URL of prelogin page ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_001")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 5, 4, "pass")
            self.driver.close()
            self.log.info("==========Verifying URL of prelogin page PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 5, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "verify URL.png"))
            self.driver.close()
            self.log.info("=========Verifying URL of prelogin page FAILED ==========")
            assert False

    def test_pl_002(self, setup):
        self.log.info("========== Click Idea  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_idea()
        time.sleep(5)
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_002")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 6, 4, "pass")
            self.driver.close()
            self.log.info("==========VClick Idea PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 6, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Idea.png"))
            self.driver.close()
            self.log.info("=========Click Idea FAILED ==========")
            assert False

    def test_pl_003(self, setup):
        self.log.info("========== Click script  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_script()
        time.sleep(5)
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_003")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 7, 4, "pass")
            self.driver.close()
            self.log.info("==========Click script PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 7, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click script.png"))
            self.driver.close()
            self.log.info("=========Click script FAILED ==========")
            assert False


    def test_pl_004(self, setup):
        self.log.info("========== Click translate  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_translate()
        time.sleep(5)
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_004")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 8, 4, "pass")
            self.driver.close()
            self.log.info("==========VClick translate PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 8, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click translate.png"))
            self.driver.close()
            self.log.info("=========Click translate FAILED ==========")
            assert False


    def test_pl_005(self, setup):
        self.log.info("========== Click narrate  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_narrate()
        time.sleep(5)
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_005")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 9, 4, "pass")
            self.driver.close()
            self.log.info("==========Click narrate PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 9, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click narrate.png"))
            self.driver.close()
            self.log.info("=========Click narrate FAILED ==========")
            assert False


    def test_pl_006(self, setup):
        self.log.info("========== Click Build Team  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_buildTeam()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_006")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 10, 4, "pass")
            self.driver.close()
            self.log.info("==========Click Build Team PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 10, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Build Team.png"))
            self.driver.close()
            self.log.info("=========Click Build Team FAILED ==========")
            assert False

    def test_pl_007(self, setup):
        self.log.info("========== Click produce  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_produce()
        time.sleep(5)
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_007")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 11, 4, "pass")
            self.driver.close()
            self.log.info("==========Click produce PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 11, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click produce.png"))
            self.driver.close()
            self.log.info("=========Click produce FAILED ==========")
            assert False

    def test_pl_008(self, setup):
        self.log.info("========== Click subtitle  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_subtitle()
        time.sleep(5)
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_008")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 12, 4, "pass")
            self.driver.close()
            self.log.info("==========Click subtitle PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 12, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click subtitle.png"))
            self.driver.close()
            self.log.info("=========Click subtitle FAILED ==========")
            assert False

    def test_pl_009(self, setup):
        self.log.info("========== Click exhibit  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_exhibit()
        time.sleep(5)
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_009")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 13, 4, "pass")
            self.driver.close()
            self.log.info("==========Click Bexhibit PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 13, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click exhibit .png"))
            self.driver.close()
            self.log.info("=========Click exhibit FAILED ==========")
            assert False

    def test_pl_010(self, setup):
        self.log.info("========== Verify email address  ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        #self.pl.scroll()
        self.driver.execute_script("window.scrollBy(0, 500);")
        actual_text = self.pl.get_email_id()
        print(actual_text)
        expected_text = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_010")
        print(expected_text)
        if actual_text == expected_text:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 14, 4, "pass")
            self.driver.close()
            self.log.info("==========Verify email address PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 14, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Verify email address.png"))
            self.driver.close()
            self.log.info("=========Verify email address FAILED ==========")
            assert False

    def test_pl_011(self, setup):
        self.log.info("========== click facebook ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll()
        time.sleep(5)
        self.pl.clk_facebook()
        time.sleep(5)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_011")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 15, 4, "pass")
            self.driver.close()
            self.log.info("==========click facebook PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 15, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "click facebook.png"))
            self.driver.close()
            self.log.info("=========click facebook FAILED ==========")
            assert False

    def test_pl_012(self, setup):
        self.log.info("========== click twter ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll()
        self.pl.clk_twter()
        time.sleep(5)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_012")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 16, 4, "pass")
            self.driver.close()
            self.log.info("==========click twter PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 16, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "click twter.png"))
            self.driver.close()
            self.log.info("=========click twter FAILED ==========")
            assert False

    def test_pl_013(self, setup):
        self.log.info("========== click youtube ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll()
        self.pl.clk_youtube()
        time.sleep(5)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_013")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 17, 4, "pass")
            self.driver.close()
            self.log.info("==========click youtube PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 17, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "click youtube.png"))
            self.driver.close()
            self.log.info("=========click youtube FAILED ==========")
            assert False

    def test_pl_014(self, setup):
        self.log.info("========== click linked in ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll()
        self.pl.clk_linked_in()
        time.sleep(5)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_014")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 14, 4, "pass")
            self.driver.close()
            self.log.info("==========click linked in PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 14, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "click linked_in.png"))
            self.driver.close()
            self.log.info("=========click linked in FAILED ==========")
            assert False

    # def test_pl_015(self, setup):
    #     self.log.info("========== click IMDB ==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #       self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.scroll()
    #     self.pl.clk_imdb()
    #     time.sleep(5)
    #     chk = alert = self.driver.switch_to.alert
    #     alert.accept()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 19, 4, "pass")
    #         self.driver.close()
    #         self.log.info("==========click IMDB PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 19, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "click IMDB.png"))
    #         self.driver.close()
    #         self.log.info("=========click IMDB FAILED ==========")
    #         assert False

    def test_pl_016(self, setup):
        self.log.info("========== click threads ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll()
        self.pl.clk_threads_in()
        time.sleep(5)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_016")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 20, 4, "pass")
            self.driver.close()
            self.log.info("==========click threads PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 20, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "click threads.png"))
            self.driver.close()
            self.log.info("=========click threads FAILED ==========")
            assert False

    def test_pl_017(self, setup):
        self.log.info("========== click pinterest ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll()
        self.pl.clk_pinterest()
        time.sleep(5)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_017")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 21, 4, "pass")
            self.driver.close()
            self.log.info("==========click pinterest PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 21, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "click pinterest.png"))
            self.driver.close()
            self.log.info("=========click pinterest FAILED ==========")
            assert False

    def test_pl_018(self, setup):
        self.log.info("========== click instagram ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll()
        self.pl.clk_instagram()
        time.sleep(5)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        actual_url = self.driver.current_url
        print(actual_url)
        expected_url = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_018")
        print(expected_url)
        if actual_url == expected_url:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 22, 4, "pass")
            self.driver.close()
            self.log.info("==========click instagram PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 22, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "click instagram.png"))
            self.driver.close()
            self.log.info("=========click instagram FAILED ==========")
            assert False
    def test_pl_019(self, setup):
        self.log.info("========== mouse hover on Explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        chk = self.pl.chk_dropdown_menu()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 23, 4, "pass")
            self.driver.close()
            self.log.info("==========mouse hover on Explore PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 23, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "mouse hover on Explore.png"))
            self.driver.close()
            self.log.info("=========mouse hover on Explore FAILED ==========")
            assert False

    def test_pl_020(self, setup):
        self.log.info("========== Click Promises on explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        chk = self.pl.chk_promises()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 24, 4, "pass")
            self.driver.close()
            self.log.info("==========Click Promises PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 24, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Promises.png"))
            self.driver.close()
            self.log.info("=========Click Promises FAILED ==========")
            assert False

    def test_pl_021(self, setup):
        self.log.info("========== Click premises pool in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_premises_pool()
        time.sleep(4)
        chk = self.pl.chk_premises_pool()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 25, 4, "pass")
            self.driver.close()
            self.log.info("==========Click premises pool PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 25, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click premises pool.png"))
            self.driver.close()
            self.log.info("=========Click premises pool FAILED ==========")
            assert False

    def test_pl_022(self, setup):
        self.log.info("========== Click sound icon of premises pool in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_premises_pool()
        self.pl.scroll1()
        self.pl.clk_sound_premises_pool()
        time.sleep(5)
        chk = self.pl.chk_hd_icon_premises_pool()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 26, 4, "pass")
            self.driver.close()
            self.log.info("==========Click script builder PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 26, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click script builder.png"))
            self.driver.close()
            self.log.info("=========Click script builder FAILED ==========")
            assert False

    def test_pl_023(self, setup):
        self.log.info("========== Click script builder in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_script_builder()
        time.sleep(5)
        chk = self.pl.chk_script_builder()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 27, 4, "pass")
            self.driver.close()
            self.log.info("==========Click script builder PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 27, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click script builder.png"))
            self.driver.close()
            self.log.info("=========Click script builder FAILED ==========")
            assert False

    def test_pl_024(self, setup):
        self.log.info("========== Click sound of script builder in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_script_builder()
        self.pl.scroll2()
        self.pl.clk_sound_script_builder()
        time.sleep(4)
        chk = self.pl.chk_hd_icon_script_builderl()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 28, 4, "pass")
            self.driver.close()
            self.log.info("==========Click sound of script builder PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 28, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click sound of script builder.png"))
            self.driver.close()
            self.log.info("=========Click sound of script builder FAILED ==========")
            assert False

    def test_pl_025(self, setup):
        self.log.info("========== Click screenplay conversion in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_screenplay_conversion()
        time.sleep(4)
        chk = self.pl.chk_screenplay_conversion()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 29, 4, "pass")
            self.driver.close()
            self.log.info("==========Click screenplay conversion PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 29, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click screenplay conversion.png"))
            self.driver.close()
            self.log.info("=========Click screenplay conversion FAILED ==========")
            assert False

    def test_pl_026(self, setup):
        self.log.info("========== Click sound of screenplay conversion in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_screenplay_conversion()
        self.pl.scroll3()
        self.pl.clk_sound_screenplay_conversion()
        time.sleep(5)
        chk = self.pl.chk_hd_icon_screenplay_conversion()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 30, 4, "pass")
            self.driver.close()
            self.log.info("==========Click screenplay conversion PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 30, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click sound scrply con.png"))
            self.driver.close()
            self.log.info("=========Click screenplay conversion FAILED ==========")
            assert False

    def test_pl_027(self, setup):
        self.log.info("========== Click pitchdech narration in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pitchdeck_creation()
        chk = self.pl.chk_pitchdeck_creation()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 31, 4, "pass")
            self.driver.close()
            self.log.info("==========Click pitchdech narration PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 31, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click pitchdech narration.png"))
            self.driver.close()
            self.log.info("=========Click pitchdech narration FAILED ==========")
            assert False

    def test_pl_028(self, setup):
        self.log.info("========== Click sound of pitchdech narration in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pitchdeck_creation()
        self.pl.scroll4()
        self.pl.clk_sound_pitchdeck_creation()
        time.sleep(4)
        chk = self.pl.chk_hd_icon_pitchdeck_creation()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 32, 4, "pass")
            self.driver.close()
            self.log.info("==========Click pitchdech narration sound PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 32, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click pitchdech narration sound.png"))
            self.driver.close()
            self.log.info("=========Click pitchdech narration sound FAILED ==========")
            assert False

    def test_pl_029(self, setup):
        self.log.info("========== Click screenplay narration in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_screenplay_narration()
        chk = self.pl.chk_screenplay_narration()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 33, 4, "pass")
            self.driver.close()
            self.log.info("==========Click screenplay narration PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 33, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click screenplay narration.png"))
            self.driver.close()
            self.log.info("=========Click screenplay narration FAILED ==========")
            assert False

    def test_pl_030(self, setup):
        self.log.info("========== Click sound of screenplay narration in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_screenplay_narration()
        self.pl.scroll5()
        self.pl.clk_sound_screenplay_narration()
        time.sleep(4)
        chk = self.pl.chk_hd_icon_screenplay_narration()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 34, 4, "pass")
            self.driver.close()
            self.log.info("==========Click screenplay narration sound PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 34, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click screenplay narration sound.png"))
            self.driver.close()
            self.log.info("=========Click screenplay narration sound FAILED ==========")
            assert False

    def test_pl_031(self, setup):
        self.log.info("========== Click harkat clubs in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_harkat_clubs()
        chk = self.pl.chk_harkat_clubs()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 35, 4, "pass")
            self.driver.close()
            self.log.info("==========Click harkat clubs PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 35, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click harkat clubs.png"))
            self.driver.close()
            self.log.info("=========Click harkat clubs FAILED ==========")
            assert False

    def test_pl_032(self, setup):
        self.log.info("========== Click sound of harkat clubs in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_harkat_clubs()
        self.pl.scroll6()
        self.pl.clk_sound_harkat_clubs()
        time.sleep(4)
        chk = self.pl.chk_hd_icon_harkat_clubs()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 36, 4, "pass")
            self.driver.close()
            self.log.info("==========Click harkat clubs sound PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 36, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click harkat clubs sound.png"))
            self.driver.close()
            self.log.info("=========Click harkat clubs sound FAILED ==========")
            assert False

    def test_pl_033(self, setup):
        self.log.info("========== Click project center in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_project_center()
        chk = self.pl.chk_project_center()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 37, 4, "pass")
            self.driver.close()
            self.log.info("==========Click project center PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 37, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click project center.png"))
            self.driver.close()
            self.log.info("=========Click project center FAILED ==========")
            assert False

    def test_pl_034(self, setup):
        self.log.info("========== Click sound of project center in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_project_center()
        self.pl.scroll7()
        self.pl.clk_sound_project_center()
        time.sleep(5)
        chk = self.pl.chk_hd_icon_project_center()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 38, 4, "pass")
            self.driver.close()
            self.log.info("==========Click project center sound PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 38, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click project center sound.png"))
            self.driver.close()
            self.log.info("=========Click project center sound FAILED ==========")
            assert False

    def test_pl_035(self, setup):
        self.log.info("========== Click subtitle hub in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_subtitle_hub()
        chk = self.pl.chk_subtitle_hub()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 39, 4, "pass")
            self.driver.close()
            self.log.info("==========Click subtitle hub PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 39, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click subtitle hub.png"))
            self.driver.close()
            self.log.info("=========Click subtitle hub FAILED ==========")
            assert False

    def test_pl_036(self, setup):
        self.log.info("========== Click sound of subtitle hub in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_subtitle_hub()
        self.pl.scroll8()
        self.pl.clk_sound_subtitle_hub()
        time.sleep(5)
        chk = self.pl.chk_hd_icon_subtitle_hub()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 40, 4, "pass")
            self.driver.close()
            self.log.info("==========Click subtitle hub sound PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 40, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click subtitle hub sound.png"))
            self.driver.close()
            self.log.info("=========Click subtitle hub sound FAILED ==========")
            assert False

    def test_pl_037(self, setup):
        self.log.info("========== Click Viewing Lounge in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_Viewing_Lounge()
        chk = self.pl.chk_Viewing_Lounge()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 41, 4, "pass")
            self.driver.close()
            self.log.info("==========Click Viewing Lounge PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 41, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Viewing Lounge.png"))
            self.driver.close()
            self.log.info("=========Click Viewing Lounge FAILED ==========")
            assert False

    def test_pl_038(self, setup):
        self.log.info("========== Click sound of Viewing Lounge in Promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_Viewing_Lounge()
        self.pl.scroll9()
        self.pl.clk_sound_Viewing_Lounge()
        time.sleep(5)
        chk = self.pl.chk_hd_icon_Viewing_Lounge()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 42, 4, "pass")
            self.driver.close()
            self.log.info("==========Click Viewing Lounge sound PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 42, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Viewing Lounge sound.png"))
            self.driver.close()
            self.log.info("=========Click Viewing Lounge sound FAILED ==========")
            assert False

    def test_pl_039(self, setup):
        self.log.info("========== Click idea image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_idea_img()
        chk = self.pl.chk_hd_icon_premises_pool()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 43, 4, "pass")
            self.driver.close()
            self.log.info("==========Click idea image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 43, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click idea image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click idea image of pricing FAILED ==========")
            assert False

    def test_pl_040(self, setup):
        self.log.info("========== Click script image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_script_img()
        chk = self.pl.chk_hd_icon_script_builderl()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 44, 4, "pass")
            self.driver.close()
            self.log.info("==========Click script image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 44, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click script image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click script image of pricing FAILED ==========")
            assert False

    def test_pl_041(self, setup):
        self.log.info("========== Click translate image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_translate_img()
        chk = self.pl.chk_hd_icon_screenplay_conversion()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 45, 4, "pass")
            self.driver.close()
            self.log.info("==========Click translate image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 45, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click translate image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click translate image of pricing FAILED ==========")
            assert False

    def test_pl_042(self, setup):
        self.log.info("========== Click pitchdack image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_pitchdack_img()
        chk = self.pl.chk_hd_icon_pitchdeck_creation()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 46, 4, "pass")
            self.driver.close()
            self.log.info("==========Click pitchdack image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 46, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click pitchdack image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click pitchdack image of pricing FAILED ==========")
            assert False

    def test_pl_043(self, setup):
        self.log.info("========== Click narrate image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_narrate_img()
        chk = self.pl.chk_hd_icon_screenplay_narration()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 47, 4, "pass")
            self.driver.close()
            self.log.info("==========Click narrate image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 47, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click narrate image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click narrate image of pricing FAILED ==========")
            assert False

    def test_pl_044(self, setup):
        self.log.info("========== Click build team image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_build_team_img()
        chk = self.pl.chk_hd_icon_harkat_clubs()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 48, 4, "pass")
            self.driver.close()
            self.log.info("==========Click build team image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 48, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click build team image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click build team image of pricing FAILED ==========")
            assert False

    def test_pl_045(self, setup):
        self.log.info("========== Click produce image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_produce_img()
        chk = self.pl.chk_hd_icon_project_center()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 49, 4, "pass")
            self.driver.close()
            self.log.info("==========Click produce image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 49, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click produce image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click produce image of pricing FAILED ==========")
            assert False

    def test_pl_046(self, setup):
        self.log.info("========== Click subtitle image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_subtitle_img()
        chk = self.pl.chk_hd_icon_subtitle_hub()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 50, 4, "pass")
            self.driver.close()
            self.log.info("==========Click subtitle image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 50, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click subtitle image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click subtitle image of pricing FAILED ==========")
            assert False

    def test_pl_047(self, setup):
        self.log.info("========== Click exhibit image of promises of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_promises()
        self.pl.clk_exhibit_img()
        chk = self.pl.chk_hd_icon_Viewing_Lounge()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 51, 4, "pass")
            self.driver.close()
            self.log.info("==========Click exhibit image of pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 51, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click exhibit image of Promises.png"))
            self.driver.close()
            self.log.info("=========Click exhibit image of pricing FAILED ==========")
            assert False

    def test_pl_048(self, setup):
        self.log.info("========== Click Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pricing()
        chk = self.pl.chk_pricing()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 52, 4, "pass")
            self.driver.close()
            self.log.info("==========Click Pricing of explore PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 52, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Pricing of explore.png"))
            self.driver.close()
            self.log.info("=========Click Pricing of explore FAILED ==========")
            assert False

    def test_pl_049(self, setup):
        self.log.info("========== Click free services of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_free_services()
        chk = self.pl.chk_free_services()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 53, 4, "pass")
            self.driver.close()
            self.log.info("========== Click free services of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 53, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click free services of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click free services of Pricing FAILED ==========")
            assert False

    def test_pl_050(self, setup):
        self.log.info("========== Click discounts of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_discounts()
        chk = self.pl.chk_discounts()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 54, 4, "pass")
            self.driver.close()
            self.log.info("========== Click discounts of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 54, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click discounts of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click discounts of Pricing FAILED ==========")
            assert False

    def test_pl_051(self, setup):
        self.log.info("========== Click  jug_pack_scr_writer of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_jug_pack_scr_writer()
        chk = alert = self.driver.switch_to.alert
        alert.accept()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 55, 4, "pass")
            self.driver.close()
            self.log.info("========== Click jug_pack_scr_writer of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 55, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click jug_pack_scr_writer of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click jug_pack_scr_writer of Pricing FAILED ==========")
            assert False

    def test_pl_052(self, setup):
        self.log.info("========== Click jug_pack_scr_house of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_jug_pack_prod_house()
        chk = alert = self.driver.switch_to.alert
        alert.accept()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 56, 4, "pass")
            self.driver.close()
            self.log.info("========== Click jug_pack_scr_house of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 56, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click jug_pack_scr_house of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click jug_pack_scr_house of Pricing FAILED ==========")
            assert False

    def test_pl_053(self, setup):
        self.log.info("========== Click subtitling of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_subtitling()
        chk = self.pl.chk_subtitling()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 57, 4, "pass")
            self.driver.close()
            self.log.info("========== Click subtitling of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 57, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click subtitling of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click subtitling of Pricing FAILED ==========")
            assert False

    def test_pl_054(self, setup):
        self.log.info("========== Click screenplay_con_pricin of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_screenplay_con_pricing()
        chk = self.pl.chk_screenplay_con_pricing()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 58, 4, "pass")
            self.driver.close()
            self.log.info("========== Click screenplay_con_pricin of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 58, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click screenplay_con_pricin of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click screenplay_con_pricin of Pricing FAILED ==========")
            assert False

    def test_pl_055(self, setup):
        self.log.info("========== Click scheduling_budjeting of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_scheduling_budjeting()
        chk = self.pl.chk_scheduling_budjeting()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 59, 4, "pass")
            self.driver.close()
            self.log.info("========== Click scheduling_budjeting of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 59, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click scheduling_budjeting of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click scheduling_budjeting of Pricing FAILED ==========")
            assert False

    def test_pl_056(self, setup):
        self.log.info("========== Click pitchdeck_creation of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pitchdeck_creation_pricing()
        chk = self.pl.chk_pitchdeck_creation_pricing()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 60, 4, "pass")
            self.driver.close()
            self.log.info("========== Click pitchdeck_creation of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 60, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click pitchdeck_creation of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click pitchdeck_creation of Pricing FAILED ==========")
            assert False

    def test_pl_57(self, setup):
        self.log.info("========== Click screenplay narration of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_scrplay_narration_pricing()
        chk = self.pl.chk_scrplay_narration_pricing()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 61, 4, "pass")
            self.driver.close()
            self.log.info("========== Click screenplay narration of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 61, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click screenplay narration of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click screenplay narration of Pricing FAILED ==========")
            assert False

    def test_pl_58(self, setup):
        self.log.info("========== Click pricing_calculator of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pricing_calculator()
        chk = self.pl.chk_pricing_cal_img()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 62, 4, "pass")
            self.driver.close()
            self.log.info("========== Click pricing_calculator of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 62, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click pricing_calculator of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click pricing_calculator of Pricing FAILED ==========")
            assert False

    def test_pl_59(self, setup):
        self.log.info("========== Click jug_pack_scr_writer_img of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pricing()
        self.pl.clk_jug_pack_scr_writer_img()
        chk = alert = self.driver.switch_to.alert
        alert.accept()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 63, 4, "pass")
            self.driver.close()
            self.log.info("========== Click jug_pack_scr_writer_img of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 63, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click jug_pack_scr_writer_img of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click jug_pack_scr_writer_img of Pricing FAILED ==========")
            assert False

    def test_pl_60(self, setup):
        self.log.info("========== Click jug_pack_prod_house_img of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pricing()
        self.pl.clk_jug_pack_prod_house_img()
        chk = alert = self.driver.switch_to.alert
        alert.accept()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 64, 4, "pass")
            self.driver.close()
            self.log.info("========== Click jug_pack_prod_house_img of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 64, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click jug_pack_prod_house_img of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click jug_pack_prod_house_img of Pricing FAILED ==========")
            assert False

    def test_pl_61(self, setup):
        self.log.info("========== Click pricing_calculator_img of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pricing()
        self.pl.clk_pricing_calculator_img()
        chk = self.pl.chk_pricing_calculator_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 65, 4, "pass")
            self.driver.close()
            self.log.info("========== Click pricing_calculator_img of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 65, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click pricing_calculator_img of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click pricing_calculator_img of Pricing FAILED ==========")
            assert False

    def test_pl_62(self, setup):
        self.log.info("========== Click pricing_calculator_pop_close of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pricing()
        self.pl.clk_pricing_calculator_img()
        self.pl.clk_cl_pricing_calculator_pop()
        chk = self.pl.chk_pricing_calculator_pop()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 66, 4, "pass")
            self.driver.close()
            self.log.info("========== Click pricing_calculator_pop_close of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 66, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click pricing_calculator_pop_close of Pricing.png"))
            self.driver.close()
            self.log.info("========= Click pricing_calculator_pop_close of Pricing FAILED ==========")
            assert False
    #
    # def test_pl_63(self, setup):
    #     self.log.info("========== Click opportunities of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_opportunities()
    #     chk = self.pl.chk_opportunities()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 67, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click opportunities PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 67, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click opportunities.png"))
    #         self.driver.close()
    #         self.log.info("========= Click opportunities FAILED ==========")
    #         assert False
    #
    # def test_pl_64(self, setup):
    #     self.log.info("========== Click refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     chk = self.pl.chk_refer_mnf()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 68, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 68, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= Click refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_65(self, setup):
    #     self.log.info("========== Click sound of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_sound_refer_mnf()
    #     time.sleep(5)
    #     chk = self.pl.chk_hd_refer_mnf()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 69, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click sound of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 69, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click sound of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= Click sound of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_66(self, setup):
    #     self.log.info("========== Click refer button of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(5)
    #     chk = self.pl.chk_refer_mnf_pop()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 70, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click refer button of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 70, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click refer button of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= Click refer button of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_67(self, setup):
    #     self.log.info("========== Click close_refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(5)
    #     self.pl.clk_cl_refer_mnf_pop()
    #     chk = self.pl.chk_refer_mnf_pop()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 71, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click close_refer_pop of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 71, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click close_refer_pop of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= Click close_refer_pop of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_68(self, setup):
    #     self.log.info("========== send email1 on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(5)
    #     self.pl.send_email1()
    #     time.sleep(2)
    #     chk = self.pl.chk_continue_btn_enable()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 72, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== send email on refer_pop of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 72, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "send email on refer_pop of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= send email on refer_pop of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_69(self, setup):
    #     self.log.info("========== click add another on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(5)
    #     self.pl.send_email1()
    #     self.pl.clk_add_another_btn()
    #     chk = self.pl.chk_email2_tb()
    #     if chk == True:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 73, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== click add another on refer_pop of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 73, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "click add another on refer_pop of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= click add another on refer_pop of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_70(self, setup):
    #     self.log.info("========== send same email1 on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email2()
    #     time.sleep(2)
    #     self.pl.clk_add_another_btn()
    #     time.sleep(2)
    #     self.pl.send_email3()
    #     self.pl.clk_add_another_btn()
    #     chk = self.pl.chk_same_email_error()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 74, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== send same email on refer_pop of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 74, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "send same email on refer_pop of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= send same email on refer_pop of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_71(self, setup):
    #     self.log.info("========== delete email1 on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email1()
    #     time.sleep(2)
    #     self.pl.clk_add_another_btn()
    #     self.pl.send_email3()
    #     self.pl.clk_delete_btn()
    #     chk = self.pl.chk_email2_tb()
    #     if chk == False:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 75, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== delete email on refer_pop of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 75, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "delete email on refer_pop of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= delete email on refer_pop of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_72(self, setup):
    #     self.log.info("========== add five email1 on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(5)
    #     self.pl.send_email1()
    #     time.sleep(2)
    #     self.pl.clk_add_another_btn()
    #     self.pl.send_email_tb2()
    #     self.pl.clk_add_another_btn()
    #     self.pl.send_email_tb3()
    #     self.pl.clk_add_another_btn()
    #     self.pl.send_email_tb4()
    #     self.pl.clk_add_another_btn()
    #     self.pl.send_email_tb5()
    #     self.pl.clk_add_another_btn()
    #     chk = self.pl.chk_max_5_email_error()
    #     if chk == True:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 76, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== delete email on refer_pop of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 76, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "delete email on refer_pop of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= delete email on refer_pop of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_73(self, setup):
    #     self.log.info("========== click continue button on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(5)
    #     self.pl.send_email1()
    #     self.pl.clk_continue_btn()
    #     time.sleep(2)
    #     chk = self.pl.chk_continue_pop()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 77, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== click continue on refer_pop of refer_mnf PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 77, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "click continue on refer_pop of refer_mnf.png"))
    #         self.driver.close()
    #         self.log.info("========= click continue on refer_pop of refer_mnf FAILED ==========")
    #         assert False
    #
    # def test_pl_74(self, setup):
    #     self.log.info("========== click close of continue pop on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email1()
    #     self.pl.clk_continue_btn()
    #     time.sleep(2)
    #     self.pl.clk_cl_continue_btn_pop()
    #     chk = self.pl.chk_continue_pop()
    #     if chk == True:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 78, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== click close of continue pop PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 78, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "click close of continue pop.png"))
    #         self.driver.close()
    #         self.log.info("========= click close of continue pop FAILED ==========")
    #         assert False
    #
    # def test_pl_75(self, setup):# cheack
    #     self.log.info("========== send your name of continue pop on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email1()
    #     self.pl.clk_continue_btn()
    #     time.sleep(2)
    #     self.pl.send_your_name()
    #     time.sleep(5)
    #     chk = self.pl.chk_refer_btn()
    #     if chk == False:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 79, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== send your name continue pop PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 79, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "send your name continue pop.png"))
    #         self.driver.close()
    #         self.log.info("========= send your name continue pop FAILED ==========")
    #         assert False
    #
    # def test_pl_76(self, setup):
    #     self.log.info("========== send email of continue pop on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email1()
    #     self.pl.clk_continue_btn()
    #     time.sleep(2)
    #     self.pl.send_your_name()
    #     self.pl.send_your_email()
    #     chk = self.pl.chk_refer_btn()
    #     if chk == True:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 80, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== send email continue pop PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 80, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "send email continue pop.png"))
    #         self.driver.close()
    #         self.log.info("========= send email continue pop FAILED ==========")
    #         assert False
    #
    # def test_pl_77(self, setup):
    #     self.log.info("========== select country code of continue pop on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email1()
    #     self.pl.clk_continue_btn()
    #     time.sleep(2)
    #     self.pl.send_your_name()
    #     self.pl.send_your_email()
    #     self.pl.send_country_code()
    #     chk = self.pl.chk_refer_btn()
    #     if chk == True:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 81, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== select country code continue pop PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 81, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "select country code continue pop.png"))
    #         self.driver.close()
    #         self.log.info("========= select country code continue pop FAILED ==========")
    #         assert False
    #
    # def test_pl_78(self, setup):
    #     self.log.info("========== mb no of continue pop on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email1()
    #     self.pl.clk_continue_btn()
    #     time.sleep(2)
    #     self.pl.send_your_name()
    #     self.pl.send_your_email()
    #     self.pl.send_country_code()
    #     self.pl.send_mb_number()
    #     chk = self.pl.chk_refer_btn()
    #     if chk == True:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 82, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== mb no continue pop PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 82, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "mb no continue pop.png"))
    #         self.driver.close()
    #         self.log.info("========= mb no continue pop FAILED ==========")
    #         assert False
    #
    # def test_pl_79(self, setup):
    #     self.log.info("========== Click refer continue pop on refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email1()
    #     self.pl.clk_continue_btn()
    #     time.sleep(2)
    #     self.pl.send_your_name()
    #     self.pl.send_your_email()
    #     self.pl.send_country_code()
    #     self.pl.send_mb_number()
    #     self.pl.clk_refer_btn()
    #     time.sleep(2)
    #     chk = self.pl.chk_thanks_pop()
    #     if chk == True:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 83, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click refer continue pop PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 83, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click refer continue pop.png"))
    #         self.driver.close()
    #         self.log.info("=========Click refer continue pop FAILED ==========")
    #         assert False
    #
    # def test_pl_80(self, setup):
    #     self.log.info("========== Click close thanks pop refer_pop of refer_mnf of explore==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.hover_explore()
    #     self.pl.clk_refer_mnf()
    #     self.pl.scroll10()
    #     self.pl.clk_btn_refer_mnf()
    #     time.sleep(2)
    #     self.pl.send_email1()
    #     self.pl.clk_continue_btn()
    #     time.sleep(2)
    #     self.pl.send_your_name()
    #     self.pl.send_your_email()
    #     self.pl.send_country_code()
    #     self.pl.send_mb_number()
    #     self.pl.clk_refer_btn()
    #     time.sleep(2)
    #     self.pl.clk_cl_thanks_pop()
    #     chk = self.pl.chk_thanks_pop()
    #     if chk == True:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 84, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click close thanks pop continue pop PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 84, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click close thanks pop.png"))
    #         self.driver.close()
    #         self.log.info("=========Click close thanks pop continue pop FAILED ==========")
    #         assert False

    def test_pl_81(self, setup):
        self.log.info("========== Click Demo of promises==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        chk = self.pl.chk_demo()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 85, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Demo of promises PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 85, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Demo of promises.png"))
            self.driver.close()
            self.log.info("=========Click Demo of promises FAILED ==========")
            assert False

    def test_pl_82(self, setup):
        self.log.info("========== Click Subtitle Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll11()
        self.pl.clk_subtitle_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 86, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Subtitle Demo PASS ==========")

    def test_pl_83(self, setup):
        self.log.info("========== Click Script pad Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll12()
        self.pl.clk_script_pad_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 87, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Script pad Demo PASS ==========")

    def test_pl_84(self, setup):
        self.log.info("========== Click Project center Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll13()
        self.pl.clk_project_center_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 88, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Project center Demo PASS ==========")

    def test_pl_85(self, setup):
        self.log.info("========== Click Premises Pool Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll14()
        self.pl.clk_premises_pool_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 89, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Premises Pool Demo PASS ==========")

    def test_pl_86(self, setup):
        self.log.info("========== Click Harkat Club Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll14()
        self.pl.clk_harkat_club_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 90, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Harkat Club Demo PASS ==========")

    def test_pl_87(self, setup):
        self.log.info("========== Click Script audit Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll15()
        self.pl.clk_script_audit_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 91, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Script audit Demo PASS ==========")

    def test_pl_88(self, setup):
        self.log.info("========== Click PPT Conversion Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll16()
        self.pl.clk_ppt_conversion_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 92, 4, "pass")
        self.driver.close()
        self.log.info("========== Click PPT Conversion Demo PASS ==========")

    def test_pl_89(self, setup):
        self.log.info("========== Click Book Conversion Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        time.sleep(5)
        self.pl.scroll17()
        self.pl.clk_book_conversion_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 93, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Book Conversion Demo PASS ==========")

    def test_pl_90(self, setup):
        self.log.info("========== Click Vivewing Loung Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll18()
        self.pl.clk_ppt_viewing_loung_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 94, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Vivewing Loung Demo PASS ==========")

    def test_pl_91(self, setup):
        self.log.info("========== Click ScreenPlay Narration Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll19()
        self.pl.clk_screenplay_narration_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 95, 4, "pass")
        self.driver.close()
        self.log.info("========== Click ScreenPlay Narration Demo PASS ==========")

    def test_pl_92(self, setup):
        self.log.info("========== Click Corporate membership Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll20()
        self.pl.clk_corporate_membership_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 96, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Corporate membership Demo PASS ==========")

    def test_pl_93(self, setup):
        self.log.info("========== Click Pitchdeck Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll21()
        self.pl.clk_pitchdeck_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 97, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Pitchdeck Demo PASS ==========")

    def test_pl_94(self, setup):
        self.log.info("========== Click Institutional Membership Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll22()
        self.pl.clk_institutional_membership_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 98, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Institutional Membership Demo PASS ==========")
    def test_pl_95(self, setup):
        self.log.info("========== Click Language Pare Partneer Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll23()
        self.pl.clk_language_pare_partner_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 99, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Language Pare Partneer Demo PASS ==========")

    def test_pl_96(self, setup):
        self.log.info("========== Click Mesiah Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll25()
        self.pl.clk_messiah_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 100, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Mesiah Demo PASS ==========")

    def test_pl_97(self, setup):
        self.log.info("========== Click Student registration Demo==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_demo()
        self.pl.scroll26()
        self.pl.clk_student_registration_demo()
        time.sleep(2)
        assert True
        result = XLUtils.writeData(self.xl_path, "Prelogin", 101, 4, "pass")
        self.driver.close()
        self.log.info("========== Click Student registration Demo PASS ==========")

    def test_pl_98(self, setup):
        self.log.info("========== Click promises of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        time.sleep(2)
        self.pl.scroll31()
        self.pl.clk_promises_footer()
        chk = self.pl.chk_promises()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 102, 4, "pass")
            self.driver.close()
            self.log.info("==========Click promises of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 102, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click promises of footer.png"))
            self.driver.close()
            self.log.info("=========Click promises of footer FAILED ==========")
            assert False

    def test_pl_99(self, setup):
        self.log.info("========== Click premises pool of promises of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        time.sleep(2)
        self.pl.scroll31()
        self.pl.clk_premises_pool_footer()
        chk = self.pl.chk_premises_pool()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 103, 4, "pass")
            self.driver.close()
            self.log.info("==========Click promises of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 103, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click promises of footer.png"))
            self.driver.close()
            self.log.info("=========Click promises of footer FAILED ==========")
            assert False
    def test_pl_100(self, setup):
        self.log.info("========== Click script builder of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_script_builder_footer()
        time.sleep(5)
        chk = self.pl.chk_script_builder()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 104, 4, "pass")
            self.driver.close()
            self.log.info("==========Click script builder of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 104, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click script builder of footer.png"))
            self.driver.close()
            self.log.info("=========Click script builder of footer FAILED ==========")
            assert False

    def test_pl_101(self, setup):
        self.log.info("========== Click screenplay conversion of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_screenplay_conversion_footer()
        time.sleep(4)
        chk = self.pl.chk_screenplay_conversion()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 105, 4, "pass")
            self.driver.close()
            self.log.info("==========Click screenplay conversion of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 105, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click screenplay conversion of footer.png"))
            self.driver.close()
            self.log.info("=========Click screenplay conversion of footer FAILED ==========")
            assert False



    def test_pl_102(self, setup):
        self.log.info("========== Click pitchdech narration in footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_pitchdeck_creation_footer()
        chk = self.pl.chk_pitchdeck_creation()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 106, 4, "pass")
            self.driver.close()
            self.log.info("==========Click pitchdech narration in footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 106, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click pitchdech narration footer.png"))
            self.driver.close()
            self.log.info("=========Click pitchdech narration in footer FAILED ==========")
            assert False


    def test_pl_103(self, setup):
        self.log.info("========== Click screenplay narration in footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_screenplay_narration_footer()
        chk = self.pl.chk_screenplay_narration()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 107, 4, "pass")
            self.driver.close()
            self.log.info("==========Click screenplay narration footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 107, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click screenplay narration footer.png"))
            self.driver.close()
            self.log.info("=========Click screenplay narration footer FAILED ==========")
            assert False



    def test_pl_104(self, setup):
        self.log.info("========== Click harkat clubs in footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_harkat_clubs_footer()
        chk = self.pl.chk_harkat_clubs()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 108, 4, "pass")
            self.driver.close()
            self.log.info("==========Click harkat clubs in footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 108, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click harkat clubs footer.png"))
            self.driver.close()
            self.log.info("=========Click harkat clubs in footer FAILED ==========")
            assert False



    def test_pl_105(self, setup):
        self.log.info("========== Click project center in footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_project_center_footer()
        chk = self.pl.chk_project_center()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 109, 4, "pass")
            self.driver.close()
            self.log.info("==========Click project center footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 109, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click project center footer.png"))
            self.driver.close()
            self.log.info("=========Click project center footerFAILED ==========")
            assert False


    def test_pl_106(self, setup):
        self.log.info("========== Click subtitle hub in footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_subtitle_hub_footer()
        chk = self.pl.chk_subtitle_hub()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 110, 4, "pass")
            self.driver.close()
            self.log.info("==========Click subtitle  footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 110, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click subtitle hub footer.png"))
            self.driver.close()
            self.log.info("=========Click subtitle hub footer FAILED ==========")
            assert False


    def test_pl_107(self, setup):
        self.log.info("========== Click Viewing Lounge in footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_viewing_Lounge_footer()
        chk = self.pl.chk_Viewing_Lounge()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 111, 4, "pass")
            self.driver.close()
            self.log.info("==========Click Viewing  footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 111, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Viewing Lounge footer.png"))
            self.driver.close()
            self.log.info("=========Click Viewing Lounge footer FAILED ==========")
            assert False

    def test_pl_108(self, setup):
        self.log.info("========== Click Pricing of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        time.sleep(2)
        self.pl.scroll31()
        self.pl.clk_pricing_footer()
        chk = self.pl.chk_pricing()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 112, 4, "pass")
            self.driver.close()
            self.log.info("==========Click Pricing of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 112, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Pricing of footer.png"))
            self.driver.close()
            self.log.info("=========Click Pricing of footer FAILED ==========")
            assert False

    def test_pl_109(self, setup):
        self.log.info("========== Click free services of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_free_services_footer()
        chk = self.pl.chk_free_services()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 113, 4, "pass")
            self.driver.close()
            self.log.info("========== Click free services of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 113, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click free services of footer.png"))
            self.driver.close()
            self.log.info("========= Click free services of footer FAILED ==========")
            assert False

    def test_pl_110(self, setup):
        self.log.info("========== Click discounts of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_discounts_footer()
        chk = self.pl.chk_discounts()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 114, 4, "pass")
            self.driver.close()
            self.log.info("========== Click discounts of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 114, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click discounts of footer.png"))
            self.driver.close()
            self.log.info("========= Click discounts of footer FAILED ==========")
            assert False

    def test_pl_111(self, setup):
        self.log.info("========== Click  jug_pack_scr_writer of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_jug_pack_scr_writer_footer()
        chk = alert = self.driver.switch_to.alert
        alert.accept()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 115, 4, "pass")
            self.driver.close()
            self.log.info("========== Click jug_pack_scr_writer of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 115, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click jug_pack_scr_writer of footer.png"))
            self.driver.close()
            self.log.info("========= Click jug_pack_scr_writer of footer FAILED ==========")
            assert False

    def test_pl_112(self, setup):
        self.log.info("========== Click jug_pack_scr_house of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_jug_pack_prod_house_footer()
        chk = alert = self.driver.switch_to.alert
        alert.accept()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 116, 4, "pass")
            self.driver.close()
            self.log.info("========== Click jug_pack_scr_house of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 116, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click jug_pack_scr_house of footer.png"))
            self.driver.close()
            self.log.info("========= Click jug_pack_scr_house of footer FAILED ==========")
            assert False

    def test_pl_113(self, setup):
        self.log.info("========== Click subtitling of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_subtitle_hub_pricing_footer()
        chk = self.pl.chk_subtitling()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 117, 4, "pass")
            self.driver.close()
            self.log.info("========== Click subtitling of Pricing PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 117, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click subtitling of footer.png"))
            self.driver.close()
            self.log.info("========= Click subtitling of footer FAILED ==========")
            assert False

    def test_pl_114(self, setup):
        self.log.info("========== Click screenplay_con_pricin of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_screenplay_con_pricing_footer()
        chk = self.pl.chk_screenplay_con_pricing()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 118, 4, "pass")
            self.driver.close()
            self.log.info("========== Click screenplay_con_pricin of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 118, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click screenplay_con_pricin of footer.png"))
            self.driver.close()
            self.log.info("========= Click screenplay_con_pricin of footer FAILED ==========")
            assert False

    def test_pl_115(self, setup):
        self.log.info("========== Click scheduling_budjeting of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_scheduling_budjeting_footer()
        chk = self.pl.chk_scheduling_budjeting()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 119, 4, "pass")
            self.driver.close()
            self.log.info("========== Click scheduling_budjeting of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 119, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click scheduling_budjeting of footer.png"))
            self.driver.close()
            self.log.info("========= Click scheduling_budjeting of footer FAILED ==========")
            assert False

    def test_pl_116(self, setup):
        self.log.info("========== Click pitchdeck_creation of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_pitchdeck_creation_pricing_footer()
        chk = self.pl.chk_pitchdeck_creation_pricing()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 120, 4, "pass")
            self.driver.close()
            self.log.info("========== Click pitchdeck_creation of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 120, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click pitchdeck_creation of footer.png"))
            self.driver.close()
            self.log.info("========= Click pitchdeck_creation of footer FAILED ==========")
            assert False

    def test_pl_117(self, setup):
        self.log.info("========== Click screenplay narration of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_screenplay_narration_pricing_footer()
        chk = self.pl.chk_scrplay_narration_pricing()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 121, 4, "pass")
            self.driver.close()
            self.log.info("========== Click screenplay narration of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 121, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click screenplay narration of footer.png"))
            self.driver.close()
            self.log.info("========= Click screenplay narration of footer FAILED ==========")
            assert False

    def test_pl_118(self, setup):
        self.log.info("========== Click pricing_calculator of footer==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.scroll31()
        self.pl.clk_pricing_calculator_footer()
        chk = self.pl.chk_pricing_cal_img()
        if chk:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 122, 4, "pass")
            self.driver.close()
            self.log.info("========== Click pricing_calculator of footer PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 122, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", " Click pricing_calculator of footer.png"))
            self.driver.close()
            self.log.info("========= Click pricing_calculator of footer FAILED ==========")
            assert False

    # def test_pl_119(self, setup):
    #     self.log.info("========== Click Opportunities of footer==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.scroll31()
    #     self.pl.clk_opportunities_footer()
    #     chk = self.pl.chk_opportunities()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 123, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click Opportunities of footer PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 123, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click Opportunities of footer.png"))
    #         self.driver.close()
    #         self.log.info("========= Click pricing_calculator of footer FAILED ==========")
    #         assert False
    #
    # def test_pl_120(self, setup):
    #     self.log.info("========== Click refer_mnf of footer==========")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.advance(setup)
    #     self.pl = PreLogin(self.driver)
    #     self.pl.scroll31()
    #     self.pl.clk_refer_mnf_footer()
    #     chk = self.pl.chk_refer_mnf()
    #     if chk:
    #         assert True
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 124, 4, "pass")
    #         self.driver.close()
    #         self.log.info("========== Click refer_mnf of footer PASS ==========")
    #     else:
    #         result = XLUtils.writeData(self.xl_path, "Prelogin", 124, 4, "fail")
    #         self.driver.save_screenshot(get_path("Screenshots", "Click refer_mnf footer.png"))
    #         self.driver.close()
    #         self.log.info("========= Click refer_mnf of footerFAILED ==========")
    #         assert False

    def test_pl_121(self, setup):
        self.log.info("========== CHECK pricing_calculator_pop_close of Pricing of explore==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.hover_explore()
        self.pl.clk_pricing()
        self.pl.clk_pricing_calculator_img()
        self.pl.send_no_pages()
        time.sleep(2)
        self.pl.clk_without_lpp()
        time.sleep(10)
        a = self.pl.get_calculations()
        print(a)
        total_price_text = self.pl.get_total_price()
        numeric_value = re.sub(r'[^\d.]', '', total_price_text)
        print(numeric_value)
        if a == numeric_value:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 125, 4, "pass")
            self.driver.close()
            self.log.info("========== CHECK pricing_calculator_pop_close of Pricing of explore PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 125, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "CHECK pricing_calculator_pop_close of Pricing of explore.png"))
            self.driver.close()
            self.log.info("=========CHECK pricing_calculator_pop_close of Pricing of explore FAILED ==========")
            assert False

    def test_pl_122(self, setup):
        self.log.info("========== Click Idea mildstone show pop up ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_idea()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        chk = self.pl.chk_login_regi_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 126, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Idea mildstone show pop up PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 126, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Idea mildstone show pop up.png"))
            self.driver.close()
            self.log.info("=========Click Idea mildstone show pop up FAILED ==========")
            assert False

    def test_pl_123(self, setup):
        self.log.info("========== Idea mildstone click Registraton ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_idea()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_registration()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_123")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 127, 4, "pass")
            self.driver.close()
            self.log.info("========== Idea mildstone click Registraton PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 127, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Idea mildstone click Registraton.png"))
            self.driver.close()
            self.log.info("=========Idea mildstone click Registraton FAILED ==========")
            assert False

    def test_pl_124(self, setup):
        self.log.info("========== Idea mildstone click Login ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_idea()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_login()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_124")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 128, 4, "pass")
            self.driver.close()
            self.log.info("========== Idea mildstone click Login PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 128, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Idea mildstone click Login.png"))
            self.driver.close()
            self.log.info("=========Idea mildstone click Login FAILED ==========")
            assert False

    def test_pl_125(self, setup):
        self.log.info("========== Click Script mildstone show pop up ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_script()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        chk = self.pl.chk_login_regi_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 129, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Script mildstone show pop up PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 129, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Script mildstone show pop up.png"))
            self.driver.close()
            self.log.info("=========Click Script mildstone show pop up FAILED ==========")
            assert False

    def test_pl_126(self, setup):
        self.log.info("========== Script mildstone click Registraton ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_script()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_registration()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_126")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 130, 4, "pass")
            self.driver.close()
            self.log.info("========== Script mildstone click Registraton PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 130, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Script mildstone click Registraton.png"))
            self.driver.close()
            self.log.info("=========Script mildstone click Registraton FAILED ==========")
            assert False

    def test_pl_127(self, setup):
        self.log.info("========== Script mildstone click Login ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_script()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_login()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_127")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 131, 4, "pass")
            self.driver.close()
            self.log.info("========== Script mildstone click Login PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 131, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Script mildstone click Login.png"))
            self.driver.close()
            self.log.info("=========Script mildstone click Login FAILED ==========")
            assert False

    def test_pl_128(self, setup):
        self.log.info("========== Click Translate mildstone show pop up ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_translate()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        chk = self.pl.chk_login_regi_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 132, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Translate mildstone show pop up PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 132, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Translate mildstone show pop up.png"))
            self.driver.close()
            self.log.info("=========Click Translate mildstone show pop up FAILED ==========")
            assert False

    def test_pl_129(self, setup):
        self.log.info("========== Translate mildstone click Registraton ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_translate()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_registration()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_129")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 133, 4, "pass")
            self.driver.close()
            self.log.info("========== Translate mildstone click Registraton PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 133, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Translate mildstone click Registraton.png"))
            self.driver.close()
            self.log.info("=========Translate mildstone click Registraton FAILED ==========")
            assert False

    def test_pl_130(self, setup):
        self.log.info("========== Translate mildstone click Login ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_translate()
        self.pl.clk_script_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_login()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_130")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 134, 4, "pass")
            self.driver.close()
            self.log.info("========== Translate mildstone click Login PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 134, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Translate mildstone click Login.png"))
            self.driver.close()
            self.log.info("=========Translate mildstone click Login FAILED ==========")
            assert False

    def test_pl_131(self, setup):
        self.log.info("========== Click Narrate mildstone show pop up ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_narrate()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        chk = self.pl.chk_login_regi_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 135, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Narrate mildstone show pop up PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 135, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Narrate mildstone show pop up.png"))
            self.driver.close()
            self.log.info("=========Click Narrate mildstone show pop up FAILED ==========")
            assert False

    def test_pl_132(self, setup):
        self.log.info("========== Narrate mildstone click Registraton ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_narrate()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_registration()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_132")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 136, 4, "pass")
            self.driver.close()
            self.log.info("========== Narrate mildstone click Registraton PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 136, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Narrate mildstone click Registraton.png"))
            self.driver.close()
            self.log.info("=========Narrate mildstone click Registraton FAILED ==========")
            assert False

    def test_pl_133(self, setup):
        self.log.info("========== Translate Narrate click Login ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_narrate()
        self.pl.clk_script_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_login()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_133")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 137, 4, "pass")
            self.driver.close()
            self.log.info("========== Narrate mildstone click Login PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 137, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Narrate mildstone click Login.png"))
            self.driver.close()
            self.log.info("=========Narrate mildstone click Login FAILED ==========")
            assert False

    def test_pl_134(self, setup):
        self.log.info("========== Click Build Team mildstone show pop up ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_buildTeam()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        chk = self.pl.chk_login_regi_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 138, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Build Team mildstone show pop up PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 138, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Build Team mildstone show pop up.png"))
            self.driver.close()
            self.log.info("=========Click Build Team mildstone show pop up FAILED ==========")
            assert False

    def test_pl_135(self, setup):
        self.log.info("========== Build Team mildstone click Registraton ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_buildTeam()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_registration()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_135")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 139, 4, "pass")
            self.driver.close()
            self.log.info("========== Build Team mildstone click Registraton PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 139, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Build Team mildstone click Registraton.png"))
            self.driver.close()
            self.log.info("=========Build Team mildstone click Registraton FAILED ==========")
            assert False

    def test_pl_136(self, setup):
        self.log.info("========== Build Team Narrate click Login ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_buildTeam()
        self.pl.clk_script_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_login()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_136")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 140, 4, "pass")
            self.driver.close()
            self.log.info("========== Build Team mildstone click Login PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 140, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Build Team mildstone click Login.png"))
            self.driver.close()
            self.log.info("=========Build Team mildstone click Login FAILED ==========")
            assert False

    def test_pl_137(self, setup):
        self.log.info("========== Click Produce mildstone show pop up ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_produce()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        chk = self.pl.chk_login_regi_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 141, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Produce mildstone show pop up PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 141, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Produce mildstone show pop up.png"))
            self.driver.close()
            self.log.info("=========Click Produce mildstone show pop up FAILED ==========")
            assert False

    def test_pl_138(self, setup):
        self.log.info("========== Produce mildstone click Registraton ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_produce()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_registration()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_138")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 142, 4, "pass")
            self.driver.close()
            self.log.info("========== Produce mildstone click Registraton PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 142, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Produce mildstone click Registraton.png"))
            self.driver.close()
            self.log.info("=========Produce mildstone click Registraton FAILED ==========")
            assert False

    def test_pl_139(self, setup):
        self.log.info("========== Produce Narrate click Login ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_produce()
        self.pl.clk_script_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_login()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_139")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 143, 4, "pass")
            self.driver.close()
            self.log.info("========== Produce mildstone click Login PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 143, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Produce mildstone click Login.png"))
            self.driver.close()
            self.log.info("=========Produce mildstone click Login FAILED ==========")
            assert False

    def test_pl_140(self, setup):
        self.log.info("========== Click Subtitle mildstone show pop up ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_subtitle()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        chk = self.pl.chk_login_regi_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 144, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Subtitle mildstone show pop up PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 144, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Subtitle mildstone show pop up.png"))
            self.driver.close()
            self.log.info("=========Click Subtitle mildstone show pop up FAILED ==========")
            assert False

    def test_pl_141(self, setup):
        self.log.info("========== Subtitle mildstone click Registraton ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_subtitle()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_registration()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_141")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 145, 4, "pass")
            self.driver.close()
            self.log.info("========== Subtitle mildstone click Registraton PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 145, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Subtitle mildstone click Registraton.png"))
            self.driver.close()
            self.log.info("=========Subtitle mildstone click Registraton FAILED ==========")
            assert False

    def test_pl_142(self, setup):
        self.log.info("========== Subtitle Narrate click Login ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_subtitle()
        self.pl.clk_script_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_login()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_142")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 146, 4, "pass")
            self.driver.close()
            self.log.info("========== Subtitle mildstone click Login PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 146, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Subtitle mildstone click Login.png"))
            self.driver.close()
            self.log.info("=========Subtitle mildstone click Login FAILED ==========")
            assert False

    def test_pl_143(self, setup):
        self.log.info("========== Click Exhibit mildstone show pop up ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_exhibit()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        chk = self.pl.chk_login_regi_pop()
        if chk == True:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 147, 4, "pass")
            self.driver.close()
            self.log.info("========== Click Exhibit mildstone show pop up PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 147, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Click Exhibit mildstone show pop up.png"))
            self.driver.close()
            self.log.info("=========Click Exhibit mildstone show pop up FAILED ==========")
            assert False

    def test_pl_144(self, setup):
        self.log.info("========== Exhibit mildstone click Registraton ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_exhibit()
        self.pl.clk_idea_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_registration()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_144")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 148, 4, "pass")
            self.driver.close()
            self.log.info("========== Exhibit mildstone click Registraton PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 148, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Exhibit mildstone click Registraton.png"))
            self.driver.close()
            self.log.info("=========Exhibit mildstone click Registraton FAILED ==========")
            assert False

    def test_pl_145(self, setup):
        self.log.info("========== Exhibit Narrate click Login ==========")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.reload(setup)
        self.advance(setup)
        self.pl = PreLogin(self.driver)
        self.pl.clk_exhibit()
        self.pl.clk_script_mildstone()
        time.sleep(1)
        self.pl.clk_mildstone_login()
        actual_title = self.driver.current_url
        print(actual_title)
        expected_title = XLUtils.readExpData(self.xl_path, "Prelogin", "test_pl_145")
        print(expected_title)
        if actual_title == expected_title:
            assert True
            result = XLUtils.writeData(self.xl_path, "Prelogin", 149, 4, "pass")
            self.driver.close()
            self.log.info("========== Exhibit mildstone click Login PASS ==========")
        else:
            result = XLUtils.writeData(self.xl_path, "Prelogin", 149, 4, "fail")
            self.driver.save_screenshot(get_path("Screenshots", "Exhibit mildstone click Login.png"))
            self.driver.close()
            self.log.info("=========Exhibit mildstone click Login FAILED ==========")
            assert False
