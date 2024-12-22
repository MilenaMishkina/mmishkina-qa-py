class TestSendingJoke:

    BUZZ_BUTTON = ('xpath', '//span[text() = "Buzz"]')
    POST_INPUT = ('xpath', '//textarea[@class = "oxd-buzz-post-input"]')
    POST_BUTTON = ('xpath', '//button[@type = "submit"]')
    NEW_POST = ('xpath', '(//div[@class = "orangehrm-buzz-post-body"]//p)[1]')
    NAME = ('xpath', '(//p[@class = "oxd-text oxd-text--p orangehrm-buzz-post-emp-name"])[1]')

    def test_joke_posted(self, get_driver, setup_method, get_joke):
        joke_test = get_joke
        get_driver.find_element(*self.BUZZ_BUTTON).click()
        get_driver.find_element(*self.POST_INPUT).send_keys(joke_test)
        get_driver.find_element(*self.POST_BUTTON).click()

        new_post_text = get_driver.find_element(*self.NEW_POST).text
        assert joke_test.rstrip() == new_post_text, 'Текст поста и шутки не совпадают'









