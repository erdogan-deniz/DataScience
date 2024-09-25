# Data for parsing:
peak_hour_url: str = "https://www.atsenergo.ru/dload/calcfacthour_regions/"

peak_hour_request_headers: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " +
                  "Chrome/126.0.0.0 Safari/537.36 SberBrowser/18.0.0.0",
    "Connection": "keep-alive"
}

peak_hour_subjs_tickets: dict = {
    # (ООО, ОАО, ПАО, АО, ЗАО, МУП, МП, ...):

    # Алтайэнергосбыт, Алтайкрайэнерго, БГЭС, Барнаульская горэлектросеть, Заринская горэлектросеть, Оборонэнергосбыт:
    "Алтайский край": [
        "ALTAENSB_01_calcfacthour", "ALTAIKEN_01_calcfacthour",
        "BARNGORS_01_calcfacthour", "OBORONSB_01_calcfacthour",
        "ZARINGES_01_calcfacthour"
    ],

    # Архангельская сбытовая компания, Архэнергосбыт, МРСК Северо-Запада, ТГК-2 Энергосбыт:
    "Архангельская область": [
        "ARHENERG_11_calcfacthour", "MRSKSEVZ_11_calcfacthour",
        "TGC2ENSB_11_calcfacthour"
    ],

    # Астраханская энергосбытовая компания, РУСЭНЕРГОСБЫТ, Оборонэнергосбыт:
    "Астраханская область": [
        "ASTRHENE_12_calcfacthour", "RUSENSBI_12_calcfacthour",
        "OBORONSB_12_calcfacthour"
    ],

    # "Белгородэнергосбыт, Оборонэнергосбыт:
    "Белгородская область": ["BELGOREN_14_calcfacthour", "OBORONSB_14_calcfacthour"],

    # Газпром энергосбыт Брянск, ТЭК-Энерго, Оборонэнергосбыт, МРСК Центра, Брянскэнергосбыт:
    "Брянская область": [
        "TEKENERG_15_calcfacthour", "TEKENERG_15_calcfacthour",
        "OBORONSB_15_calcfacthour", "MRSKCENT_15_calcfacthour",
        "BRYANENE_15_calcfacthour"
    ],

    # ЭСВ, РУСЭНЕРГОСБЫТ, ЭнергосбыТ Плюс, ВКС, МРСК Центра и Приволжья, Владимирские коммунальные системы,
    # Владимирэнергосбыт, Оборонэнергосбыт:
    "Владимирская область": [
        "ESKVOLGA_17_calcfacthour", "RUSENSBI_17_calcfacthour",
        "ORENBENE_17_calcfacthour", "VLADKOMS_17_calcfacthour",
        "MRSKCPRV_17_calcfacthour", "VLADIMEN_17_calcfacthour",
        "OBORONSB_17_calcfacthour"
    ],

    # РУСЭНЕРГОСБЫТ, Волгоградэнергосбыт, Оборонэнергосбыт, ВОЭС:
    "Волгоградская область": [
        "RUSENSBI_18_calcfacthour", "VOLGOGEN_18_calcfacthour",
        "OBORONSB_18_calcfacthour", "VOLGOBEL_18_calcfacthour"
    ],

    # ССК, МРСК Северо-Запада, Вологдаэнергосбыт, Оборонэнергосбыт:
    "Вологодская область": [
        "NORDSBYT_19_calcfacthour", "MRSKSEVZ_19_calcfacthour",
        "VOLOGENE_19_calcfacthour", "OBORONSB_19_calcfacthour"
    ],

    # БЭСО, ТНС энерго Воронеж, Борисоглебского городского округа Воронежской области, Оборонэнергосбыт,
    # Воронежская энергосбытовая компания:
    "Воронежская область": [
        "MPBORISO_20_calcfacthour", "VORNEGEN_20_calcfacthour",
        "OBORONSB_20_calcfacthour"
    ],

    # СЕВЭНЕРГОСБЫТ:
    "Город Севастополь": ["SEVENSBT_67_calcfacthour"],

    # Читаэнергосбыт, Оборонэнергосбыт:
    "Забайкальский край": ["CHITAENE_76200_calcfacthour", "OBORONSB_76200_calcfacthour"],

    # Ивановоэнергосбыт, Энергосбыт Плюс, ЭСК Гарант, Оборонэнергосбыт, МРСК Центра и Приволжья, Энергосетевая компания:
    "Ивановская область": [
        "IVENERSK_24_calcfacthour", "ORENBENE_24_calcfacthour",
        "ESKGARAN_24_calcfacthour", "OBORONSB_24_calcfacthour",
        "MRSKCPRV_24_calcfacthour"
    ],

    # Иркутскэнергосбыт, РУСЭНЕРГОСБЫТ, Витимэнергосбыт, Оборонэнергосбыт:
    "Иркутская область": [
        "IRKUTSBT_25_calcfacthour", "RUSENSBI_25_calcfacthour",
        "VITIMENS_25_calcfacthour", "OBORONSB_25_calcfacthour"
    ],

    # Россети Северный Кавказ, Каббалкэнерго:
    "Кабардино-Балкарская Республика": ["MRSKSKAV_83_calcfacthour", "KABBAGEN_83_calcfacthour"],

    # Янтарьэнергосбыт, Оборонэнергосбыт:
    "Калининградская область": ["YANTSBYT_27_calcfacthour", "OBORONSB_27_calcfacthour"],

    # Калужская сбытовая компания, Оборонэнергосбыт:
    "Калужская область": ["KALUGENE_29_calcfacthour", "OBORONSB_29_calcfacthour"],

    # Россети Северный Кавказ, Карачаево-Черкесскэнерго:
    "Карачаево-Черкесская Республика": ["MRSKSKAV_91_calcfacthour", "KCHERKEN_91_calcfacthour"],

    # Кузбассэнергосбыт, Металлэнергофинанс, Оборонэнергосбыт:
    "Кемеровская область": [
        "KUZBSBYT_32_calcfacthour", "METALENE_32_calcfacthour",
        "OBORONSB_32_calcfacthour"
    ],

    # ЭнергосбыТ Плюс, РУСЭНЕРГОСБЫТ, Оборонэнергосбыт, Кировэнергосбыт:
    "Кировская область": [
        "ORENBENE_33_calcfacthour", "RUSENSBI_33_calcfacthour",
        "OBORONSB_33_calcfacthour", "KIROVENE_33_calcfacthour"
    ],

    # Костромская сбытовая компания, РУСЭНЕРГОСБЫТ, Оборонэнергосбыт:
    "Костромская область": [
        "KOSTRENE_34_calcfacthour", "RUSENSBI_34_calcfacthour",
        "OBORONSB_34_calcfacthour"
    ],

    # ТНС энерго Кубань, НЭСК, Кубаньэнергосбыт, Оборонэнергосбыт:
    "Краснодарский край": [
        "KUBANESK_03_calcfacthour", "NESKKRSN_03_calcfacthour",
        "OBORONSB_03_calcfacthour"
    ],

    # Красноярскэнергосбыт, Оборонэнергосбыт:
    "Красноярский край": ["KRASNOEN_04_calcfacthour", "OBORONSB_04_calcfacthour"],

    # ЭК Восток, Оборонэнергосбыт, Энергосбыт:
    "Курганская область": [
        "ESVOSTOK_37_calcfacthour", "OBORONSB_37_calcfacthour",
        "KURGENRG_37_calcfacthour"
    ],

    # АтомЭнергоСбыт, РЭК, Оборонэнергосбыт, МРСК Центра, Курскрегионэнергосбыт:
    "Курская область": [
        "ATOMSBYT_38_calcfacthour", "REKKURSK_38_calcfacthour",
        "OBORONSB_38_calcfacthour", "MRSKCENT_38_calcfacthour",
        "KURSKENE_38_calcfacthour"
    ],

    # Петербургская сбытовая компания, РКС-энерго, Русэнергосбыт, Оборонэнергосбыт, ЭНЕРГИЯ ХОЛДИНГ, 470 ЭС:
    "Ленинградская область": [
        "LENENERG_41_calcfacthour", "RKSENERG_41_calcfacthour",
        "RUSENSBI_41_calcfacthour", "OBORONSB_41_calcfacthour",
        "ENERHOLD_41_calcfacthour", "OAO470ES_41_calcfacthour"
    ],

    # НОВИТЭН, ЛЭСК, ГЭСК, Оборонэнергосбыт:
    "Липецкая область": [
        "GORODESK_42_calcfacthour", "LIPECKEN_42_calcfacthour",
        "OBORONSB_42_calcfacthour"
    ],

    # БЭЛС, РУСЭНЕРГОСБЫТ, ЭНЕРГОСБЫТХОЛДИНГ, Мосэнергосбыт, Электросеть, ИЭК, СКЛ, Объединение истринские,
    # Троицкая электросеть, Россети Московский регион, МОЭСК, КЭС, Ивантеевские, Королевская электросеть,
    # Оборонэнергосбыт:
    "Московская область": [
        "BALASHEL_46_calcfacthour", "RUSENSBI_46_calcfacthour",
        "RUSENSBM_46_calcfacthour", "MOSENERG_46_calcfacthour",
        "ELSETMYT_46_calcfacthour", "IVELSETI_46_calcfacthour",
        "KOROLSET_46_calcfacthour", "ISTRSETI_46_calcfacthour",
        "TROIELST_46_calcfacthour", "MOSOBCOM_46_calcfacthour",
        "KRASNGOR_46_calcfacthour", "KOROLSET_46_calcfacthour",
        "OBORONSB_46_calcfacthour"
    ],

    # Арктик-энерго, АтомЭнергоСбыт, РУСЭНЕРГОСБЫТ, МРСК Северо-Запада, Колэнергосбыт:
    "Мурманская область": [
        "ARCTIKEN_47_calcfacthour", "ATOMSBYT_47_calcfacthour",
        "RUSENSBI_47_calcfacthour", "MRSKSEVZ_47_calcfacthour",
        "KOLENERG_47_calcfacthour"
    ],

    # ТНС энерго НН, Волгаэнергосбыт, РУСЭНЕРГОСБЫТ, Обеспечение РФЯЦ-ВНИИЭФ, Оборонэнергосбыт:
    "Нижегородская область": [
        "NIGNOVEN_22_calcfacthour", "RUSENSBI_22_calcfacthour",
        "VOLGAESB_22_calcfacthour", "OBESPRFC_22_calcfacthour",
        "OBORONSB_22_calcfacthour"
    ],

    # ТНС энерго Великий Новгород, Оборонэнергосбыт, МРСК Северо-Запада:
    "Новгородская область": [
        "GARENERC_49_calcfacthour", "OBORONSB_49_calcfacthour",
        "MRSKSEVZ_49_calcfacthour", "NOVGSBYT_49_calcfacthour",
        "NOVGOREN_49_calcfacthour"
    ],

    # Новосибирскэнерго, СибирьЭнерго:
    "Новосибирская область": ["SBRENERG_50_calcfacthour"],

    # ОЭК, Петербуская сбытовая, Оборонэнергосбыт, МРСК Сибири, Омскэнергосбыт:
    "Омская область": [
        "OMSKENEC_52_calcfacthour", "LENENERG_52_calcfacthour",
        "OBORONSB_52_calcfacthour", "MRSKSIBR_52_calcfacthour",
        "OMSKENER_52_calcfacthour"
    ],

    # Восток, РУСЭНЕРГОСБЫТ, ЭнергосбыТ Плюс, Оренбургсельэнергосбыт, Оборонэнергосбыт, Оренбургэнергосбыт:
    "Оренбургская область": [
        "ESVOSTOK_53_calcfacthour", "RUSENSBI_53_calcfacthour",
        "ORENBENE_53_calcfacthour", "ORSELSBT_53_calcfacthour",
        "OBORONSB_53_calcfacthour"
    ],

    # ИНТЕР РАО - Орловский энергосбыт, Оборонэнергосбыт, МРСК Центра, Орелэнергосбыт:
    "Орловская область": [
        "IRAORLSB_54_calcfacthour", "OBORONSB_54_calcfacthour",
        "MRSKCENT_54_calcfacthour", "ORELENER_54_calcfacthour"
    ],

    # ТНС энерго Пенза, Энерготрейдинг, МРСК Волги, Пензаэнергосбыт:
    "Пензенская область": [
        "ENTREDIN_56_calcfacthour", "MRSKVOLG_56_calcfacthour",
        "PENZAENE_56_calcfacthour"
    ],

    # Пермэнергосбыт, Оборонэнергосбыт:
    "Пермский край": ["PERMENER_57_calcfacthour", "OBORONSB_57_calcfacthour"],

    # Псковэнергосбыт, Оборонэнергосбыт:
    "Псковская область": ["PSKOVENE_58_calcfacthour", "OBORONSB_58_calcfacthour"],

    # Алтайэнергосбыт:
    "Республика Алтай": ["ALTAENSB_84_calcfacthour"],

    # ЭСКБ, Оборонэнергосбыт:
    "Республика Башкортостан": ["BASHKESK_80_calcfacthour", "OBORONSB_80_calcfacthour"],

    # Читаэнергосбыт, Бурятэнергосбыт, МРСК Сибири:
    "Республика Бурятия": [
        "CHITAENE_81_calcfacthour", "MRSKSIBR_81_calcfacthour",
        "BURYATEN_81_calcfacthour"
    ],

    # Россети Северный Кавказ, Дагестанская энергосбытовая компания:
    "Республика Дагестан": ["MRSKSKAV_82_calcfacthour", "DAGESBYT_82_calcfacthour"],

    # Россети Северный Кавказ, МРСК Северного Кавказа, Ингушэнерго:
    "Республика Ингушетия": [
        "MRSKSKAV_26_calcfacthour", "MRSKSKAV_26_calcfacthour",
        "INGUSHEN_26_calcfacthour"
    ],

    # Читаэнергосбыт, Россети Юг, Калмэнергосбыт, ЮМЭК, МРСК Юга:
    "Республика Калмыкия": [
        "CHITAENE_85_calcfacthour", "MRSKYUGG_85_calcfacthour",
        "KALMENER_85_calcfacthour", "UZMEZREG_85_calcfacthour"
    ],

    # Энергокомфорт Карелия, ТНС энерго Карелия, РУСЭНЕРГОСБЫТ, Оборонэнергосбыт, Карельская энергосбытовая компания:
    "Республика Карелия": [
        "EKOMFORT_86_calcfacthour", "KARELENE_86_calcfacthour",
        "RUSENSBI_86_calcfacthour", "OBORONSB_86_calcfacthour"
    ],

    # Коми энергосбытовая компания, Оборонэнергосбыт:
    "Республика Коми": ["KOMIENER_87_calcfacthour", "OBORONSB_87_calcfacthour"],

    # Крымэнерго:
    "Республика Крым": ["KRYMENRG_35_calcfacthour"],

    # ТНС энерго Марий Эл, Оборонэнергосбыт:
    "Республика Марий Эл": ["MARIENER_88_calcfacthour", "OBORONSB_88_calcfacthour"],

    # Ватт-Электросбыт, РУСЭНЕРГОСБЫТ, Мордовская энергосбытовая компания, Оборонэнергосбыт:
    "Республика Мордовия": [
        "ELSKVATT_89_calcfacthour", "MORDOVEN_89_calcfacthour",
        "RUSENSBI_89_calcfacthour", "OBORONSB_89_calcfacthour"
    ],

    # Россети Северный Кавказ, Севкавказэнерго:
    "Республика Северная Осетия-Алания": ["MRSKSKAV_90_calcfacthour", "SEVKAVEN_90_calcfacthour"],

    # Татэнергосбыт, Оборонэнергосбыт:
    "Республика Татарстан": ["TATENERG_92_calcfacthour", "OBORONSB_92_calcfacthour"],

    # Россети Сибирь Тываэнерго, Тываэнерго, Тываэнергосбыт:
    "Республика Тыва": ["TUVAENER_93_calcfacthour", "TUVASBYT_93_calcfacthour", ],

    # Абаканэнергосбыт, РУСЭНЕРГОСБЫТ, АтомЭнергоСбыт Бизнес, Россети Сибирь, МРСК Сибири, Оборонэнергосбыт,
    # Хакасэнергосбыт:
    "Республика Хакасия": [
        "ABAKANSB_95_calcfacthour", "RUSENSBI_95_calcfacthour",
        "REKKURSK_95_calcfacthour", "MRSKSIBR_95_calcfacthour",
        "OBORONSB_95_calcfacthour", "HAKASENE_95_calcfacthour"
    ],

    # ТНС энерго Ростов-на-Дону, Оборонэнергосбыт, Энергосбыт Ростовэнерго, ДЭС:
    "Ростовская область": [
        "ROSTOVEN_60_calcfacthour", "OBORONSB_60_calcfacthour",
        "DONENATS_60_calcfacthour"
    ],

    # РЭСК, РГМЭК, Оборонэнергосбыт:
    "Рязанская область": [
        "RYAZENER_61_calcfacthour", "RYAZENGR_61_calcfacthour",
        "OBORONSB_61_calcfacthour"
    ],

    # ТЭК, Самараэнерго, СамГЭС, ТЭС, Оборонэнергосбыт:
    "Самарская область": [
        "GPTOLESB_36_calcfacthour", "AMARAEN_36_calcfacthour",
        "SAMGESGP_36_calcfacthour", "TOLLENSB_36_calcfacthour",
        "OBORONSB_36_calcfacthour"
    ],

    # РУСЭНЕРГОСБЫТ, СПГЭС, Саратовэнерго, Оборонэнергосбыт:
    "Саратовская область": [
        "RUSENSBI_63_calcfacthour", "SARGORES_63_calcfacthour",
        "SARATENE_63_calcfacthour", "OBORONSB_63_calcfacthour"
    ],

    # ЕЭнС, ЭнергосбыТ Плюс, НТЭСК, РИР, МРСК Урала, НУЭСК, Роскоммунэнерго, Свердловэнергосбыт:
    "Свердловская область": [
        "EKATSBKO_65_calcfacthour", "ORENBENE_65_calcfacthour",
        "ORENSES3_65_calcfacthour", "OBTEPENG_65_calcfacthour",
        "MRSKURAL_65_calcfacthour", "NOVOYRAL_65_calcfacthour",
        "ROSKOMEN_65_calcfacthour", "SVERDLEN_65_calcfacthour"
    ],

    # АтомЭнергоСбыт, Оборонэнергосбыт, Смоленскэнергосбыт:
    "Смоленская область": [
        "ATOMSBYT_66_calcfacthour", "OBORONSB_66_calcfacthour",
        "SMOLENER_66_calcfacthour"
    ],

    # Будённовскэнергосбыт, Ставропольэнергосбыт, Ставрополькоммунэлектро, Пятигорские электрические сети,
    # ГОРЭЛЕКТРОСЕТЬ, Горэлектросеть, ПЭС:
    "Ставропольский край": [
        "BUDELSET_07_calcfacthour", "STAVRENE_07_calcfacthour",
        "STAVRKOM_07_calcfacthour", "PYATELSE_07_calcfacthour",
        "GORELKIS_07_calcfacthour", "NEVNGORS_07_calcfacthour"
    ],

    # Тамбовская энергосбытовая компания, ТОСК:
    "Тамбовская область": ["TAMBOVEN_68_calcfacthour", "TOSKTOSK_68_calcfacthour", ],

    # АтомЭнергоСбыт, Россети Центр, МРСК Центра, Оборонэнергосбыт, ТРАНССЕРВИСЭНЕРГО, Тверьэнергосбыт,
    # Тверьоблэнергосбыт:
    "Тверская область": [
        "ATOMSBYT_28_calcfacthour", "MRSKCENT_28_calcfacthour",
        "OBORONSB_28_calcfacthour", "TRANSERE_28_calcfacthour",
        "TVERENER_28_calcfacthour", "TVEROBLE_28_calcfacthour"
    ],

    # Томскэнергосбыт, Оборонэнергосбыт:
    "Томская область": ["TOMSKENE_69_calcfacthour", "OBORONSB_69_calcfacthour"],

    # Алексинэнергосбыт, ГП СЗ НЭСК, ТНС энерго Тула, Оборонэнергосбыт:
    "Тульская область": [
        "ALEKSNSB_70_calcfacthour", "NOVMOSSK_70_calcfacthour",
        "TULAENSK_70_calcfacthour", "OBORONSB_70_calcfacthour",
        "MRSKCPRV_70_calcfacthour"
    ],

    # Восток, Салехардэнерго, ЮТЭК, Газпром энергосбыт Тюмень, НЭСКО, ГЭС, Оборонэнергосбыт,
    # Северная энергетическая компания:
    "Тюменская область": [
        "ESVOSTOK_71_calcfacthour", "SALEHARD_71_calcfacthour",
        "UGORTEKO_71_calcfacthour", "TUMENENE_71_calcfacthour",
        "OOONESKO_71_calcfacthour", "HANTGORS_71_calcfacthour",
        "OBORONSB_71_calcfacthour", "SEVEREKO_71_calcfacthour"
    ],

    # ЭнергосбыТ Плюс, Оборонэнергосбыт:
    "Удмуртская Республика": ["ORENBENE_94_calcfacthour", "OBORONSB_94_calcfacthour"],

    # Ульяновскэнерго, Оборонэнергосбыт:
    "Ульяновская область": ["ULYANENE_73_calcfacthour", "OBORONSB_73_calcfacthour"],

    # Уралэнергосбыт, МЭК, МРСК Урала, Челябэнергосбыт, Оборонэнергосбыт, РУСЭНЕРГОСБЫТ:
    "Челябинская область": [
        "FORTUNEW_75_calcfacthour", "MAGNENKO_75_calcfacthour",
        "MRSKURAL_75_calcfacthour", "CHELENER_75_calcfacthour",
        "OBORONSB_75_calcfacthour", "RUSENSBI_75_calcfacthour"
    ],

    # Чеченэнерго, Оборонэнергосбыт, Нурэнерго:
    "Чеченская Республика": [
        "CHECHENG_96_calcfacthour", "NURENERG_96_calcfacthour",
        "OBORONSB_96_calcfacthour"
    ],

    # Чувашская энергосбытовая компания:
    "Чувашская Республика-Чувашия": ["CHUVENER_97_calcfacthour"],

    # РУСЭНЕРГОСБЫТ, ТНС энерго Ярославль, ЯСК:
    "Ярославская область": [
        "RUSENSBI_78_calcfacthour", "OBORONSB_78_calcfacthour",
        "YARENERG_78_calcfacthour",
    ]
}
