from hamcrest import assert_that, is_not, is_

from app.page.index_page import IndexPage
from app.page.search_page import SearchPage


class TestDeleteMember:
    def setup(self):
        self.index_page = IndexPage()

    def test_delete_member(self):
        member_name = "neal"
        search_page: SearchPage = self.index_page.goto_contact_page().goto_search_page()
        members = search_page.search(member_name)
        origin_length = len(members)
        assert_that(origin_length, is_not(0), "search member is exist")
        if origin_length != 0:
            search_page.goto_personal_detail_page(members[0]).goto_personal_edit_page().delete_member()
            assert_that(len(search_page.search(member_name)), is_(origin_length - 1), "delete success")
