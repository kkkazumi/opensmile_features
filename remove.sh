#!/bin/bash

if [ $# -ne 1 ]; then
	echo "指定された引数は$#個です。" 1>&2
	echo "実行するには3個の引数が必要です。" 1>&2
	exit 1
fi
# ヒアドキュメントでメッセージを表示する。
echo $1

sed -i -e '3d' $1
sed -i 's/unknown,//g' $1
