from my_selenium.podemo.index_page import IndexPage


class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_add_contact(self):
        name = "xiaoming"
        account = "aaaa"
        phonenum = "123234"

        addmemberpage = self.index.click_add_member()
        addmemberpage.add_member(name, account, phonenum)
        result = addmemberpage.get_member(name)
        assert result