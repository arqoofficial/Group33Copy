from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Text_for_check(BaseModel):
    text: str

app = FastAPI()

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

@app.get("/")
def root():
  return{"message": "Это практическая работа группы 33. Анализ тональности текста. Тест FastAPI приложения. Отправьте текст для оценки токсичности на: <адрес>/chektext/ методом POST"}

@app.post("/chektext/")
def chektext(item: Text_for_check):
  text_res = classifier(item.text)[0]
  if text_res["label"]=="NEGATIVE":
    text_out = f"По нашему мнению это негативное высказывание. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  elif text_res["label"]=="POSITIVE":
    text_out = f"По нашему мнению это доброе высказывание. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  elif text_res["label"]=="NEUTRAL":
    text_out = f"По нашему мнению это высказываение нейтрально. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  else: text_out = "Чёрт знает что хотел сказать автор"
  return text_out