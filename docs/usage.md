# 使い方

## データの取得（Pythonオブジェクト編）

`pyny.api` モジュール内の各種関数を呼び出すと、Web APIが返却するJSONをPythonオブジェクトに変換した形で取得することができます。
戻り値はリストや辞書になっているので、JSONをパースする手間をかけずに、そのままプログラム内で利用することが可能です。
また、Web APIには存在しない機能についても、いくつか独自実装として提供しています。

```console
>>> from pyny import api
>>> data = api.get_by_id('c1161', 2)
>>>
>>> import pprint
>>> p = pprint.PrettyPrinter()
>>> p.pprint(data)
{'attrs': {'attr0': '市役所・出張所',
           'attr1': '出張所',
           'attr2': 'おおたかの森出張所',
           'attr3': '流山市西初石6-185-2（流山おおたかの森S・C内3階）',
           'attr6': '35.8706965',
           'attr7': '139.9261438',
           'attr8': '04-7154-0333 '},
 'created': '2013/07/19 17:01:02',
 'distance': 0,
 'feature_id': 2,
 'files': {},
 'geometry': 'POINT(139.9261438 35.8706965)',
 'layer_id': 'c1161',
 'mid': 0,
 'moduserid': 0,
 'status': 0,
 'user_id': 307}
>>>
```

`pyny.api` で提供されている関数には下記のものがあります。

### get_by_id(layer_id, feature_id)

指定されたレイヤID、項目IDにマッチするデータを取得します。
レイヤIDについては [流山市オープンデータトライアルWeb APIに関する情報提供ページ](http://ecom-plat.jp/nagareyama/group.php?gid=10446) で公開されているWeb APIリファレンスをご参照ください。

### get_data(layer_id, count)

指定されたレイヤIDにマッチするデータを指定された件数ぶん取得します。
レイヤIDについては [流山市オープンデータトライアルWeb APIに関する情報提供ページ](http://ecom-plat.jp/nagareyama/group.php?gid=10446) で公開されているWeb APIリファレンスをご参照ください。

### get_all_data(layer_id)

指定されたレイヤIDにマッチするすべてのデータを取得します。
レイヤIDについては [流山市オープンデータトライアルWeb APIに関する情報提供ページ](http://ecom-plat.jp/nagareyama/group.php?gid=10446) で公開されているWeb APIリファレンスをご参照ください。

### get_data_count(layer_id)

指定されたレイヤIDにマッチするデータの件数を取得します。
レイヤIDについては [流山市オープンデータトライアルWeb APIに関する情報提供ページ](http://ecom-plat.jp/nagareyama/group.php?gid=10446) で公開されているWeb APIリファレンスをご参照ください。

## データの取得（モデル編）

Web APIの戻り値は（本来は数値や日付であっても）文字列であることが多く、参照する際に型変換をしなければいけないケースが多々あります。
pynyでは、Web APIから取得したデータの入れ物（以下モデル）を定義することで、あらかじめプログラマが指定した型に値を変換する仕組みを提供しています。

```console
>>> from pyny.models import Model
>>> from pyny.fields import DecimalField, StringField
>>>
>>> class SampleModel(Model):
...     layer_id = StringField()
...     longitude = DecimalField('attrs.attr7')
...
>>> data = SampleModel.get_by_id('c1161', 2)
>>> data.layer_id
'c1161'
>>> data.longitude
Decimal('139.9261438')
>>>
```

モデルは `pyny.models.Model` のサブクラスとして定義します。
そのクラスのクラス変数として、 `pyny.fields` モジュールの各種フィールド（後述）を定義してください。
そのフィールド（厳密にはそのクラス変数と同名のインスタンス変数）にWeb APIから取得した値が格納されます。

### データとフィールドのマッピング

各フィールドは、変数名と同名のJSONの項目を参照します。
また、定義時に明示的にJSONの項目名を指定することも可能です。
下記サンプルの `layer_id` 、 `id` には、どちらもJSON上の `'layer_id'` の値が格納されます。

```console
>>> from pyny.models import Model
>>> from pyny.fields import StringField
>>>
>>> class SampleModel(Model):
...     layer_id = StringField()
...     id = StringField('layer_id')
>>>
```

「辞書の中の辞書」のように階層構造になっている項目を参照する場合、各項目の名称を `.` で連結した値を指定してください。

```console
>>> from pyny import api
>>> data = api.get_by_id('c1161', 2)
>>>
>>> import pprint
>>> p = pprint.PrettyPrinter()
>>> p.pprint(data)
{'attrs': {'attr0': '市役所・出張所',
           'attr1': '出張所',
           'attr2': 'おおたかの森出張所',
           'attr3': '流山市西初石6-185-2（流山おおたかの森S・C内3階）',
           'attr6': '35.8706965',
           'attr7': '139.9261438',
           'attr8': '04-7154-0333 '},
 'created': '2013/07/19 17:01:02',
 'distance': 0,
 'feature_id': 2,
 'files': {},
 'geometry': 'POINT(139.9261438 35.8706965)',
 'layer_id': 'c1161',
 'mid': 0,
 'moduserid': 0,
 'status': 0,
 'user_id': 307}
>>>
>>> from pyny.models import Model
>>> from pyny.fields import StringField
>>>
>>> class SampleModel(Model):
...     name = StringField('attrs.attr2')
...
>>> data = SampleModel.get_by_id('c1161', 2)
>>> data.name
'おおたかの森出張所'
>>>
```

### フィールドの種類

モデルにフィールドとして定義できるクラスには下記のものがあります。
いずれも `pyny.fields` モジュールで提供しています。

#### StringField

文字列を表現するフィールドクラスです。
Web APIから取得した値を `str` として格納します。

#### IntegerField

整数を表現するフィールドクラスクラスです。
Web APIから取得した値を `int` として格納します。

#### DecimalField

固定小数点数を表現するフィールドクラスです。
Web APIから取得した値を `decimal.Decimal` として格納します。

#### FloatField

浮動小数点数を表現するフィールドクラスです。
Web APIから取得した値を `float` として格納します。

#### DateField

日付を表現するフィールドクラスです。
Web APIから取得した値を `datetime.date` として格納します。
文字列を日付に変換する際のフォーマットは `%Y/%m/%d` を想定していますが、定義時に任意のフォーマットを指定することもできます。

```console
>>> from pyny.models import Model
>>> from pyny.fields import DateField
>>>
>>> class SampleModel(Model):
...     date1 = DateField()
...     date2 = DateField(fmt='%Y-%m-%d')
...
>>>
```

### DateTimeField

日時を表現するフィールドクラスです。
Web APIから取得した値を `datetime.datetime` として格納します。
文字列を日時に変換する際のフォーマットは `%Y/%m/%d %H:%M:%S` を想定していますが、定義時に任意のフォーマットを指定することもできます。

```console
>>> from pyny.models import Model
>>> from pyny.fields import DateTimeField
>>>
>>> class SampleModel(Model):
...     datetime1 = DateTimeField()
...     datetime2 = DateTimeField(fmt='%Y-%m-%d %H:%M:%S')
...
>>>
```

### データの取得方法

`pyny.models.Model` には下記のクラスメソッドが定義されています。

#### get_by_id(layer_id, feature_id)

指定されたレイヤID、項目IDにマッチするデータを取得します。
レイヤIDについては [流山市オープンデータトライアルWeb APIに関する情報提供ページ](http://ecom-plat.jp/nagareyama/group.php?gid=10446) で公開されているWeb APIリファレンスをご参照ください。

#### get_data(layer_id, count)

指定されたレイヤIDにマッチするデータを指定された件数ぶん取得します。
レイヤIDについては [流山市オープンデータトライアルWeb APIに関する情報提供ページ](http://ecom-plat.jp/nagareyama/group.php?gid=10446) で公開されているWeb APIリファレンスをご参照ください。

#### get_all_data(layer_id)

指定されたレイヤIDにマッチするすべてのデータを取得します。
レイヤIDについては [流山市オープンデータトライアルWeb APIに関する情報提供ページ](http://ecom-plat.jp/nagareyama/group.php?gid=10446) で公開されているWeb APIリファレンスをご参照ください。
