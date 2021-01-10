import etcd3
import sys

if __name__ == "__main__":
	etcd = etcd3.client()
	print(etcd.get('DailyReportPort'))

