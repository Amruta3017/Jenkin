from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Utilities.commonMethods import CustomWait
from faker import Faker
from selenium.webdriver.support.select import Select


class PreLogin:

    def __init__(self, driver):
        self.driver = driver
        self.cusMethod = CustomWait(self.driver)
        self.wafe = self.cusMethod.wait_for_element

 # ****************************************** LOCATERS **********************************************

    idea = (By.XPATH, '/html/body/main/section[1]/div/div/section/div/div/a[2]')

    script = (By.XPATH, '/html/body/main/section[1]/div/div/section/div/div/a[3]')

    translate = (By.XPATH, '/html/body/main/section[1]/div/div/section/div/div/a[4]')

    narrate = (By.XPATH, '/html/body/main/section[1]/div/div/section/div/div/a[5]')

    buildTeam = (By.XPATH, '/html/body/main/section[1]/div/div/section/div/div/a[6]')

    produce = (By.XPATH, '/html/body/main/section[1]/div/div/section/div/div/a[7]')

    subtitle = (By.XPATH, '/html/body/main/section[1]/div/div/section/div/div/a[8]')

    exhibit = (By.XPATH, '/html/body/main/section[1]/div/div/section/div/div/a[9]')

    facebook = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div/span[2]/a/img')

    email_id = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/p[2]')

    instagram = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div/span[1]/a/img')

    twter = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div/span[3]/a/img')

    youtube = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div/span[4]/a/img')

    linked_in = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div/span[5]/a/img')

    #imdb = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div/span[6]/a/img')

    threads = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div/span[6]/a/img')

    pinterest = (By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div/span[7]/a/img')

    explore = (By.ID, 'Exploremore')

    promises = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/div[1]/a')

    dp_menu = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div')

    ch_promises = (By.XPATH, "//h2[@class='c-green']")

    premises_pool = (By.XPATH, "//a[@class='dropdown-item_custom_style'][normalize-space()='Premise Pool']")

    ch_premises_pool = (By.XPATH, "//div[@id='premise-pool-body-bookmark']//h2[@class='main-color']")

    sd_premises_pool = (By.ID, 'premise-speaker')

    hd_premises_pool = (By.XPATH, "//img[@class='premise-static-text premise-hand-1']")

    script_builder = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/ul/li[2]/a')

    ch_script_builder = (By.XPATH, "//h2[normalize-space()='Script Builder']")

    sd_script_builder = (By.XPATH, "//img[@id='scriptbuilder-speaker']")

    hd_script_builder = (By.XPATH, "//img[@class='scriptbuilder-static-text scriptbuilder-hand-1']")

    screenplay_conversion = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/ul/li[3]/a')

    ch_screenplay_conversion = (By.XPATH, "//h2[normalize-space()='Script Builder']")

    sd_screenplay_conversion = (By.XPATH, '//*[@id="conversion-speaker"]')

    hd_screenplay_conversion = (By.XPATH, "//img[@class='conversion-static-text conversion-hand-1']")

    pitchdeck_creation = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/ul/li[4]/a')

    ch_pitchdeck_creation = (By.XPATH, '//*[@id="pitchdeck-body-bookmark"]/div[1]/div/div[2]/h2')

    sd_pitchdeck_creation = (By.XPATH, '//*[@id="pitchdeck-speaker"]')

    hd_pitchdeck_creation = (By.XPATH, '//*[@id="pitchdeck-body-bookmark"]/div[2]/div/div[2]/div/p[1]/img')

    screenplay_narration = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/ul/li[5]/a')

    ch_screenplay_narration = (By.XPATH, '//*[@id="narration-body-bookmark"]/div[1]/div/div[1]/h2')

    sd_screenplay_narration = (By.XPATH, '//*[@id="narration-speaker"]')

    hd_screenplay_narration = (By.XPATH, '//*[@id="narration-body-bookmark"]/div[2]/div/div[2]/div/p[1]/img')

    harkat_clubs = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/ul/li[6]/a')

    ch_harkat_clubs = (By.XPATH, '//*[@id="harkat-body-bookmark"]/div[1]/div/div[2]/h2')

    sd_harkat_clubs = (By.XPATH, '//*[@id="harkat-speaker"]')

    hd_harkat_clubs = (By.XPATH, '//*[@id="harkat-body-bookmark"]/div[2]/div/div[2]/div/p[1]/img')

    project_center = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/ul/li[7]/a')

    ch_project_center = (By.XPATH, '//*[@id="project-center-body-bookmark"]/div[1]/div/h2')

    sd_project_center = (By.XPATH, '//*[@id="projectcenter-speaker"]')

    hd_project_center = (By.XPATH, '//*[@id="project-center-body-bookmark"]/div[2]/div/div[2]/div/p[1]/img')

    subtitle_hub = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/ul/li[8]/a')

    ch_subtitle_hub = (By.XPATH, '//*[@id="subtitle-hub-body-bookmark"]/div[1]/div/div[2]/h2')

    sd_subtitle_hub = (By.XPATH, '//*[@id="subtitlehub-speaker"]')

    hd_subtitle_hub = (By.XPATH, '//*[@id="subtitle-hub-body-bookmark"]/div[2]/div/div[2]/div/p[1]/img')

    Viewing_Lounge = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/ul/li[9]/a')

    ch_Viewing_Lounge = (By.XPATH, '//*[@id="viewing-lounge-body-bookmark"]/div[1]/div/div[1]/h2')

    sd_Viewing_Lounge = (By.XPATH, '//*[@id="viewinglounge-speaker"]')

    hd_Viewing_Lounge = (By.XPATH, '//*[@id="viewing-lounge-body-bookmark"]/div[2]/div/div[2]/div/p[1]/img')

    idea1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[1]/div[1]/img')

    script1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[2]/div[1]/img')

    translate1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[3]/div[1]/img')

    pitchdack1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[4]/div[1]/img')

    narrate1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[5]/div[1]/img')

    build_team1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[6]/div[1]/img')

    produce1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[7]/div[1]/img')

    subtitle1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[8]/div[1]/img')

    exhibit1 = (By.XPATH, '/html/body/main/main/section[2]/div[2]/div/div[9]/div[1]/img')


    # ******************************** pRICING *********************************************************

    pricing = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/div/a')

    ch_pricing = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/section[2]/div[1]/h2')

    free_services = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[1]/a')

    ch_free_services = (By.XPATH, '//*[@id="free-services-body-bookmark"]/div[1]/div/div[1]/h2')

    discounts = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[2]/a')

    ch_discounts = (By.XPATH, '//*[@id="discounts-body-bookmark"]/div[1]/div/div[2]/h2')

    jug_pack_scr_writer = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[3]/a')

    #ch_jug_pack_scr_writer =(By.XPATH, '')

    jug_pack_prod_house = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[4]/a')

    # ch_jug_pack_scr_house =(By.XPATH, '')

    subtitling = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[5]/a')

    ch_subtitling = (By.XPATH, '//*[@id="subtitling-body-bookmark"]/div[1]/div/div[1]/h2')

    screenplay_con_pricing = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[6]/a')

    ch_screenplay_con_pricing = (By.XPATH, '//*[@id="p-screenplay-conversion-body-bookmark"]/div[1]/div/div[2]/h2')

    scheduling_budjeting = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[7]/a')

    ch_scheduling_budjeting = (By.XPATH, '//*[@id="scheduling-budgeting-body-bookmark"]/div[1]/div/div[1]/h2')

    pitchdeck_creation_pricing = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[8]/a')

    ch_pitchdeck_creation_pricing = (By.XPATH, '//*[@id="p-pitchdeck-body-bookmark"]/div[1]/div/div[2]/h2')

    scrplay_narration_pricing = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[9]/a')

    ch_scrplay_narration_pricing = (By.XPATH, '//*[@id="p-screenplay narration-body-bookmark"]/div[1]/div/div[1]/h2')

    pricing_calculator = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[2]/ul/li[10]/a')

    ch_pricing_cal_img = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/section[2]/div[2]/div/div[3]/div[1]/img')

    jug_pack_scr_writer_img = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/section[2]/div[2]/div/div[1]/div[1]/img')

    jug_pack_prod_house_img = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/section[2]/div[2]/div/div[2]/div[1]/img')

    pricing_calculator_img = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/section[2]/div[2]/div/div[3]/div[1]/img')

    ch_pricing_calculator_pop = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/div[1]/div')

    cl_pricing_calculator_pop = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/div[1]/i')

    # ***************************************** Opportunities *****************************

    opportunities = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[3]/div/a')

    ch_opportunities = (By.XPATH, '/html/body/main/main/section[2]/div/h2')

    refer_mnf = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[3]/ul/li[1]/a')

    ch_refer_mnf = (By.XPATH, '//*[@id="Refer-MNF-body-bookmark"]/div[1]/div/div[1]/h2')

    sd_refer_mnf = (By.XPATH, '//*[@id="refer-speaker"]')

    hd_refer_mnf = (By.XPATH, '//*[@id="Refer-MNF-body-bookmark"]/div[2]/div/div[2]/div/p[1]/img')

    btn_refer_mnf = (By.XPATH, '//*[@id="Refer-MNF-body-bookmark"]/div[2]/div/div[2]/button')

    refer_mnf_pop = (By.XPATH, '//*[@id="exampleModalLabel"]')

    cl_refer_mnf_pop = (By.XPATH, "//div[@class='custom-elementcrossbutton']//button[@aria-label='Close'][normalize-space()='X']")

    email_tb1 = (By.XPATH, "//input[@placeholder='Enter Friend Email']")

    email_tb2 = (By.XPATH, '//*[@id="divTxt"]/p[2]/input')

    same_email_error = (By.XPATH, '//*[@id="refer-error"]')

    email_tb3 = (By.XPATH, '//*[@id="divTxt"]/p[3]/input')

    email_tb4 = (By.XPATH, '//*[@id="divTxt"]/p[4]/input')

    email_tb5 = (By.XPATH, '//*[@id="divTxt"]/p[5]/input')

    max_5 = (By.XPATH, '//*[@id="refer-error"]')

    btn_continue = (By.XPATH, '//*[@id="buttonReferid"]')

    add_another = (By.XPATH, '//*[@id="addAnotherEmail"]')

    btn_cl =(By.XPATH, '//*[@id="exampleModal"]/div/div/div[1]/button[1]')

    continue_pop = (By.XPATH, '//*[@id="exampleModal"]/div/div')

    your_name = (By.XPATH, '//*[@id="refer_name"]')

    your_email = (By.XPATH, '//*[@id="email-input"]')

    country_code = (By.XPATH, '//*[@id="countryCodeSelect"]')

    mb_no_refer = (By.XPATH, '//*[@id="phoneNumber"]')

    refer = (By.XPATH, '//*[@id="continue-btn"]')

    delete = (By.XPATH, "//*[name()='rect' and contains(@opacity,'0.5')]")

    thanks_pop = (By.XPATH, '//*[@id="thanksModal"]/div/div')

    cl_thanks_pop = (By.XPATH, '//*[@id="thanksModal"]/div/div/div/button[1]')

    # ********************** Calculations of pricing *****************************************************

    no_pages = (By.XPATH, '//*[@id="script-conversion-input"]')

    with_lpp = (By.XPATH, '//*[@id="script-with-lpp"]')

    without_lpp = (By.XPATH, '//*[@id="script-without-lpp"]')

    price = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/div[1]/div/div[2]/div[1]/section[2]/div[2]/div[4]/span[2]')

    total_price = (By.XPATH, '//*[@id="hide-body-for-popups"]/main/div[1]/p')

    # **************************************** Demo ****************************************************
    demo = (By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[2]/div/div/div[1]/div[2]/a')

    ch_demo = (By.XPATH, '/html/body/main/main/section[2]/div/h2')

    subtitle_demo = (By.XPATH, '//*[@id="demo-subtitle"]')

    ch_script_pad = (By.XPATH, '/html/body/main/main/section[4]/p')

    script_pad_demo = (By.XPATH, '//*[@id="demo-script-pad"]')

    ch_project_center_demo = (By.XPATH, '/html/body/main/main/section[5]/p')

    project_center_demo = (By.XPATH, '//*[@id="demo-project-center"]')

    ch_premises_pool_demo = (By.XPATH, '/html/body/main/main/section[6]/p')

    premises_pool_demo = (By.XPATH, '//*[@id="demo-premise"]')

    ch_harkat_club_demo = (By.XPATH, '/html/body/main/main/section[7]/p')

    harkat_club_demo = (By.XPATH, "//video[@id='demo-harkat']")

    ch_script_audit_demo = (By.XPATH, '/html/body/main/main/section[8]/p')

    script_audit_demo = (By.XPATH, '//*[@id="demo-audit"]')

    ch_ppt_conversion_demo = (By.XPATH, '/html/body/main/main/section[9]/p')

    ppt_conversion_demo = (By.XPATH, '//*[@id="demo-ppt"]')

    ch_book_con_demo = (By.XPATH, '/html/body/main/main/section[10]/p')

    book_con_demo = (By.XPATH, '//*[@id="demo-book"]')

    ch_viewing_loung_demo = (By.XPATH, '/html/body/main/main/section[11]/p')

    viewing_loung_demo = (By.XPATH, '//*[@id="demo-viewing-lounge"]')

    ch_screenplay_narration_demo = (By.XPATH, '/html/body/main/main/section[12]/p')

    screenplay_narration_demo = (By.XPATH, '//*[@id="demo-char-intro"]')

    ch_corporate_membership_demo = (By.XPATH, '/html/body/main/main/section[13]/p')

    corporate_membership_demo = (By.XPATH, '//*[@id="demo-corporate"]')

    ch_pitchdeck_demo = (By.XPATH, '/html/body/main/main/section[14]/p')

    pitchdeck_demo = (By.XPATH, '//*[@id="demo-pitchdeck"]')

    ch_institutional_membership_demo = (By.XPATH, '/html/body/main/main/section[15]/p')

    institutional_membership_demo = (By.XPATH, '//*[@id="demo-institutional"]')

    ch_language_pare_partner_demo = (By.XPATH, '/html/body/main/main/section[16]/p')

    language_pare_partner_demo = (By.XPATH, '//*[@id="demo-lpp"]')

    ch_messiah_demo = (By.XPATH, '/html/body/main/main/section[17]/p')

    messiah_demo = (By.XPATH, '//*[@id="demo-messiah"]')

    ch_student_registration_demo = (By.XPATH, '/html/body/main/main/section[18]/p')

    student_registration_demo = (By.XPATH, '//*[@id="demo-student"]')

    # ****************************************** Footer Locaters *************************************

    promises_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/div/h5/a')

    scroll_footer = (By.XPATH, '//*[@id="forcedBottomFooter"]')

    premises_pool_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[1]/a')

    script_builder_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[2]/a')

    screenplay_conversion_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[3]/a')

    pitchdeck_creation_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[4]/a')

    screenplay_narration_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[5]/a')

    harkat_clubs_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[6]/a')

    project_center_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[7]/a')

    subtitle_hub_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[9]/a')

    viewing_Lounge_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[1]/ul/li[11]/a')

    # ****************************************** Footer Pricing *************************************

    pricing_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/div/h5/a')

    free_services_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[1]/a')

    discounts_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[2]/a')

    jug_pack_scr_writer_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[3]/a')

    jug_pack_prod_house_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[4]/a')

    subtitling_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[5]/a')

    screenplay_con_pricing_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[6]/a')

    scheduling_budjeting_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[7]/a')

    pitchdeck_creation_pricing_footer = (
    By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[8]/a')


    scrplay_narration_pricing_footer = (
    By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[9]/a')

    pricing_calculator_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[2]/ul/li[10]/a')

    # ***************************************** Opportunities *****************************

    opportunities_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[3]/div/h5/a')

    refer_mnf_footer = (By.XPATH, '/html/body/main/footer[1]/div/div/div[2]/div/div[3]/ul/li[1]/a')

    # ****************************************** Mildston Pages Login Registration ********************

    login_registration = (By.XPATH, "//div[@class='modal-body']")

    idea_mildstone = (By.XPATH, '/html/body/div[1]/picture/img')

    mildstone_registration = (By.XPATH, '//*[@id="exampleModal"]/div/div/div/div[1]/div[2]/span[1]/a')

    mildstone_login = (By.XPATH, '//*[@id="exampleModal"]/div/div/div/div[1]/div[2]/span[2]/a')

    script_mildstone = (By.XPATH, "//div[@class='buildImgPopupClick']//picture")

    traslate_mildstone = (By.XPATH, '/html/body/div[1]/picture/img')

    # ****************************************** FUNCTIONS **********************************************
    def clk_idea(self):
        ele = self.wafe(self.idea)
        ele.click()

    def clk_script(self):
        ele = self.wafe(self.script)
        ele.click()

    def clk_translate(self):
        ele = self.wafe(self.translate)
        ele.click()

    def clk_narrate(self):
        ele = self.wafe(self.narrate)
        ele.click()

    def clk_buildTeam(self):
        ele = self.wafe(self.buildTeam)
        ele.click()

    def clk_produce(self):
        ele = self.wafe(self.produce)
        ele.click()

    def clk_subtitle(self):
        ele = self.wafe(self.subtitle)
        ele.click()

    def clk_exhibit(self):
        ele = self.wafe(self.exhibit)
        ele.click()

    def scroll(self):
        element_to_scroll_to = self.wafe(self.promises_footer)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def get_email_id(self):
        ele = self.wafe(self.email_id)
        return ele.text

    def clk_instagram(self):
        ele = self.wafe(self.instagram)
        ele.click()
    def clk_facebook(self):
        ele = self.wafe(self.facebook)
        ele.click()

    def clk_twter(self):
        ele = self.wafe(self.twter)
        ele.click()

    def clk_youtube(self):
        ele = self.wafe(self.youtube)
        ele.click()

    def clk_linked_in(self):
        ele = self.wafe(self.linked_in)
        ele.click()

    # def clk_imdb(self):
    #     ele = self.wafe(self.imdb)
    #     ele.click()

    def clk_threads_in(self):
        ele = self.wafe(self.threads)
        ele.click()

    def clk_pinterest(self):
        ele = self.wafe(self.pinterest)
        ele.click()

    def hover_explore(self):
        ele = self.wafe(self.explore)
        actions = ActionChains(self.driver)
        actions.move_to_element(ele).perform()

    def chk_dropdown_menu(self):
        try:
            ele = self.wafe(self.dp_menu)
            return ele.is_displayed()
        except:
            return False

    def clk_promises(self):
        ele = self.wafe(self.promises)
        ele.click()

    def chk_promises(self):
        try:
            ele = self.wafe(self.ch_promises)
            return ele.is_displayed()
        except:
            return False

    def clk_premises_pool(self):
        ele = self.wafe(self.premises_pool)
        ele.click()

    def chk_premises_pool(self):
        try:
            ele = self.wafe(self.ch_premises_pool)
            return ele.is_displayed()
        except:
            return

    def clk_sound_premises_pool(self):
        ele = self.wafe(self.sd_premises_pool)
        ele.click()

    def chk_hd_icon_premises_pool(self):
        try:
            ele = self.wafe(self.hd_premises_pool)
            return ele.is_displayed()
        except:
            return

    def scroll1(self):
        element_to_scroll_to = self.wafe(self.hd_premises_pool)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_script_builder(self):
        ele = self.wafe(self.script_builder)
        ele.click()

    def chk_script_builder(self):
        try:
            ele = self.wafe(self.ch_script_builder)
            return ele.is_displayed()
        except:
            return False

    def clk_sound_script_builder(self):
        ele = self.wafe(self.sd_script_builder)
        ele.click()

    def chk_hd_icon_script_builderl(self):
        try:
            ele = self.wafe(self.hd_script_builder)
            return ele.is_displayed()
        except:
            return

    def scroll2(self):
        element_to_scroll_to = self.wafe(self.hd_script_builder)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_screenplay_conversion(self):
        ele = self.wafe(self.screenplay_conversion)
        ele.click()

    def chk_screenplay_conversion(self):
        try:
            ele = self.wafe(self.ch_screenplay_conversion)
            return ele.is_displayed()
        except:
            return False

    def clk_sound_screenplay_conversion(self):
        ele = self.wafe(self.sd_screenplay_conversion)
        ele.click()

    def chk_hd_icon_screenplay_conversion(self):
        try:
            ele = self.wafe(self.hd_screenplay_conversion)
            return ele.is_displayed()
        except:
            return

    def scroll3(self):
        element_to_scroll_to = self.wafe(self.hd_screenplay_conversion)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_pitchdeck_creation(self):
        ele = self.wafe(self.pitchdeck_creation)
        ele.click()

    def chk_pitchdeck_creation(self):
        try:
            ele = self.wafe(self.ch_pitchdeck_creation)
            return ele.is_displayed()
        except:
            return

    def clk_sound_pitchdeck_creation(self):
        ele = self.wafe(self.sd_pitchdeck_creation)
        ele.click()

    def chk_hd_icon_pitchdeck_creation(self):
        try:
            ele = self.wafe(self.hd_pitchdeck_creation)
            return ele.is_displayed()
        except:
            return

    def scroll4(self):
        element_to_scroll_to = self.wafe(self.hd_pitchdeck_creation)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_screenplay_narration(self):
        ele = self.wafe(self.screenplay_narration)
        ele.click()

    def chk_screenplay_narration(self):
        try:
            ele = self.wafe(self.ch_screenplay_narration)
            return ele.is_displayed()
        except:
            return

    def clk_sound_screenplay_narration(self):
        ele = self.wafe(self.sd_screenplay_narration)
        ele.click()

    def chk_hd_icon_screenplay_narration(self):
        try:
            ele = self.wafe(self.hd_screenplay_narration)
            return ele.is_displayed()
        except:
            return

    def scroll5(self):
        element_to_scroll_to = self.wafe(self.hd_screenplay_narration)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_harkat_clubs(self):
        ele = self.wafe(self.harkat_clubs)
        ele.click()

    def chk_harkat_clubs(self):
        try:
            ele = self.wafe(self.ch_harkat_clubs)
            return ele.is_displayed()
        except:
            return

    def clk_sound_harkat_clubs(self):
        ele = self.wafe(self.sd_harkat_clubs)
        ele.click()

    def chk_hd_icon_harkat_clubs(self):
        try:
            ele = self.wafe(self.hd_harkat_clubs)
            return ele.is_displayed()
        except:
            return

    def scroll6(self):
        element_to_scroll_to = self.wafe(self.hd_harkat_clubs)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_project_center(self):
        ele = self.wafe(self.project_center)
        ele.click()

    def chk_project_center(self):
        try:
            ele = self.wafe(self.ch_project_center)
            return ele.is_displayed()
        except:
            return

    def clk_sound_project_center(self):
        ele = self.wafe(self.sd_project_center)
        ele.click()

    def chk_hd_icon_project_center(self):
        try:
            ele = self.wafe(self.hd_project_center)
            return ele.is_displayed()
        except:
            return

    def scroll7(self):
        element_to_scroll_to = self.wafe(self.hd_project_center)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_subtitle_hub(self):
        ele = self.wafe(self.subtitle_hub)
        ele.click()

    def chk_subtitle_hub(self):
        try:
            ele = self.wafe(self.ch_subtitle_hub)
            return ele.is_displayed()
        except:
            return

    def clk_sound_subtitle_hub(self):
        ele = self.wafe(self.sd_subtitle_hub)
        ele.click()

    def chk_hd_icon_subtitle_hub(self):
        try:
            ele = self.wafe(self.hd_subtitle_hub)
            return ele.is_displayed()
        except:
            return

    def scroll8(self):
        element_to_scroll_to = self.wafe(self.hd_subtitle_hub)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_Viewing_Lounge(self):
        ele = self.wafe(self.Viewing_Lounge)
        ele.click()

    def chk_Viewing_Lounge(self):
        try:
            ele = self.wafe(self.ch_Viewing_Lounge)
            return ele.is_displayed()
        except:
            return

    def clk_sound_Viewing_Lounge(self):
        ele = self.wafe(self.sd_Viewing_Lounge)
        ele.click()

    def chk_hd_icon_Viewing_Lounge(self):
        try:
            ele = self.wafe(self.hd_Viewing_Lounge)
            return ele.is_displayed()
        except:
            return

    def scroll9(self):
        element_to_scroll_to = self.wafe(self.hd_Viewing_Lounge)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()


    def clk_idea_img(self):
        ele = self.wafe(self.idea1)
        ele.click()

    def clk_script_img(self):
        ele = self.wafe(self.script1)
        ele.click()

    def clk_translate_img(self):
        ele = self.wafe(self.translate1)
        ele.click()

    def clk_pitchdack_img(self):
        ele = self.wafe(self.pitchdack1)
        ele.click()

    def clk_narrate_img(self):
        ele = self.wafe(self.narrate1)
        ele.click()

    def clk_build_team_img(self):
        ele = self.wafe(self.build_team1)
        ele.click()

    def clk_produce_img(self):
        ele = self.wafe(self.produce1)
        ele.click()

    def clk_subtitle_img(self):
        ele = self.wafe(self.subtitle1)
        ele.click()

    def clk_exhibit_img(self):
        ele = self.wafe(self.exhibit1)
        ele.click()


    # ********************* pricing Functions **************************************************************

    def clk_pricing(self):
        ele = self.wafe(self.pricing)
        ele.click()

    def chk_pricing(self):
        try:
            ele = self.wafe(self.ch_pricing)
            return ele.is_displayed()
        except:
            return False

    def clk_free_services(self):
        ele = self.wafe(self.free_services)
        ele.click()

    def chk_free_services(self):
        try:
            ele = self.wafe(self.ch_free_services)
            return ele.is_displayed()
        except:
            return False

    def clk_discounts(self):
        ele = self.wafe(self.discounts)
        ele.click()

    def chk_discounts(self):
        try:
            ele = self.wafe(self.ch_discounts)
            return ele.is_displayed()
        except:
            return False
    def clk_jug_pack_scr_writer(self):
        ele = self.wafe(self.jug_pack_scr_writer)
        ele.click()

    # def chk_jug_pack_scr_writer(self):
    #     try:
    #         ele = self.wafe(self.ch_jug_pack_scr_writer)
    #         return ele.is_displayed()
    #     except:
    #         return False

    def clk_jug_pack_prod_house(self):
        ele = self.wafe(self.jug_pack_prod_house)
        ele.click()

    # def chk_jug_pack_prod_house(self):
    #     try:
    #         ele = self.wafe(self.ch_jug_pack_prod_house)
    #         return ele.is_displayed()
    #     except:
    #         return False

    def clk_subtitling(self):
        ele = self.wafe(self.subtitling)
        ele.click()

    def chk_subtitling(self):
        try:
            ele = self.wafe(self.ch_subtitling)
            return ele.is_displayed()
        except:
            return False

    def clk_screenplay_con_pricing(self):
        ele = self.wafe(self.screenplay_con_pricing)
        ele.click()

    def chk_screenplay_con_pricing(self):
        try:
            ele = self.wafe(self.ch_screenplay_con_pricing)
            return ele.is_displayed()
        except:
            return False

    def clk_scheduling_budjeting(self):
        ele = self.wafe(self.scheduling_budjeting)
        ele.click()

    def chk_scheduling_budjeting(self):
        try:
            ele = self.wafe(self.ch_scheduling_budjeting)
            return ele.is_displayed()
        except:
            return False

    def clk_pitchdeck_creation_pricing(self):
        ele = self.wafe(self.pitchdeck_creation_pricing)
        ele.click()

    def chk_pitchdeck_creation_pricing(self):
        try:
            ele = self.wafe(self.ch_pitchdeck_creation_pricing)
            return ele.is_displayed()
        except:
            return False

    def clk_scrplay_narration_pricing(self):
        ele = self.wafe(self.scrplay_narration_pricing)
        ele.click()

    def chk_scrplay_narration_pricing(self):
        try:
            ele = self.wafe(self.ch_pitchdeck_creation_pricing)
            return ele.is_displayed()
        except:
            return False

    def clk_pricing_calculator(self):
        ele = self.wafe(self.pricing_calculator)
        ele.click()

    def chk_pricing_cal_img(self):
        try:
            ele = self.wafe(self.ch_pricing_cal_img)
            return ele.is_displayed()
        except:
            return False

    def clk_jug_pack_scr_writer_img(self):
        ele = self.wafe(self.jug_pack_scr_writer_img)
        ele.click()

    def clk_jug_pack_prod_house_img(self):
        ele = self.wafe(self.jug_pack_prod_house_img)
        ele.click()

    def clk_pricing_calculator_img(self):
        ele = self.wafe(self.pricing_calculator_img)
        ele.click()

    def chk_pricing_calculator_pop(self):
        try:
            ele = self.wafe(self.ch_pricing_calculator_pop)
            return ele.is_displayed()
        except:
            return False

    def clk_cl_pricing_calculator_pop(self):
        ele = self.wafe(self.cl_pricing_calculator_pop)
        return ele.is_displayed()

    def clk_opportunities(self):
        ele = self.wafe(self.opportunities)
        ele.click()

    def chk_opportunities(self):
        try:
            ele = self.wafe(self.ch_opportunities)
            return ele.is_displayed()
        except:
            return False

    def clk_refer_mnf(self):
        ele = self.wafe(self.refer_mnf)
        ele.click()

    def chk_refer_mnf(self):
        try:
            ele = self.wafe(self.ch_refer_mnf)
            return ele.is_displayed()
        except:
            return False

    def clk_sound_refer_mnf(self):
        ele = self.wafe(self.sd_refer_mnf)
        ele.click()

    def chk_hd_refer_mnf(self):
        try:
            ele = self.wafe(self.hd_refer_mnf)
            return ele.is_displayed()
        except:
            return False

    def scroll10(self):
        element_to_scroll_to = self.wafe(self.btn_refer_mnf)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_btn_refer_mnf(self):
        ele = self.wafe(self.btn_refer_mnf)
        ele.click()

    def chk_refer_mnf_pop(self):
        try:
            ele = self.wafe(self.refer_mnf_pop)
            return ele.is_displayed()
        except:
            return False

    def clk_cl_refer_mnf_pop(self):
        ele = self.wafe(self.cl_refer_mnf_pop)
        ele.click()

    def send_email1(self):
        fake = Faker()
        fake_email = fake.email()
        ele = self.wafe(self.email_tb1)
        return ele.send_keys(fake_email)

    def send_email2(self):
        ele = self.wafe(self.email_tb1)
        return ele.send_keys("abc@gmail.com")

    def send_email3(self):
        ele = self.wafe(self.email_tb2)
        return ele.send_keys("abc@gmail.com")

    def chk_same_email_error(self):
        try:
            ele = self.wafe(self.same_email_error)
            return ele.is_displayed()
        except:
            return False

    def chk_continue_btn_enable(self):
        ele = self.wafe(self.cl_refer_mnf_pop)
        return ele.is_enabled()

    def clk_add_another_btn(self):
        ele = self.wafe(self.add_another)
        ele.click()

    def chk_email2_tb(self):
        try:
            ele = self.wafe(self.email_tb2)
            return ele.is_displayed()
        except:
            return False

    def send_email_tb2(self):
        fake = Faker()
        fake_email = fake.email()
        ele = self.wafe(self.email_tb2)
        return ele.send_keys(fake_email)

    def send_email_tb3(self):
        fake = Faker()
        fake_email = fake.email()
        ele = self.wafe(self.email_tb3)
        return ele.send_keys(fake_email)

    def send_email_tb4(self):
        fake = Faker()
        fake_email = fake.email()
        ele = self.wafe(self.email_tb4)
        return ele.send_keys(fake_email)

    def send_email_tb5(self):
        fake = Faker()
        fake_email = fake.email()
        ele = self.wafe(self.email_tb5)
        return ele.send_keys(fake_email)

    def chk_max_5_email_error(self):
        try:
            ele = self.wafe(self.max_5)
            return ele.is_displayed()
        except:
            return False
    def clk_delete_btn(self):
        ele = self.wafe(self.delete)
        ele.click()

    def clk_continue_btn(self):
        ele = self.wafe(self.btn_continue)
        ele.click()

    def chk_continue_pop(self):
        try:
            ele = self.wafe(self.continue_pop)
            return ele.is_displayed()
        except:
            return False

    def clk_cl_continue_btn_pop(self):
        ele = self.wafe(self.btn_cl)
        ele.click()

    def send_your_name(self):
        fake = Faker()
        fake_name = fake.name()
        ele = self.wafe(self.your_name)
        return ele.send_keys(fake_name)

    def chk_refer_btn(self):
        ele = self.wafe(self.refer)
        return ele.is_enabled()

    def send_your_email(self):
        fake = Faker()
        fake_email = fake.email()
        ele = self.wafe(self.your_email)
        return ele.send_keys(fake_email)

    def send_country_code(self):
        ele = self.wafe(self.country_code)
        Select(ele).select_by_index(1)

    def send_mb_number(self):
        ele = self.wafe(self.mb_no_refer)
        return ele.send_keys("1234567890")

    def clk_refer_btn(self):
        ele = self.wafe(self.refer)
        ele.click()

    def chk_thanks_pop(self):
        try:
            ele = self.wafe(self.thanks_pop)
            return ele.is_displayed()
        except:
            return False

    def clk_cl_thanks_pop(self):
        ele = self.wafe(self.cl_thanks_pop)
        ele.click()

    # ************************** calculate ***************************************

    def send_no_pages(self):
        ele = self.wafe(self.no_pages)
        return ele.send_keys("100")

    def clk_with_lpp(self):
        ele = self.wafe(self.with_lpp)
        ele.click()

    def clk_without_lpp(self):
        ele = self.wafe(self.without_lpp)
        ele.click()

    def get_price(self):
        ele = self.wafe(self.price)
        return ele.text

    def get_total_price(self):
        ele = self.wafe(self.total_price)
        return ele.text

    def get_calculations(self):
        result = 100 * 3
        res = (result / 100) * 30
        return "{:.2f}".format(result - res)
    # ************************** Demo **************************************************
    def clk_demo(self):
        ele = self.wafe(self.demo)
        ele.click()

    def chk_demo(self):
        try:
            ele = self.wafe(self.ch_demo)
            return ele.is_displayed()
        except:
            return False

    def clk_subtitle_demo(self):
        ele = self.wafe(self.subtitle_demo)
        ele.click()

    def scroll11(self):
        element_to_scroll_to = self.wafe(self.ch_script_pad)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()


    def clk_script_pad_demo(self):
        ele = self.wafe(self.script_pad_demo)
        ele.click()


    def scroll12(self):
        element_to_scroll_to = self.wafe(self.ch_project_center_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()
    def clk_project_center_demo(self):
        ele = self.wafe(self.project_center_demo)
        ele.click()
    def scroll13(self):
        element_to_scroll_to = self.wafe(self.ch_premises_pool_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_premises_pool_demo(self):
        ele = self.wafe(self.premises_pool_demo)
        ele.click()
    def scroll14(self):
        element_to_scroll_to = self.wafe(self.ch_harkat_club_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_harkat_club_demo(self):
        ele = self.wafe(self.harkat_club_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll15(self):
        element_to_scroll_to = self.wafe(self.ch_script_audit_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_script_audit_demo(self):
        ele = self.wafe(self.script_audit_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll16(self):
        element_to_scroll_to = self.wafe(self.ch_ppt_conversion_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_ppt_conversion_demo(self):
        ele = self.wafe(self.ppt_conversion_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll17(self):
        element_to_scroll_to = self.wafe(self.ch_book_con_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_book_conversion_demo(self):
        ele = self.wafe(self.book_con_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll18(self):
        element_to_scroll_to = self.wafe(self.ch_viewing_loung_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_ppt_viewing_loung_demo(self):
        ele = self.wafe(self.viewing_loung_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll19(self):
        element_to_scroll_to = self.wafe(self.ch_screenplay_narration_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_screenplay_narration_demo(self):
        ele = self.wafe(self.screenplay_narration_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll20(self):
        element_to_scroll_to = self.wafe(self.ch_corporate_membership_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_corporate_membership_demo(self):
        ele = self.wafe(self.corporate_membership_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll21(self):
        element_to_scroll_to = self.wafe(self.ch_pitchdeck_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_pitchdeck_demo(self):
        ele = self.wafe(self.pitchdeck_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll22(self):
        element_to_scroll_to = self.wafe(self.ch_institutional_membership_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_institutional_membership_demo(self):
        ele = self.wafe(self.institutional_membership_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll23(self):
        element_to_scroll_to = self.wafe(self.ch_language_pare_partner_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_language_pare_partner_demo(self):
        ele = self.wafe(self.language_pare_partner_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()

    def scroll24(self):
        element_to_scroll_to = self.wafe(self.ch_messiah_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_messiah_demo(self):
        ele = self.wafe(self.messiah_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()

    def scroll25(self):
        element_to_scroll_to = self.wafe(self.ch_student_registration_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_student_registration_demo(self):
        ele = self.wafe(self.student_registration_demo)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(ele).perform()
    def scroll26(self):
        element_to_scroll_to = self.wafe(self.ch_student_registration_demo)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()


    # ********************************* Footer - Promises ************************************************************

    def clk_promises_footer(self):
        ele = self.wafe(self.promises_footer)
        ele.click()
    def scroll31(self):
        element_to_scroll_to = self.wafe(self.scroll_footer)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_scroll_to).perform()

    def clk_premises_pool_footer(self):
        ele = self.wafe(self.premises_pool_footer)
        ele.click()
    def clk_script_builder_footer(self):
        ele = self.wafe(self.script_builder_footer)
        ele.click()

    def clk_screenplay_conversion_footer(self):
        ele = self.wafe(self.screenplay_conversion_footer)
        ele.click()

    def clk_pitchdeck_creation_footer(self):
        ele = self.wafe(self.pitchdeck_creation_footer)
        ele.click()

    def clk_screenplay_narration_footer(self):
        ele = self.wafe(self.screenplay_narration_footer)
        ele.click()

    def clk_harkat_clubs_footer(self):
        ele = self.wafe(self.harkat_clubs_footer)
        ele.click()

    def clk_project_center_footer(self):
        ele = self.wafe(self.project_center_footer)
        ele.click()

    def clk_subtitle_hub_footer(self):
        ele = self.wafe(self.subtitle_hub_footer)
        ele.click()

    def clk_viewing_Lounge_footer(self):
        ele = self.wafe(self.viewing_Lounge_footer)
        ele.click()

    # ********************************* Footer - Pricing ************************************************************

    def clk_pricing_footer(self):
        ele = self.wafe(self.pricing_footer)
        ele.click()

    def clk_free_services_footer(self):
        ele = self.wafe(self.free_services_footer)
        ele.click()

    def clk_discounts_footer(self):
        ele = self.wafe(self.discounts_footer)
        ele.click()

    def clk_jug_pack_scr_writer_footer(self):
        ele = self.wafe(self.jug_pack_scr_writer_footer)
        ele.click()

    def clk_jug_pack_prod_house_footer(self):
        ele = self.wafe(self.jug_pack_prod_house_footer)
        ele.click()

    def clk_subtitle_hub_pricing_footer(self):
        ele = self.wafe(self.subtitling_footer)
        ele.click()

    def clk_screenplay_con_pricing_footer(self):
        ele = self.wafe(self.screenplay_con_pricing_footer)
        ele.click()

    def clk_scheduling_budjeting_footer(self):
        ele = self.wafe(self.scheduling_budjeting_footer)
        ele.click()

    def clk_pitchdeck_creation_pricing_footer(self):
        ele = self.wafe(self.pitchdeck_creation_pricing_footer)
        ele.click()

    def clk_screenplay_narration_pricing_footer(self):
        ele = self.wafe(self.scrplay_narration_pricing_footer)
        ele.click()

    def clk_pricing_calculator_footer(self):
        ele = self.wafe(self.pricing_calculator_footer)
        ele.click()

    # ********************************* Footer - Opportunities ************************************************************

    def clk_opportunities_footer(self):
        ele = self.wafe(self.opportunities_footer)
        ele.click()

    def clk_refer_mnf_footer(self):
        ele = self.wafe(self.refer_mnf_footer)
        ele.click()

    # ********************************* Footer - Opportunities ************************************************************

    def clk_idea_mildstone(self):
        ele = self.wafe(self.idea_mildstone)
        ele.click()

    def chk_login_regi_pop(self):
        try:
            ele = self.wafe(self.login_registration)
            return ele.is_displayed()
        except:
            return False
    def clk_mildstone_registration(self):
        ele = self.wafe(self.mildstone_registration)
        ele.click()

    def clk_mildstone_login(self):
        ele = self.wafe(self.mildstone_login)
        ele.click()

    def clk_script_mildstone(self):
        ele = self.wafe(self.script_mildstone)
        ele.click()