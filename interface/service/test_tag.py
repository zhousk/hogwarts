import json

import pytest
import requests


from hamcrest import assert_that, has_item

from interface.service.tag import Tag


class TestTag:
    def setup_class(self):
        # todo：数据清理的过程，把测试数据清空或者还原
        self.tag = Tag()
        self.tag.get_token()
        self.origin_data = self.tag.list().json()["tag_group"]

    def teardown_class(self):
        self.data_after_test = self.tag.list().json()["tag_group"]

        # 方法一：
        # 简单粗暴,全部删除,然后把原本的数据全部add进去
        for data in self.data_after_test:
            self.tag.delete([],data["group_id"])
        for data in self.origin_data:
            tags = [{'name': tag['name']} for tag in data["tag"]]
            self.tag.add(data["group_name"], tags)

        # 方法二：
        # # 恢复数据，通过比较原始数据和操作后的数据，还原被删除的数据
        # group_names = [group["group_name"] for group in self.data_after_test]
        # # tag_group_name = [{group["group_name"]:[tag["name"] for tag in group["tag"]]} for group in self.data_after_test]
        #
        # for origin_tag_group in self.origin_data:
        #     if origin_tag_group["group_names"] not in group_names:
        #         origin_tags = [{['name':origin_tag["name"]} for origin_tag in origin_tag_group["tag"]]
        #         self.tag.add(origin_tag_group["group_names"], origin_tags)
        #     else:
        #         # 当group没有变，查看tag是否少了，少了就还原,这里需要比较两个新老数据group对应的tag队列，嵌套迭代，效率非常差
        #         pass
        #
        # # 删除数据，通过比较原始数据和操作后的数据，删除新增的数据
        # origin_group_ids = [group["group_id"] for group in self.origin_data]
        #
        # for tag_group in self.data_after_test:
        #     if tag_group["group_id"] not in origin_group_ids:
        #         self.tag.delete(tag_group["group_id"], [])
        #     else:
        #         # 同理，需要比较新老数据的tag_id然后删除
        #         pass

    def test_tag_list(self):
        # todo: 完善功能测试
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("group_name, tag_names", [
        ["group_demo_1201", [{'name': 'tag_demo_1201'}]],
        ["group_demo_1202", [{'name': 'tag_demo_1202'}, {'name': 'tag_demo_1203'}]],
    ])
    def test_tag_add(self, group_name, tag_names):
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        # assert r.json()['errcode'] == 0

        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [{'name': tag['name']} for tag in group['tag']]
        print(group)
        print(tags)
        assert group['group_name'] == group_name
        assert tags == tag_names

    @pytest.mark.parametrize("group_name", [
        ["group_demo_haha"],
    ])
    def test_tag_add_without_tag_name(self, group_name):
        r = self.tag.add(group_name, [])
        assert r.status_code == 200
        assert r.json()['errcode'] != 0
        assert r.json()['errmsg'].find("some parameters are empty") != 0

    @pytest.mark.parametrize("tag_name", [
        ["tag_name111"],
    ])
    def test_tag_add_without_group_name(self, tag_name):
        r = self.tag.add([], tag_name)
        assert r.status_code == 200
        assert r.json()['errcode'] != 0
        assert r.json()['errmsg'].find("some parameters are empty") != 0

    def test_tag_add_with_emptry(self):
        r = self.tag.add(["   "], ["        "])
        assert r.status_code == 200
        assert r.json()['errcode'] != 0
        assert r.json()['errmsg'].find("some parameters are empty") != 0

    def test_tag_add_with_none(self):
        r = self.tag.add([], [])
        assert r.status_code == 200
        assert r.json()['errcode'] != 0
        assert r.json()['errmsg'].find("some parameters are empty") != 0

    def test_tag_add_length_over_the_limit(self):
        r = self.tag.add(["11111111111111111111111111111"], [])
        assert r.status_code == 200
        assert r.json()['errcode'] != 0
        assert r.json()['errmsg'].find("wrong json format") != 0

    def test_delete_with_groupid_and_tag_id(self):
        tag_group = self.tag.list().json()["tag_group"]
        # 因为当没有客户标签的时候，依然会有一行默认的tag_group存在（也就是客户级别），所以通过长度判断是否有数据
        if len(tag_group) <= 1:
            print("没有数据")
        else:
            group_id = [tag_group[0]["group_id"]]
            tag_id = [tag_group[0]["tag"][0]["id"]]
            r = self.tag.delete(tag_id, group_id)
            assert r.status_code == 200
            assert r.json()['errcode'] == 0

    def test_delete_with_groupid(self):
        tag_group = self.tag.list().json()["tag_group"]
        # 因为当没有客户标签的时候，依然会有一行默认的tag_group存在（也就是客户级别），所以通过长度判断是否有数据
        if len(tag_group) <= 1:
            print("没有数据")
        else:
            group_id = [tag_group[0]["group_id"]]
            r = self.tag.delete([], group_id)
            group_ids_result = [group["group_id"] for group in self.tag.list().json()["tag_group"]]
            # 删除后groupid不在列表出现
            assert_that(group_ids_result, not (has_item(group_id)))
            assert r.status_code == 200
            assert r.json()['errcode'] == 0

    def test_delete_with_tagid(self):
        tag_group = self.tag.list().json()["tag_group"]
        # 因为当没有客户标签的时候，依然会有一行默认的tag_group存在（也就是客户级别），所以通过长度判断是否有数据
        if len(tag_group) <= 1:
            print("没有数据")
        else:
            tag_id = [tag_group[0]["tag"][0]["id"]]
            r = self.tag.delete(tag_id, [])
            assert r.status_code == 200
            assert r.json()['errcode'] == 0

    def test_delete_with_tagid_and_groupid_are_none(self):
        r = self.tag.delete([], [])
        assert r.status_code == 200
        assert r.json()['errcode'] != 0

    def test_delete_with_all_tagid_group_will_delete_automatically(self):
        tag_group = self.tag.list().json()["tag_group"]
        # 因为当没有客户标签的时候，依然会有一行默认的tag_group存在（也就是客户级别），所以通过长度判断是否有数据
        if len(tag_group) <= 1:
            print("没有数据")
        else:
            group_id = tag_group[0]["group_id"]
            tag_ids = [tag["id"] for tag in tag_group[0]["tag"]]
            r = self.tag.delete(tag_ids, [])
            group_ids_result = [group["group_id"] for group in self.tag.list().json()["tag_group"]]
            # 删除后groupid不在列表出现
            assert_that(group_ids_result, not (has_item(group_id)))
            assert r.status_code == 200
            assert r.json()['errcode'] == 0

