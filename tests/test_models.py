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

from pyny.fields import StringField
from pyny.models import Model


class StringModel(Model):
    """
    StringFieldをテストするためのモデル。
    """
    created = StringField()
    geo = StringField('geometry')
    name = StringField('attrs.attr2')


class ModelTest(TestCase):
    """
    Modelに対するテストコード。
    """

    def test_get_all_data_01(self):
        """
        [対象] get_all_data() : No.01
        [条件] 有効なレイヤIDを指定して実行する。
        [結果] 定義されたモデルのリストが返却される。
        """
        actual = StringModel.get_all_data('c1161')

        self.assertEquals(5, len(actual))
        for item in actual:
            self.assertTrue(isinstance(item, StringModel))

    def test_get_all_data_02(self):
        """
        [対象] get_all_data() : No.02
        [条件] 無効なレイヤIDを指定して実行する。
        [結果] WebApiErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.WebApiError):
            StringModel.get_all_data('error')

    def test_get_all_data_03(self):
        """
        [対象] get_all_data() : No.03
        [条件] 文字列フィールドを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = StringModel.get_all_data('c1161')

        self.assertEquals('2013/07/19 17:01:02', actual[0].created)
        self.assertEquals('POINT(139.9028991 35.8562708)', actual[0].geo)
        self.assertEquals('流山市役所', actual[0].name)
