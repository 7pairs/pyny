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


class StringFieldTest(TestCase):
    """
    StringFieldに対するテストコード。
    """

    def _get_target_object(self, *args, **kwargs):
        """
        テスト対象のオブジェクトを取得する。

        :param args: 可変長引数
        :type args: tuple
        :param kwargs: キーワード引数
        :type kwargs: dict
        :return: テスト対象のフィールドオブジェクト
        :rtype: pyny.fields.StringField
        """
        # テスト対象のオブジェクトを生成する
        from pyny.fields import StringField
        return StringField(*args, **kwargs)

    def test_init_01(self):
        """
        [対象] __init__() : No.01
        [条件] キーを指定して実行する。
        [結果] プロパティが設定される。
        """
        target = self._get_target_object('string_field')

        self.assertEqual('string_field', target.name)

    def test_init_02(self):
        """
        [対象] __init__() : No.02
        [条件] キーを指定せずに実行する。
        [結果] プロパティに何も設定されない。
        """
        target = self._get_target_object()

        self.assertIsNone(target.name)

    def test_convert_01(self):
        """
        [対象] convert() : No.01
        [条件] 文字列を指定して実行する。
        [結果] 指定した値がそのまま返却される。
        """
        target = self._get_target_object()
        actual = target.convert('string_value')

        self.assertEqual('string_value', actual)

    def test_convert_02(self):
        """
        [対象] convert() : No.02
        [条件] 数値を指定して実行する。
        [結果] 指定した値が文字列化して返却される。
        """
        target = self._get_target_object()
        actual = target.convert(13)

        self.assertEqual('13', actual)
