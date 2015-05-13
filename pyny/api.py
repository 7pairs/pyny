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

import json
from urllib.error import HTTPError
from urllib.request import urlopen


# 流山市オープンデータWeb APIのURL
WEB_API_URL = 'http://nagareyama.ecom-plat.jp/map/api/feature/8?layers=%s&pagenum=%d'


class PynyError(Exception):
    """
    当ライブラリで想定していない入出力があったことを示す例外。
    """


def get_all_data(layer_id):
    """
    指定されたレイヤIDにマッチするすべてのデータを取得する。

    :param layer_id: レイヤID
    :type layer_id: str
    :return: 辞書にまとめられたデータのリスト
    :rtype: list
    :raises PynyError: Web APIへの問い合わせが正常に完了しなかった
    """
    # データの件数を取得する
    data_count = get_data_count(layer_id)

    # 流山市オープンデータWeb APIに問い合わせを行う
    try:
        with urlopen(WEB_API_URL % (layer_id, data_count)) as response:
            encoding = response.headers.get_content_charset() or 'utf-8'
            data = json.loads(response.read().decode(encoding, 'ignore'))
            return data['results']
    except HTTPError:
        raise PynyError()


def get_data_count(layer_id):
    """
    指定されたレイヤIDにマッチするデータの件数を取得する。

    :param layer_id: レイヤID
    :type layer_id: str
    :return: データの件数
    :rtype: int
    :raises PynyError: Web APIへの問い合わせが正常に完了しなかった
    """
    # 流山市オープンデータWeb APIに問い合わせを行う
    try:
        with urlopen(WEB_API_URL % (layer_id, 1)) as response:
            encoding = response.headers.get_content_charset() or 'utf-8'
            data = json.loads(response.read().decode(encoding, 'ignore'))
            return int(data['num'])
    except HTTPError:
        raise PynyError()
