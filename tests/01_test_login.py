from pages.login_page import LoginPage


def test_login_page_flow(page):

    login = LoginPage(page)
    login.navigate()

    assert login.is_email_input_visible()
    print(f"\nFormularul de email este vizibil")

    login.enter_email("test.automation@gmail.com")
    print(f"Email introdus: test.automation@gmail.com")
