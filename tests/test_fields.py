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

import decimal
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


class IntegerFieldTest(TestCase):
    """
    IntegerFieldに対するテストコード。
    """

    def _get_target_object(self, *args, **kwargs):
        """
        テスト対象のオブジェクトを取得する。

        :param args: 可変長引数
        :type args: tuple
        :param kwargs: キーワード引数
        :type kwargs: dict
        :return: テスト対象のフィールドオブジェクト
        :rtype: pyny.fields.IntegerField
        """
        # テスト対象のオブジェクトを生成する
        from pyny.fields import IntegerField
        return IntegerField(*args, **kwargs)

    def test_init_01(self):
        """
        [対象] __init__() : No.01
        [条件] キーを指定して実行する。
        [結果] プロパティが設定される。
        """
        target = self._get_target_object('integer_field')

        self.assertEqual('integer_field', target.name)

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
        [条件] 整数を指定して実行する。
        [結果] 指定した値がそのまま返却される。
        """
        target = self._get_target_object()
        actual = target.convert(35)

        self.assertEqual(35, actual)

    def test_convert_02(self):
        """
        [対象] convert() : No.02
        [条件] 文字列を指定して実行する。
        [結果] 指定した値が整数化して返却される。
        """
        target = self._get_target_object()
        actual = target.convert('32')

        self.assertEqual(32, actual)

    def test_convert_03(self):
        """
        [対象] convert() : No.03
        [条件] 整数化できない文字列を指定して実行する。
        [結果] ValueErrorが送出される。
        """
        target = self._get_target_object()
        with self.assertRaises(ValueError):
            target.convert('error')


class DecimalFieldTest(TestCase):
    """
    DecimalFieldに対するテストコード。
    """

    def _get_target_object(self, *args, **kwargs):
        """
        テスト対象のオブジェクトを取得する。

        :param args: 可変長引数
        :type args: tuple
        :param kwargs: キーワード引数
        :type kwargs: dict
        :return: テスト対象のフィールドオブジェクト
        :rtype: pyny.fields.DecimalField
        """
        # テスト対象のオブジェクトを生成する
        from pyny.fields import DecimalField
        return DecimalField(*args, **kwargs)

    def test_init_01(self):
        """
        [対象] __init__() : No.01
        [条件] キーを指定して実行する。
        [結果] プロパティが設定される。
        """
        target = self._get_target_object('decimal_field')

        self.assertEqual('decimal_field', target.name)

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
        [条件] 固定小数点数を指定して実行する。
        [結果] 指定した値がそのまま返却される。
        """
        target = self._get_target_object()
        actual = target.convert(decimal.Decimal('3.14'))

        self.assertEqual(decimal.Decimal('3.14'), actual)

    def test_convert_02(self):
        """
        [対象] convert() : No.02
        [条件] 文字列を指定して実行する。
        [結果] 指定した値が数値化して返却される。
        """
        target = self._get_target_object()
        actual = target.convert('2.71828')

        self.assertEqual(decimal.Decimal('2.71828'), actual)

    def test_convert_03(self):
        """
        [対象] convert() : No.03
        [条件] 数値化できない文字列を指定して実行する。
        [結果] InvalidOperationが送出される。
        """
        target = self._get_target_object()
        with self.assertRaises(decimal.InvalidOperation):
            target.convert('error')


class FloatFieldTest(TestCase):
    """
    FloatFieldに対するテストコード。
    """

    def _get_target_object(self, *args, **kwargs):
        """
        テスト対象のオブジェクトを取得する。

        :param args: 可変長引数
        :type args: tuple
        :param kwargs: キーワード引数
        :type kwargs: dict
        :return: テスト対象のフィールドオブジェクト
        :rtype: pyny.fields.FloatField
        """
        # テスト対象のオブジェクトを生成する
        from pyny.fields import FloatField
        return FloatField(*args, **kwargs)

    def test_init_01(self):
        """
        [対象] __init__() : No.01
        [条件] キーを指定して実行する。
        [結果] プロパティが設定される。
        """
        target = self._get_target_object('float_field')

        self.assertEqual('float_field', target.name)

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
        [条件] 浮動小数点数を指定して実行する。
        [結果] 指定した値がそのまま返却される。
        """
        target = self._get_target_object()
        actual = target.convert(3.14)

        self.assertEqual(3.14, actual)

    def test_convert_02(self):
        """
        [対象] convert() : No.02
        [条件] 文字列を指定して実行する。
        [結果] 指定した値が数値化して返却される。
        """
        target = self._get_target_object()
        actual = target.convert('2.71828')

        self.assertEqual(2.71828, actual)

    def test_convert_03(self):
        """
        [対象] convert() : No.03
        [条件] 数値化できない文字列を指定して実行する。
        [結果] ValueErrorが送出される。
        """
        target = self._get_target_object()
        with self.assertRaises(ValueError):
            target.convert('error')
