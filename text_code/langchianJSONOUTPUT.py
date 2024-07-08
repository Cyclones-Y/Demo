from typing import List

from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

from langchain_community.chat_models import QianfanChatEndpoint

import json
from datetime import date





api_key = 'vxQOoOXPpMIM66yaaGhDd69Y'
secret_key = 'Nbt4lY5KCMaDp0F3oe8wsEt2Gketx8rP'


llm = QianfanChatEndpoint(model="ERNIE-Bot",
                 qianfan_ak=api_key, qianfan_sk=secret_key)


class JSONSerializableMixin:
    def as_dict(self):
        """返回一个准备用于JSON序列化的字典表示。"""
        return {k: v.isoformat() if isinstance(v, date) else v for k, v in self.__dict__.items()}

class Actor(BaseModel,JSONSerializableMixin):
    name: str = Field(description="演员姓名")
    film_names: List[str] = Field(description="他们主演的电影名称列表")

response_schemas = [
    ResponseSchema(type="bool",name="result", description=""),
    ResponseSchema(type="str",
        name="source",
        description="你输出判断的原因",
    ),
]


actor_query = "生成随机演员的电影作品列表。"

def get_json_output(qus, schema):
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas=response_schemas)
    prompt = PromptTemplate(
        template="回答用户查询。\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": output_parser.get_format_instructions()},
    )
    chain = prompt | llm | output_parser
    result = chain.invoke({"query": qus})
    return result
print(get_json_output(actor_query, Actor))
print(get_json_output(actor_query, Actor).get("result"))