var = {
    "甲级": 3,
    "乙级": 2,
    "丙级": 1,

    "一级": 3,
    "二级": 2,
    "三级": 1,

    "A": 3,
    "B": 2,
    "C": 1,
}


content = "投标人须知前附表1.4.1投标人资格条件、能力和信誉-资质条件：具备【市政公用工程施工总承包】（资质名称）【三级以上（含三级）】（级别）"
for key in var:
    if key in content:
        print(f"Key: {key}, Value: {var[key]}")
        break
else:
    print("No key found in content.")







