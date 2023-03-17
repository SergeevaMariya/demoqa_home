from pages.swag_lab import SwagLabs

def test_swag(browser):
    testswag = SwagLabs(browser)
    testswag.vizit()
    testswag.exist_icon()


def test_swag2(browser):
    testswag = SwagLabs(browser)
    testswag.vizit()
    testswag.find_element('#user-name')

def tast_swag3(browser):
    testswag = SwagLabs(browser)
    testswag.vizit()
    testswag.find_element('#password')

    # help help