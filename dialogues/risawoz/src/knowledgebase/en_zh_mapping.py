class RisaWOZMapping(object):
    def __init__(self):
        # currently untranslated
        self._risawoz_domain_slot_MAP = {
            '医院': ['区域', '名称', '门诊时间', '挂号时间', 'DSA', '3.0T MRI', '重点科室', '电话', '公交线路', '地铁可达', 'CT', '等级', '性质', '类别', '地址'],
            '天气': ['温度', '目的地', '日期', '城市', '风力风向', '天气', '紫外线强度'],
            '旅游景点': [
                '门票价格',
                '电话号码',
                '菜系',
                '名称',
                '评分',
                '最适合人群',
                '房费',
                '景点类型',
                '房型',
                '推荐菜',
                '消费',
                '开放时间',
                '价位',
                '是否地铁直达',
                '区域',
                '地址',
                '特点',
            ],
            '汽车': [
                '座椅通风',
                '油耗水平',
                '级别',
                '能源类型',
                '名称',
                '价格',
                '驱动方式',
                '所属价格区间',
                '车型',
                '座位数',
                '座椅加热',
                '倒车影像',
                '定速巡航',
                '动力水平',
                '车系',
                '厂商',
            ],
            '火车': ['出发时间', '票价', '目的地', '车型', '舱位档次', '日期', '时长', '到达时间', '车次信息', '出发地', '准点率', '航班信息', '坐席'],
            '电影': ['制片国家/地区', '豆瓣评分', '片名', '主演名单', '具体上映时间', '导演', '片长', '类型', '年代', '主演'],
            '电脑': [
                '价格区间',
                '内存容量',
                '商品名称',
                '显卡型号',
                '裸机重量',
                '价格',
                '品牌',
                '系统',
                'CPU型号',
                '系列',
                '特性',
                '屏幕尺寸',
                '游戏性能',
                '分类',
                '产品类别',
                '待机时长',
                '色系',
                '硬盘容量',
                'CPU',
                '显卡类别',
            ],
            '电视剧': ['制片国家/地区', '豆瓣评分', '片名', '主演名单', '首播时间', '导演', '片长', '集数', '单集片长', '类型', '年代', '主演'],
            '辅导班': [
                '开始日期',
                '老师',
                '上课方式',
                '校区',
                '价格',
                '难度',
                '时段',
                '课时',
                '科目',
                '班号',
                '结束日期',
                '年级',
                '下课时间',
                '教室地点',
                '每周',
                '课次',
                '上课时间',
                '区域',
            ],
            '酒店': ['电话号码', '星级', '名称', '房费', '地址', '地铁是否直达', '房型', '停车场', '推荐菜', '酒店类型', '价位', '是否地铁直达', '区域', '评分'],
            '飞机': ['出发时间', '票价', '温度', '目的地', '起飞时间', '舱位档次', '日期', '城市', '到达时间', '出发地', '准点率', '航班信息', '天气'],
            '餐厅': ['营业时间', '电话号码', '菜系', '名称', '评分', '房费', '人均消费', '推荐菜', '开放时间', '价位', '是否地铁直达', '区域', '地址'],
            '通用': [],
        }

        self._risawoz_domain_MAP = {k: k for k in self._risawoz_domain_slot_MAP.keys()}
        self._risawoz_slot_set = set([v[i] for v in self._risawoz_domain_slot_MAP.values() for i in range(len(v)) if v[i]])
        self._risawoz_slot_MAP = {k: k for k in list(self._risawoz_slot_set)}

        self._risawoz_API_MAP = {
            # currently untranslated
            "天气": "天气",
            "火车": "火车",
            "电脑": "电脑",
            "电影": "电影",
            "辅导班": "辅导班",
            "汽车": "汽车",
            "餐厅": "餐厅",
            "酒店": "酒店",
            "旅游景点": "旅游景点",
            "飞机": "飞机",
            "医院": "医院",
            "电视剧": "电视剧",
            "通用": "通用",
        }

        self._risawoz_ACT_MAP = {
            # untranslated in the original dataset
            'inform': 'inform',
            'general': 'general',
            'greeting': 'greeting',
            'bye': 'bye',
            'request': 'request',
            'recommend': 'recommend',
            'no-offer': 'no-offer',
        }

    def get_mapping(self, enable=False):
        if enable:
            return (
                self._risawoz_domain_slot_MAP,
                self._risawoz_domain_MAP,
                self._risawoz_slot_MAP,
                self._risawoz_API_MAP,
                self._risawoz_ACT_MAP,
            )
        else:
            return None, None, None, None, None
