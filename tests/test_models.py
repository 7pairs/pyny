# -*- coding: utf-8 -*-

#
# Copyright 2015-2017 Jun-ya HASEBA
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

import datetime
import decimal
from mock import patch
from unittest import TestCase

from pyny.fields import DateField, DateTimeField, DecimalField, FloatField, IntegerField, StringField
from pyny.models import Model


class StringModel(Model):
    """
    StringFieldをテストするためのモデル。
    """
    created = StringField()
    geo = StringField('geometry')
    name = StringField('attrs.attr2')


class IntegerModel(Model):
    """
    IntegerFieldをテストするためのモデル。
    """
    status = IntegerField()
    id = IntegerField('feature_id')
    attr = IntegerField('attrs.attr0')


class DecimalModel(Model):
    """
    DecimalFieldをテストするためのモデル。
    """
    user_id = DecimalField()
    mod = DecimalField('moduserid')
    latitude = DecimalField('attrs.attr6')


class FloatModel(Model):
    """
    FloatFieldをテストするためのモデル。
    """
    float1 = FloatField()
    float2 = FloatField('float')
    float3 = FloatField('attrs.attr3')


class DateModel(Model):
    """
    DateFieldをテストするためのモデル。
    """
    date1 = DateField()
    date2 = DateField('date')
    date3 = DateField('attrs.attr3')


class DateTimeModel(Model):
    """
    DateTimeFieldをテストするためのモデル。
    """
    date_time1 = DateTimeField()
    date_time2 = DateTimeField('date_time')
    date_time3 = DateTimeField('attrs.attr3')


class ModelTest(TestCase):
    """
    models.Modelに対するテストコード。
    """

    def test_get_by_id_01(self):
        """
        [対象] get_by_id() : No.01
        [条件] 有効なレイヤID、項目IDを指定して実行する。
        [結果] モデルが返却される。
        """
        actual = StringModel.get_by_id('c1161', 3)

        self.assertTrue(isinstance(actual, StringModel))

    def test_get_by_id_02(self):
        """
        [対象] get_by_id() : No.02
        [条件] 有効なレイヤID、無効な項目IDを指定して実行する。
        [結果] Noneが返却される。
        """
        actual = StringModel.get_by_id('c1161', 2015)

        self.assertIsNone(actual)

    def test_get_by_id_03(self):
        """
        [対象] get_by_id() : No.03
        [条件] 無効なレイヤIDを指定して実行する。
        [結果] WebApiErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.WebApiError):
            StringModel.get_by_id('error', 3)

    def test_get_by_id_04(self):
        """
        [対象] get_by_id() : No.04
        [条件] StringFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = StringModel.get_by_id('c1161', 3)

        self.assertEquals('2013/07/19 17:01:02', actual.created)
        self.assertEquals('POINT(139.942968 35.843176)', actual.geo)
        self.assertEquals('東部出張所', actual.name)

    def test_get_by_id_05(self):
        """
        [対象] get_by_id() : No.05
        [条件] IntegerFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = IntegerModel.get_by_id('c1150', 3)

        self.assertEquals(0, actual.status)
        self.assertEquals(3, actual.id)
        self.assertEquals(3, actual.attr)

    def test_get_by_id_06(self):
        """
        [対象] get_by_id() : No.06
        [条件] DecimalFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = DecimalModel.get_by_id('c1161', 3)

        self.assertEquals(decimal.Decimal('307'), actual.user_id)
        self.assertEquals(decimal.Decimal('0'), actual.mod)
        self.assertEquals(decimal.Decimal('35.843176'), actual.latitude)

    @patch('pyny.models.api._get_json')
    def test_get_by_id_07(self, get_json):
        """
        [対象] get_by_id() : No.07
        [条件] FloatFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 3,
            'results': [{
                'float': '123.456',
                'float1': '456.789',
                'attrs': {
                    'attr3': '789.123',
                },
                'feature_id': 1,
            }, {
                'float': '112.233',
                'float1': '445.566',
                'attrs': {
                    'attr3': '778.899',
                },
                'feature_id': 2,
            }, {
                'float': '111.222',
                'float1': '444.555',
                'attrs': {
                    'attr3': '777.888',
                },
                'feature_id': 3,
            }],
        }

        actual = FloatModel.get_by_id('dummy', 2)

        self.assertEquals(445.566, actual.float1)
        self.assertEquals(112.233, actual.float2)
        self.assertEquals(778.899, actual.float3)

    @patch('pyny.models.api._get_json')
    def test_get_by_id_08(self, get_json):
        """
        [対象] get_by_id() : No.08
        [条件] DateFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 1,
            'results': [{
                'date': '2015/02/02',
                'date1': '2015/01/01',
                'attrs': {
                    'attr3': '2015/03/03',
                },
                'feature_id': 1,
            }, {
                'date': '2015/05/05',
                'date1': '2015/04/04',
                'attrs': {
                    'attr3': '2015/06/06',
                },
                'feature_id': 2,
            }, {
                'date': '2015/08/08',
                'date1': '2015/07/07',
                'attrs': {
                    'attr3': '2015/09/09',
                },
                'feature_id': 3,
            }],
        }

        actual = DateModel.get_by_id('dummy', 2)

        self.assertEquals(datetime.date(2015, 4, 4), actual.date1)
        self.assertEquals(datetime.date(2015, 5, 5), actual.date2)
        self.assertEquals(datetime.date(2015, 6, 6), actual.date3)

    @patch('pyny.models.api._get_json')
    def test_get_by_id_09(self, get_json):
        """
        [対象] get_by_id() : No.09
        [条件] DateTimeFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 1,
            'results': [{
                'date_time': '2015/02/02 02:02:02',
                'date_time1': '2015/01/01 01:01:01',
                'attrs': {
                    'attr3': '2015/03/03 03:03:03',
                },
                'feature_id': 1,
            }, {
                'date_time': '2015/05/05 05:05:05',
                'date_time1': '2015/04/04 04:04:04',
                'attrs': {
                    'attr3': '2015/06/06 06:06:06',
                },
                'feature_id': 2,
            }, {
                'date_time': '2015/08/08 08:08:08',
                'date_time1': '2015/07/07 07:07:07',
                'attrs': {
                    'attr3': '2015/09/09 09:09:09',
                },
                'feature_id': 3,
            }],
        }

        actual = DateTimeModel.get_by_id('dummy', 2)

        self.assertEquals(datetime.datetime(2015, 4, 4, 4, 4, 4), actual.date_time1)
        self.assertEquals(datetime.datetime(2015, 5, 5, 5, 5, 5), actual.date_time2)
        self.assertEquals(datetime.datetime(2015, 6, 6, 6, 6, 6), actual.date_time3)

    def test_get_data_01(self):
        """
        [対象] get_data() : No.01
        [条件] 有効なレイヤIDを指定して実行する。
        [結果] モデルのリストが返却される。
        """
        actual = StringModel.get_data('c1161', 3)

        self.assertEquals(3, len(actual))
        for item in actual:
            self.assertTrue(isinstance(item, StringModel))

    def test_get_data_02(self):
        """
        [対象] get_data() : No.02
        [条件] 無効なレイヤIDを指定して実行する。
        [結果] WebApiErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.WebApiError):
            StringModel.get_data('error', 5)

    def test_get_data_03(self):
        """
        [対象] get_data() : No.03
        [条件] StringFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = StringModel.get_data('c1161', 3)

        self.assertEquals('2013/07/19 17:01:02', actual[0].created)
        self.assertEquals('POINT(139.9028991 35.8562708)', actual[0].geo)
        self.assertEquals('流山市役所', actual[0].name)

    def test_get_data_04(self):
        """
        [対象] get_data() : No.04
        [条件] IntegerFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = IntegerModel.get_data('c1150', 3)

        self.assertEquals(0, actual[0].status)
        self.assertEquals(1, actual[0].id)
        self.assertEquals(1, actual[0].attr)

    def test_get_data_05(self):
        """
        [対象] get_data() : No.05
        [条件] DecimalFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = DecimalModel.get_data('c1161', 3)

        self.assertEquals(decimal.Decimal('307'), actual[0].user_id)
        self.assertEquals(decimal.Decimal('0'), actual[0].mod)
        self.assertEquals(decimal.Decimal('35.8562708'), actual[0].latitude)

    @patch('pyny.models.api._get_json')
    def test_get_data_06(self, get_json):
        """
        [対象] get_data() : No.06
        [条件] FloatFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 1,
            'results': [{
                'float': '123.456',
                'float1': '456.789',
                'attrs': {
                    'attr3': '789.123',
                },
            }],
        }

        actual = FloatModel.get_data('dummy', 1)

        self.assertEquals(456.789, actual[0].float1)
        self.assertEquals(123.456, actual[0].float2)
        self.assertEquals(789.123, actual[0].float3)

    @patch('pyny.models.api._get_json')
    def test_get_data_07(self, get_json):
        """
        [対象] get_data() : No.07
        [条件] DateFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 1,
            'results': [{
                'date': '1989/06/23',
                'date1': '1988/10/19',
                'attrs': {
                    'attr3': '2008/11/09',
                },
            }],
        }

        actual = DateModel.get_data('dummy', 1)

        self.assertEquals(datetime.date(1988, 10, 19), actual[0].date1)
        self.assertEquals(datetime.date(1989, 6, 23), actual[0].date2)
        self.assertEquals(datetime.date(2008, 11, 9), actual[0].date3)

    @patch('pyny.models.api._get_json')
    def test_get_data_08(self, get_json):
        """
        [対象] get_data() : No.08
        [条件] DateTimeFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 1,
            'results': [{
                'date_time': '1989/06/23 12:23:34',
                'date_time1': '1988/10/19 01:12:23',
                'attrs': {
                    'attr3': '2008/11/09 23:34:45',
                },
            }],
        }

        actual = DateTimeModel.get_data('dummy', 1)

        self.assertEquals(datetime.datetime(1988, 10, 19, 1, 12, 23), actual[0].date_time1)
        self.assertEquals(datetime.datetime(1989, 6, 23, 12, 23, 34), actual[0].date_time2)
        self.assertEquals(datetime.datetime(2008, 11, 9, 23, 34, 45), actual[0].date_time3)

    def test_get_all_data_01(self):
        """
        [対象] get_all_data() : No.01
        [条件] 有効なレイヤIDを指定して実行する。
        [結果] モデルのリストが返却される。
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
        [条件] StringFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = StringModel.get_all_data('c1161')

        self.assertEquals('2013/07/19 17:01:02', actual[0].created)
        self.assertEquals('POINT(139.9028991 35.8562708)', actual[0].geo)
        self.assertEquals('流山市役所', actual[0].name)

    def test_get_all_data_04(self):
        """
        [対象] get_all_data() : No.04
        [条件] IntegerFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = IntegerModel.get_all_data('c1150')

        self.assertEquals(0, actual[0].status)
        self.assertEquals(1, actual[0].id)
        self.assertEquals(1, actual[0].attr)

    def test_get_all_data_05(self):
        """
        [対象] get_all_data() : No.05
        [条件] DecimalFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        actual = DecimalModel.get_all_data('c1161')

        self.assertEquals(decimal.Decimal('307'), actual[0].user_id)
        self.assertEquals(decimal.Decimal('0'), actual[0].mod)
        self.assertEquals(decimal.Decimal('35.8562708'), actual[0].latitude)

    @patch('pyny.models.api._get_json')
    def test_get_all_data_06(self, get_json):
        """
        [対象] get_all_data() : No.06
        [条件] FloatFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 1,
            'results': [{
                'float': '123.456',
                'float1': '456.789',
                'attrs': {
                    'attr3': '789.123',
                },
            }],
        }

        actual = FloatModel.get_all_data('dummy')

        self.assertEquals(456.789, actual[0].float1)
        self.assertEquals(123.456, actual[0].float2)
        self.assertEquals(789.123, actual[0].float3)

    @patch('pyny.models.api._get_json')
    def test_get_all_data_07(self, get_json):
        """
        [対象] get_all_data() : No.07
        [条件] DateFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 1,
            'results': [{
                'date': '1989/06/23',
                'date1': '1988/10/19',
                'attrs': {
                    'attr3': '2008/11/09',
                },
            }],
        }

        actual = DateModel.get_all_data('dummy')

        self.assertEquals(datetime.date(1988, 10, 19), actual[0].date1)
        self.assertEquals(datetime.date(1989, 6, 23), actual[0].date2)
        self.assertEquals(datetime.date(2008, 11, 9), actual[0].date3)

    @patch('pyny.models.api._get_json')
    def test_get_all_data_08(self, get_json):
        """
        [対象] get_all_data() : No.08
        [条件] DateTimeFieldを持つモデルの当該メソッドを実行する。
        [結果] 各フィールドに値が設定される。
        """
        get_json.return_value = {
            'num': 1,
            'results': [{
                'date_time': '1989/06/23 12:23:34',
                'date_time1': '1988/10/19 01:12:23',
                'attrs': {
                    'attr3': '2008/11/09 23:34:45',
                },
            }],
        }

        actual = DateTimeModel.get_all_data('dummy')

        self.assertEquals(datetime.datetime(1988, 10, 19, 1, 12, 23), actual[0].date_time1)
        self.assertEquals(datetime.datetime(1989, 6, 23, 12, 23, 34), actual[0].date_time2)
        self.assertEquals(datetime.datetime(2008, 11, 9, 23, 34, 45), actual[0].date_time3)
