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

    def test_get_by_id_01(self):
        """
        [対象] get_by_id() : No.01
        [条件] 有効なレイヤID、項目IDを指定して実行する。
        [結果] JSONを変換した辞書が返却される。
        """
        expected = {
            'files': {},
            'distance': 0,
            'status': 0,
            'created': '2013/07/19 17:01:02',
            'attrs': {
                'attr0': '市役所・出張所',
                'attr2': 'おおたかの森出張所',
                'attr1': '出張所',
                'attr3': '流山市西初石6-185-2（流山おおたかの森S・C内3階）',
                'attr6': '35.8706965',
                'attr8': '04-7154-0333 ',
                'attr7': '139.9261438',
            },
            'feature_id': 2,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.9261438 35.8706965)',
        }

        from pyny import api
        actual = api.get_by_id('c1161', 2)

        self.assertEqual(expected, actual)

    def test_get_by_id_02(self):
        """
        [対象] get_by_id() : No.02
        [条件] 有効なレイヤID、無効な項目IDを指定して実行する。
        [結果] Noneが返却される。
        """
        from pyny import api
        actual = api.get_by_id('c1161', 2015)

        self.assertIsNone(actual)

    def test_get_by_id_03(self):
        """
        [対象] get_by_id() : No.03
        [条件] 無効なレイヤIDを指定して実行する。
        [結果] WebApiErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.WebApiError):
            api.get_by_id('error', 2)

    def test_get_all_data_01(self):
        """
        [対象] get_all_data() : No.01
        [条件] 有効なレイヤIDを指定して実行する。
        [結果] JSONを変換した辞書のリストが返却される。
        """
        expected = [{
            'files': {},
            'distance': 0,
            'status': 0,
            'created': '2013/07/19 17:01:02',
            'attrs': {
                'attr0': '市役所・出張所',
                'attr2': '流山市役所',
                'attr1': '市役所',
                'attr3': '流山市平和台1\u20101\u20101',
                'attr6': '35.8562708',
                'attr8': '04-7158-1111',
                'attr7': '139.9028991',
            },
            'feature_id': 1,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.9028991 35.8562708)',
        }, {
            'files': {},
            'distance': 0,
            'status': 0,
            'created': '2013/07/19 17:01:02',
            'attrs': {
                'attr0': '市役所・出張所',
                'attr2': 'おおたかの森出張所',
                'attr1': '出張所',
                'attr3': '流山市西初石6-185-2（流山おおたかの森S・C内3階）',
                'attr6': '35.8706965',
                'attr8': '04-7154-0333 ',
                'attr7': '139.9261438',
            },
            'feature_id': 2,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.9261438 35.8706965)',
        }, {
            'files': {},
            'distance': 0,
            'status': 0,
            'created': '2013/07/19 17:01:02',
            'attrs': {
                'attr0': '市役所・出張所',
                'attr2': '東部出張所',
                'attr1': '出張所',
                'attr3': '流山市名都借314',
                'attr6': '35.843176',
                'attr8': '04-7144-2175',
                'attr7': '139.942968',
            },
            'feature_id': 3,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.942968 35.843176)',
        }, {
            'files': {},
            'distance': 0,
            'status': 0,
            'created': '2013/07/19 17:01:02',
            'attrs': {
                'attr0': '市役所・出張所',
                'attr2': '江戸川台駅前出張所',
                'attr1': '出張所',
                'attr3': '流山市江戸川台東1\u20104（JA流山市ビル内）',
                'attr6': '35.8976138',
                'attr8': '04-7152-3132',
                'attr7': '139.9107444',
            },
            'feature_id': 4,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.9107444 35.8976138)',
        }, {
            'files': {},
            'distance': 0,
            'status': 0,
            'created': '2013/07/19 17:01:02',
            'attrs': {
                'attr0': '市役所・出張所',
                'attr2': '南流山出張所',
                'attr1': '出張所',
                'attr3': '流山市南流山3\u20103\u20101（南流山センター内）',
                'attr6': '35.8388429',
                'attr8': '04-7159-4512',
                'attr7': '139.9017914',
            },
            'feature_id': 5,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.9017914 35.8388429)',
        }]

        from pyny import api
        actual = api.get_all_data('c1161')

        self.assertEqual(expected, actual)

    def test_get_all_data_02(self):
        """
        [対象] get_all_data() : No.02
        [条件] 無効なレイヤIDを指定して実行する。
        [結果] WebApiErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.WebApiError):
            api.get_all_data('error')

    def test_get_data_count_01(self):
        """
        [対象] get_data_count() : No.01
        [条件] 有効なレイヤIDを指定して実行する。
        [結果] データ件数が返却される。
        """
        from pyny import api
        actual = api.get_data_count('c1120')

        self.assertEqual(71, actual)

    def test_get_data_count_02(self):
        """
        [対象] get_data_count() : No.02
        [条件] 無効なレイヤIDを指定して実行する。
        [結果] WebApiErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.WebApiError):
            api.get_data_count('error')

    def test_get_json_01(self):
        """
        [対象] _get_json() : No.01
        [条件] 有効なURLを指定して実行する。
        [結果] JSONを変換したPythonオブジェクトが返却される。
        """
        expected = {
            'num': 100,
            'results': [{
                'files': {},
                'distance': 0,
                'status': 0,
                'created': '2013/07/19 16:37:17',
                'attrs': {
                    'attr9': '',
                    'attr10': '',
                    'attr0': '1',
                    'attr11': '',
                    'attr12': '',
                    'attr2': '流山市西深井829他',
                    'attr1': '利根運河',
                    'attr6': '139.902901',
                    'attr5': '35.915248',
                    'attr8': '明治時代に開削された江戸川と利根川を結ぶ延長9キロメートルの人工水路で、開削にあたってはオランダ人土木技師のムルデルが起用された。現在は市民の憩いの場として、運河水辺公園、運河緑道が整備されている。',
                    'attr7': '東武野田線運河駅徒歩4分',
                },
                'feature_id': 1,
                'moduserid': 0,
                'layer_id': 'c1150',
                'user_id': 307,
                'mid': 0,
                'geometry': 'POINT(139.902901 35.915248)',
            }],
        }

        from pyny import api
        actual = api._get_json('http://nagareyama.ecom-plat.jp/map/api/feature/8?layers=c1150&pagenum=1')
        del(actual['_timestamp'])    # 実行するたびに値が変わってしまうためテスト対象外とする

        self.assertEqual(expected, actual)

    def test_get_json_02(self):
        """
        [対象] _get_json() : No.02
        [条件] 無効なURLを指定して実行する。
        [結果] WebApiErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.WebApiError):
            api._get_json('error')

    def test_get_json_03(self):
        """
        [対象] _get_json() : No.03
        [条件] JSONを返却しないURLを指定して実行する。
        [結果] WebApiErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.WebApiError):
            api._get_json('http://thunder-claw.com/')
