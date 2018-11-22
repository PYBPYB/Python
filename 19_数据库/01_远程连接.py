from pymysql import connect


class JD(object):
    def __init__(self):
        self.conn = connect(host='localhost',
                            port=3306,
                            user='root',
                            password='1314',
                            database='jing_dong',
                            charset='utf8')
        self.cursor = self.conn.cursor()  # 获取一个游标def

    def __del__(self):
        self.conn.close()
        self.cursor.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_goods(self):
        """显示所有商品"""
        self.execute_sql('select * from goods;')

    def show_all_cates(self):
        """现实所有的商品分类信息"""
        self.execute_sql("select * from goods_cstes;")

    def show_all_brands(self):
        """现实所有的商品品牌分类"""
        self.execute_sql('select * from goods_brands;')

    @staticmethod
    def print_menu():
        print("-----京东商城-----")
        print("1、所有的商品")
        print("2、所有的商品分类")
        print("3、所有的商品品牌分类")
        return input("请输入您要进行的操作序号:")

    def run(self):
        while True:
            num = self.print_menu()

            if num == '1':
                self.show_all_goods()
            elif num == '2':
                self.show_all_cates()
            elif num == '3':
                self.show_all_brands()
            else:
                print("输入错误，请重新输入 。。。")


def main():
    # 1、创建京东商城对象
    jd = JD()
    # 2、调用对象的 run 方法
    jd.run()


if __name__ == '__main__':
    main()