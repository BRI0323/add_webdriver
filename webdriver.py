import requests
from bs4 import BeautifulSoup

def get_latest_chromedriver_version():
    try:
        # Chrome Driverの最新バージョン情報があるページ
        url = 'https://sites.google.com/chromium.org/driver/'
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードが200 OK以外はエラーを発生させる

        # ページの内容を解析する
        soup = BeautifulSoup(response.text, 'html.parser')

        # 特定の要素（ここでは、最新バージョン番号が含まれるであろう要素）を検索する
        # 注意: ウェブページの構造が変わると、このセレクタも更新する必要があります
        version_element = soup.select_one('a[href*="/chromedriver/downloads"]')
        if version_element:
            # テキストからバージョン番号を取得する
            version = version_element.text.strip()
            return version
        else:
            print("最新バージョンの情報が見つかりませんでした。")
            return None

    except requests.RequestException as e:
        print(f"リクエスト中にエラーが発生しました: {e}")
        return None
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
        return None

# 関数を呼び出して最新バージョンを取得
latest_version = get_latest_chromedriver_version()
if latest_version:
    print(f"最新のChromeDriverバージョン: {latest_version}")
