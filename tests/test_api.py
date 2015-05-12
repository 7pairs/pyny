# -*- coding: utf-8 -*-

#
# Copyright 2015 Jun-ya HASEBA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from unittest import TestCase


class ApiTest(TestCase):
    """
    api.pyに対するテストコード。
    """

    def test_get_item_count_01(self):
        """
        [対象] get_item_count()
        [条件] 有効なレイヤIDを指定して呼び出す。
        [結果] 件数がが返されること。
        """
        from pyny import api
        actual = api.get_item_count('c1120')

        self.assertEqual(71, actual)

    def test_get_item_count_02(self):
        """
        [対象] get_item_count()
        [条件] 無効なレイヤIDを指定して呼び出す。
        [結果] PynyErrorが送出されること。
        """
        from pyny import PynyError

        with self.assertRaises(PynyError):
            api.get_item_count('error')