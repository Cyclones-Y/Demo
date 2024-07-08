from fastapi import FastAPI
from langchain_community.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint
from langchain_wenxin.chat_models import ChatWenxin
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import  ChatPromptTemplate, PromptTemplate, MessagesPlaceholder
from pydantic import BaseModel,Field
import  uvicorn


class Score(BaseModel):
    result: str = Field(description="如果有2条获奖证书同时满足以上3项评分要求，每条0.5分，共得1分。超出部分不计入得分。")
    cause: str=Field(description="返回提供材料里符合要求的获奖证书")

app = FastAPI()

qianfan_ak = 'vxQOoOXPpMIM66yaaGhDd69Y'
qianfan_sk = 'Nbt4lY5KCMaDp0F3oe8wsEt2Gketx8rP'

llm = QianfanChatEndpoint(model_name='ERNIE-Bot-4', qianfan_ak=qianfan_ak, qianfan_sk=qianfan_sk, temperature=0.5)

#llm = ChatWenxin(model='wenxin', baidu_api_key=qianfan_ak, baidu_secret_key=qianfan_sk)
system_prompt = "请你根据我提供的材料和评分依据进行对材料的打分，我提供的材料为“工程获奖情况表”是一个json列表，列表中的每一个json子列表都是一个企业工程获奖详情内容。打分的要求为：需要你判断每一个json子列表工程获奖详情内容，评分依据有:1.工程获奖证书是否为“房屋建筑工程或市政公用工程相关行业获奖证书，”2.获奖证书年份是否为“2021年05月01日至投标截止时间：2024年5月20日”。3.奖项类别是否为省级以上。如果提供的材料满足这三项中的每一项，则得0.5分，请你返回总分，总分最高为1分。"

@app.post("/score")
def json_parser(text):
    parser = JsonOutputParser(pydantic_object=Score)
    prompt = PromptTemplate(
        template = "{system_prompt}\n{format_instructions}\n{text}\n",
        input_variables=["text"],
        partial_variables={"system_prompt": system_prompt, "format_instructions": parser.get_format_instructions()},
    )
    runnable = prompt | llm | parser
    result = runnable.invoke({"text": text})
    print(result)
    return result



if __name__ == '__main__':
    uvicorn.run("langchain_text:app",port=8080,reload=True)