from datas.connection_datas import ConnectionDatas


class TestPageLoad:

    @staticmethod
    def test_pageload(browser, hh_page):
        for page in ConnectionDatas.PAGE_ADDRESSES:
            hh_page.go_to_page(page)
