from hamcrest import assert_that, is_not, is_

from app.page.app import App
from app.page.main import Main
from app.page.search_page import SearchPage
import pytest
import yaml

from app.utils.data_utils import DataUtils


class TestDeleteMember:
    # class的driver共用
    def setup_class(self):
        self.app = App()
        self.contact = DataUtils().load_data("../data/contact.yaml")["contact"]

    def setup(self):
        self.main = self.app.start().goto_main()

    @pytest.mark.skip
    def test_delete_member(self):
        member_name = self.contact["name"]
        search_page: SearchPage = self.main.goto_contact_page().goto_search_page()
        members = search_page.search(member_name)
        origin_length = len(members)
        assert_that(origin_length, is_not(0), "search member is exist")
        if origin_length != 0:
            search_page.goto_personal_detail_page(members[0]).goto_personal_edit_page().delete_member()
            assert_that(len(search_page.search(member_name)), is_(origin_length - 1), "delete success")


    def test_add_member(self):
        # print(DataUtils().load_data("../data/contact.yaml"))

        result = self.main.goto_contact_page().add_contact_manually().edit_member(self.contact["name"], self.contact["gender"], self.contact["phonenum"]).verify_toast()
        assert '添加成功' == result
