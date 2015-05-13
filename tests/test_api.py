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

    def test_get_all_data_01(self):
        """
        [対象] get_all_data() : No.01
        [条件] 有効なレイヤIDを指定して実行する。
        [結果] JSONを変換した辞書が返却される。
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
                'attr7': '139.9028991'
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
                'attr7': '139.9261438'
            },
            'feature_id': 2,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.9261438 35.8706965)'
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
                'attr7': '139.942968'
            },
            'feature_id': 3,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.942968 35.843176)'
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
                'attr7': '139.9107444'
            },
            'feature_id': 4,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.9107444 35.8976138)'
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
                'attr7': '139.9017914'
            },
            'feature_id': 5,
            'moduserid': 0,
            'layer_id': 'c1161',
            'user_id': 307,
            'mid': 0,
            'geometry': 'POINT(139.9017914 35.8388429)'
        }]

        from pyny import api
        actual = api.get_all_data('c1161')

        self.assertEqual(expected, actual)

    def test_get_all_data_02(self):
        """
        [対象] get_all_data() : No.02
        [条件] 無効なレイヤIDを指定して実行する。
        [結果] PynyErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.PynyError):
            api.get_all_data('error')

    def test_get_item_count_01(self):
        """
        [対象] get_item_count() : No.01
        [条件] 有効なレイヤIDを指定して実行する。
        [結果] 件数が返却される。
        """
        from pyny import api
        actual = api.get_item_count('c1120')

        self.assertEqual(71, actual)

    def test_get_item_count_02(self):
        """
        [対象] get_item_count() : No.02
        [条件] 無効なレイヤIDを指定して実行する。
        [結果] PynyErrorが送出される。
        """
        from pyny import api
        with self.assertRaises(api.PynyError):
            api.get_item_count('error')
