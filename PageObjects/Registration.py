from faker import Faker
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Utilities.commonMethods import CustomWait
from selenium.webdriver.support.color import Color



class Register:

    def __init__(self, driver):
        self.driver = driver
        self.cusMethod = CustomWait(self.driver)
        self.wafe = self.cusMethod.wait_for_element

 # ****************************************** LOCATERS **********************************************

    log_in = (By.XPATH, '//*[@id="Login_btn"]')

    log_in_dp = (By.XPATH, '//*[@id="LoginDropDown"]')

    personal = (By.XPATH, '//*[@id="LoginDropDown"]/li[1]')

    personal_login = (By.XPATH, '//*[@id="LoginDropDown"]/li[1]/span/a[2]')

    back = (By.XPATH, '/html/body/div/a/button')

    personal_register = (By.XPATH, '//*[@id="LoginDropDown"]/li[1]/span/a[1]')

    register = (By.XPATH, '//*[@id="registerButton"]')

    error_msg = (By.XPATH, '//*[@id="errorText"]')

    error_msg0 = (By.XPATH, '//*[@id="errorTextEmail"]')

    error_msg1 = (By.XPATH, '//*[@id="errorTextPass"]')

    verify_msg = (By.XPATH, '//*[@id="popup"]')

    go_to_email = (By.XPATH, '//*[@id="popup"]/button[2]')

    cl_go_to_email = (By.XPATH, '//*[@id="popup"]/button[1]')

    go_to_email_pop = (By.XPATH, '//*[@id="popup"]')

    ch_sign_in_email = (By.XPATH, '//*[@id="headingText"]')

    login = (By.XPATH, '//*[@id="LoginButton"]')

    email = (By.XPATH, '//*[@id="email"]')

    password = (By.XPATH, '//*[@id="password"]')

    confirm_pwd = (By.XPATH, '//*[@id="confirm-password"]')

    eye_pwd = (By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[3]/div[2]/i')

    eye_confirm_pwd = (By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[6]/div[2]/i')

    small_ch = (By.XPATH, '//*[@id="small"]')

    capital_ch = (By.XPATH, '//*[@id="capital"]')

    digit_ch = (By.XPATH, '//*[@id="digit"]')
# ****************************************** Functions *************************************************
    def clk_log_in(self):
        ele = self.wafe(self.log_in)
        ele.click()

    def chk_login_dropdown_menu(self):
        try:
            ele = self.wafe(self.log_in_dp)
            return ele.is_displayed()
        except:
            return False

    def hover_personal(self):
        ele = self.wafe(self.personal)
        actions = ActionChains(self.driver)
        actions.move_to_element(ele).perform()

    def get_css_personal(self):
        css_cs = self.wafe(self.personal)
        text_color_before_hover = css_cs.value_of_css_property("color")
        hex_value = Color.from_string(text_color_before_hover).hex
        return hex_value

    def clk_per_register(self):
        ele = self.wafe(self.personal_register)
        ele.click()

    def clk_back(self):
        ele = self.wafe(self.back)
        ele.click()

    def clk_register(self):
        ele = self.wafe(self.register)
        ele.click()

    def chk_error_msg(self):
        try:
            ele = self.wafe(self.error_msg)
            return ele.is_displayed()
        except:
            return False

    def get_error_msg(self):
        ele = self.wafe(self.error_msg)
        return ele.text

    def get_error_msg0(self):
        ele = self.wafe(self.error_msg0)
        return ele.text
    def get_error_msg1(self):
        ele = self.wafe(self.error_msg1)
        return ele.text

    def get_verify_msg(self):
        ele = self.wafe(self.verify_msg)
        return ele.text

    def clk_go_to_email(self):
        ele = self.wafe(self.go_to_email)
        ele.click()

    def clk_close_go_to_email(self):
        ele = self.wafe(self.cl_go_to_email)
        ele.click()

    def chk_go_to_email_pop(self):
        try:
            ele = self.wafe(self.go_to_email_pop)
            return ele.is_displayed()
        except:
            return False

    def chk_sign_in_go_to_email(self):
        try:
            ele = self.wafe(self.ch_sign_in_email)
            return ele.is_displayed()
        except:
            return False

    def clk_login_button(self):
        ele = self.wafe(self.login)
        ele.click()

    def send_email(self):
        fake = Faker()
        fake_email = fake.email()
        ele = self.wafe(self.email)
        return ele.send_keys(fake_email)

    def send_password(self):
        ele = self.wafe(self.password)
        return ele.send_keys("Amruta@3")

    def send_confirm_password(self):
        ele = self.wafe(self.confirm_pwd)
        return ele.send_keys("Amruta@3")

    def send_Existed_email(self):
        ele = self.wafe(self.email)
        return ele.send_keys("amruta3017@gmail.com")

    def send_invalid_email(self):
        ele = self.wafe(self.email)
        return ele.send_keys("amruta3017gmail.com")

    def chk_eye_icon_password(self):
        ele = self.wafe(self.password)
        return ele.get_attribute("type")
    def clk_eye_icon_password(self):
        ele = self.wafe(self.eye_pwd)
        ele.click()

    def clk_eye_icon_confirm_pwd(self):
        ele = self.wafe(self.eye_confirm_pwd)
        actions = ActionChains(self.driver)
        actions.move_to_element(ele).perform()

    def chk_eye_icon_confirm_pwd(self):
        ele = self.wafe(self.confirm_pwd)
        print(ele.get_attribute("type"))
        return ele.get_attribute("type")

    def send_password1(self, text):
        ele = self.wafe(self.password)
        return ele.send_keys(text)

    def get_css_small_ch_box(self):
        css_cs = self.wafe(self.small_ch)
        text_color_before_hover = css_cs.value_of_css_property("color")
        hex_value = Color.from_string(text_color_before_hover).hex
        return hex_value

    def get_css_capital_ch_box(self):
        css_cs = self.wafe(self.small_ch)
        text_color_before_hover = css_cs.value_of_css_property("color")
        hex_value = Color.from_string(text_color_before_hover).hex
        return hex_value

    def get_css_digit_ch_box(self):
        css_cs = self.wafe(self.small_ch)
        text_color_before_hover = css_cs.value_of_css_property("color")
        hex_value = Color.from_string(text_color_before_hover).hex
        return hex_value

    def send_password2(self):
        ele = self.wafe(self.password)
        return ele.send_keys("Amruta")

    def send_confirm_password2(self):
        ele = self.wafe(self.confirm_pwd)
        return ele.send_keys("Amruta")

    def send_password3(self):
        ele = self.wafe(self.password)
        return ele.send_keys("AMRUTA1")

    def send_confirm_password3(self):
        ele = self.wafe(self.confirm_pwd)
        return ele.send_keys("AMRUTA1")

    def send_password4(self):
        ele = self.wafe(self.password)
        return ele.send_keys("amruta1")

    def send_confirm_password4(self):
        ele = self.wafe(self.confirm_pwd)
        return ele.send_keys("amruta1")
