from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Utilities.commonMethods import CustomWait
from selenium.webdriver.support.color import Color



class Login:

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

    register =(By.XPATH, '//*[@id="forgotButton"]')

    per_login_btn = (By.XPATH, '//*[@id="login_button"]')

    error_msg = (By.XPATH, '//*[@id="login_button"]')

    email = (By.XPATH, '//*[@id="email_input"]')

    password = (By.XPATH, '//*[@id="passwordLogin"]')

    eye_icon = (By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/div[2]/i')

    forget_password = (By.XPATH, '//*[@id="forgotbuttonStyle"]')

    ch_forget_pwd = (By.XPATH, '//*[@id="contentBlockENterMail"]/div/div/h2')

    forget_pwd_next = (By.XPATH, '//*[@id="nextButton"]')

    forget_pwd_next_error_msg = (By.XPATH, '//*[@id="errorTextEmail"]')

    forget_pwd_email = (By.XPATH, '//*[@id="email_input"]')

    forget_pwd_code = (By.XPATH, '//*[@id="fourDigit"]')

    check_forget_email = (By.XPATH, '//*[@id="displayEmail"]')

    code = (By.XPATH, '//*[@id="fourDigit"]')

    forget_error_msg = (By.XPATH, '//*[@id="errorTextPass"]')

    forget_next = (By.XPATH, '//*[@id="nextResetButton"]')

    reset_pwd = (By.XPATH, "//input[@id='password']")

    reverse_cnt = (By.XPATH, '//*[@id="reverse_countdown"]')

    resend_btn = (By.XPATH, '//*[@id="forgotButton"]')

    con_reset_pwd = (By.XPATH, '//*[@id="confirm-password"]')
    change_reset_pwd = (By.XPATH, '//*[@id="Change_password_button"]')
    small = (By.XPATH, '//*[@id="second_popup"]/div[2]/div[2]/div[1]')
    capital = (By.XPATH, '//*[@id="second_popup"]/div[2]/div[2]/div[2]')
    digit = (By.XPATH, '//*[@id="second_popup"]/div[2]/div[2]/div[3]')
    error = (By.XPATH, '//*[@id="errorText"]')
    reset_pwd_eye = (By.XPATH, '//*[@id="second_popup"]/div[1]/div[2]/i')
    con_reset_pwd_eye = (By.XPATH, '//*[@id="second_popup"]/div[4]/div[2]/i')

    small_ch = (By.XPATH, '//*[@id="small"]')

    capital_ch = (By.XPATH, '//*[@id="capital"]')

    digit_ch = (By.XPATH, '//*[@id="digit"]')

 # ***************************************** FUNCTIONS ******************************************

    def clk_log_in(self):
          ele =self.wafe(self.log_in)
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

    def clk_personal_login(self):
          ele =self.wafe(self.personal_login)
          ele.click()

    def clk_back(self):
        ele = self.wafe(self.back)
        ele.click()

    def clk_register(self):
        ele = self.wafe(self.register)
        ele.click()

    def clk_per_login_btn(self):
        ele = self.wafe(self.per_login_btn)
        ele.click()

    def chk_error_msg(self):
        try:
            ele = self.wafe(self.error_msg)
            return ele.is_displayed()
        except:
            return False

    def send_email(self):
        ele = self.wafe(self.email)
        return ele.send_keys("amruta3017@gmail.com")

    def send_email1(self):
        ele = self.wafe(self.email)
        return ele.send_keys("moniurzzaman25@.com")

    def send_password(self):
        ele = self.wafe(self.password)
        return ele.send_keys("Amruta@30")

    def send_password1(self):
        ele = self.wafe(self.password)
        return ele.send_keys("Amruta30")

    def get_password(self):
        ele = self.wafe(self.password)
        return ele.get_attribute("type")

    def clk_eye_icon(self):
        ele = self.wafe(self.eye_icon)
        ele.click()

    def clk_forget_password(self):
        ele = self.wafe(self.forget_password)
        ele.click()

    def chk_forget_password(self):
        try:
            ele = self.wafe(self.ch_forget_pwd)
            return ele.is_displayed()
        except:
            return False

    def clk_forget_password_next(self):
        ele = self.wafe(self.forget_pwd_next)
        ele.click()

    def chk_forget_pwd_next_error_msg(self):
        try:
            ele = self.wafe(self.forget_pwd_next_error_msg)
            return ele.is_displayed()
        except:
            return False

    def send_forget_pwd_email1(self):
        ele = self.wafe(self.forget_pwd_email)
        return ele.send_keys("moniurzzaman25@.com")

    def send_forget_pwd_email(self):
        ele = self.wafe(self.forget_pwd_email)
        return ele.send_keys("amruta3017@gmail.com")

    def chk_forget_pwd_code(self):
        try:
            ele = self.wafe(self.forget_pwd_code)
            return ele.is_displayed()
        except:
            return False

    def get_forget_pwd_email(self):
        ele = self.wafe(self.forget_pwd_email)
        return ele.get_attribute("value")

    def check_email_forget_pwd(self):
        ele = self.wafe(self.check_forget_email)
        line = ele.text
        return line

    def send_forget_code(self):
        ele = self.wafe(self.code)
        return ele.send_keys("1234")
    def send_forget_code1(self):
        ele = self.wafe(self.code)
        return ele.send_keys("123")

    def clk_next(self):
        ele = self.wafe(self.forget_next)
        ele.click()

    def chk_reverse_counter(self):
        ele = self.wafe(self.reverse_cnt)
        line = ele.text
        return line
    def chk_forget_pwd_error_msg(self):
        try:
            ele = self.wafe(self.forget_error_msg)
            return ele.is_displayed()
        except:
            return False

    def clk_resend(self):
        ele = self.wafe(self.resend_btn)
        return ele.is_enabled()

    def send_reset_pwd(self):
        ele = self.wafe(self.reset_pwd)
        return ele.send_keys("Amruta@3")
    def clr_send_reset_pwd(self):
        ele = self.wafe(self.reset_pwd)
        return ele.clear()

    def clr_send_reset_con_pwd(self):
        ele = self.wafe(self.con_reset_pwd)
        return ele.clear()

    def send_confirm_reset_pwd(self):
        ele = self.wafe(self.con_reset_pwd)
        return ele.send_keys("Amruta@3")

    def clk_change_reset_pwd(self):
        ele = self.wafe(self.change_reset_pwd)
        ele.click()

    def chk_reset_error_msg(self):
        ele = self.wafe(self.error)
        return ele.text

    def clk_eye_icon_password(self):
        ele = self.wafe(self.reset_pwd_eye)
        ele.click()

    def chk_eye_icon_password(self):
        ele = self.wafe(self.reset_pwd)
        return ele.get_attribute("type")

    def clk_eye_icon_con_password(self):
        ele = self.wafe(self.con_reset_pwd_eye)
        ele.click()

    def chk_eye_icon_con_password(self):
        ele = self.wafe(self.con_reset_pwd)
        return ele.get_attribute("type")

    def send_password11(self, text):
        ele = self.wafe(self.reset_pwd)
        return ele.send_keys(text)
    def clk_change_reset_pwd11(self, text):
        ele = self.wafe(self.con_reset_pwd)
        return ele.send_keys(text)
    def get_css_small_ch_box(self):
        css_cs = self.wafe(self.small_ch)
        text_color_before_hover = css_cs.value_of_css_property("background-color")
        hex_value = Color.from_string(text_color_before_hover).hex
        return hex_value

    def get_css_capital_ch_box(self):
        css_cs = self.wafe(self.small_ch)
        text_color_before_hover = css_cs.value_of_css_property("background-color")
        hex_value = Color.from_string(text_color_before_hover).hex
        return hex_value

    def get_css_digit_ch_box(self):
        css_cs = self.wafe(self.small_ch)
        text_color_before_hover = css_cs.value_of_css_property("background-color")
        hex_value = Color.from_string(text_color_before_hover).hex
        return hex_value


