import spacy

nlp = spacy.load("zh_core_web_sm")


def extract_keywords(review_requirements):
    doc = nlp(review_requirements)
    # print(doc)
    keywords = {
        "业绩类别及专业": [],
        "年份": [],
        "金额": None,
        "入库信息": []
    }

    for token in doc:
        # Extract categories and professions
        if token.text in ["施工", "工程总承包", "EPC", "市政公用工程", "公路工程", "道路", "给排水", "新建", "改造"]:
            keywords["业绩类别及专业"].append(token.text)

        # Extract dates
        #if token.like_date:
            #keywords["年份"].append(token.text)

        # Extract amounts
        if token.text.endswith("万元") or token.text.endswith("元"):
            amount = token.text.replace("万元", "").replace("元", "").replace("（含）", "")
            print(amount)
            # amount = float(token.text.replace("万元", "").replace("元", "").replace("（含）", ""))
            keywords["金额"] = amount if keywords["金额"] is None else max(keywords["金额"], amount)

        # Extract entry information
        if token.text in ["A类", "B类"]:
            keywords["入库信息"].append(token.text)

    return keywords


# Example review requirements
review_requirements = "业绩类别及专业：施工或工程总承包 (EPC)类-市政公用工程或公路工程-道路或者给排水相关专业（新建或改造） 年份：2021年05月01日至投标截止时间 金额：500万元（含）以上 分值：0.5分/个，最多得2分。 注：业绩以住建领域主体信息库A类+B类入库信息为准，时间以竣工验收时间为准。"

keywords = extract_keywords(review_requirements)
print(keywords)