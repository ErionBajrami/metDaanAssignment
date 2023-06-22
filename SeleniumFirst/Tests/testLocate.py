from selenium.webdriver.common.by import By


class PageMainLocate(object):
    CAN = (By.LINK_TEXT, "Create an Account")
    SI = (By.LINK_TEXT, "Sign In")


class SignUpLogInAndMorePageLocate(object):
    #LOGIN AND SIGNUP
    f = (By.ID, "firstname")
    la = (By.ID, "lastname")
    e = (By.ID, "email_address")
    eLog = (By.ID, "email")
    p = (By.ID, "password")
    pLog = (By.ID, "pass")
    pc = (By.ID, "password-confirmation")

    #MAIN PAGE
    Login = (By.LINK_TEXT, "Sign In")
    Ca = (By.LINK_TEXT, "Create an Account")

    #SHIPPING AND BILLING
    first = (By.NAME, "firstname")
    last = (By.NAME, "lastname")
    CMP = (By.NAME, "company")
    CT = (By.NAME, "city")
    ST0 = (By.NAME, "street[0]")
    ST1 = (By.NAME, "street[1]")
    ST2 = (By.NAME, "street[2]")
    PostC = (By.NAME, "postcode")


class ProductInformationAntonia(object):
    NameA = "Antonia Racer Tank"
    PriceA = "$34.00"
    DescA = "You won't know what you like best about the Antonia Racer Tank: soft, "\
            'stretchy, lightweight fabric? Super-cute colorblocked details? Whatever it '\
            'is, this piece is sure to quickly move to the top of your workout rotation.'
    CheckBoxXS = "XS"
    CheckBoxS = "S"
    CheckBoxM = "M"
    CheckBoxL = "L"
    CheckBoxXL = "XL"