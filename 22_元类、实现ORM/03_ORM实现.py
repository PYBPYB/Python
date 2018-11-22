class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是指定的 StringField 或者 IntegerField 的实例对象
            if isinstance(v, tuple):
                # print("found mappings:%s==>%s" % (k, v))
                mappings[k] = v
        # 删除这些已经在字典里存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将之前的uid/name/emall/password以及对应的对象引用、类名字
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMetaclass):
    # 当指定元类的时候，以上的类属性将不在类中，
    # 而是在 __mappings__ 属性指定的字典中存储
    # 以上User类中有
    # __mappings__ = {
    #     uid = ('uid', "int unsigned")
    #     name = ('username', "varchar(30)")
    #     email = ('email', "varchar(30)")
    #     password = ('password', "varchar(30)")
    # }
    # __table__ = "User"

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
            # self.name = value

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        # mysql > insert into User(uid, username, email, password)
        #                   values(12345, 小潘, None, 1314);

        # sql = 'insert into %s(%s) values(%s);' % (self.__table__,
        #                                           ','.join(fields),
        #                                           ','.join([str(i) for i in args]))


        args_list = list()
        for temp in args:
            if isinstance(temp, int):
                args_list.append(str(temp))
            elif isinstance(temp, str):
                args_list.append("""'%s'""" % temp)
        sql = 'insert into %s(%s) values(%s);' % (self.__table__,
                                                  ','.join(fields),
                                                  ','.join(args_list))
        print("mysql>%s" % sql)


class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")

u = User(uid=12345,
         name='小潘',
         email='2679771017@qq.com',
         password='1314')
u.save()

u = User(uid=123456,
         name='小李',
         email='xxxxx@qq.com',
         password='sdfhieu')
u.save()

